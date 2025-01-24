# Copyright 2024 John Sirois.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import annotations

import itertools
import os
from collections import defaultdict
from pathlib import Path
from typing import Any, Container, Iterable, Iterator, Mapping, Set, cast

from dev_cmd.errors import InvalidModelError
from dev_cmd.expansion import expand
from dev_cmd.model import Command, Configuration, ExitStyle, Factor, Group, Task
from dev_cmd.placeholder import Environment
from dev_cmd.project import PyProjectToml


def _assert_list_str(obj: Any, *, path: str) -> list[str]:
    if not isinstance(obj, list) or not all(isinstance(item, str) for item in obj):
        raise InvalidModelError(
            f"Expected value at {path} to be a list of strings, but given: {obj} of type "
            f"{type(obj)}."
        )
    return cast("list[str]", obj)


def _assert_dict_str_keys(obj: Any, *, path: str) -> dict[str, Any]:
    if not isinstance(obj, dict) or not all(isinstance(key, str) for key in obj):
        raise InvalidModelError(
            f"Expected value at {path} to be a dict with string keys, but given: {obj} of type "
            f"{type(obj)}."
        )
    return cast("dict[str, Any]", obj)


def _parse_commands(
    commands: dict[str, Any] | None,
    required_steps: dict[str, list[tuple[Factor, ...]]],
    project_dir: Path,
) -> Iterator[Command]:
    if not commands:
        raise InvalidModelError(
            "There must be at least one entry in the [tool.dev-cmd.commands] table to run "
            "`dev-cmd`."
        )

    for name, data in commands.items():
        extra_env: list[tuple[str, str]] = []
        if isinstance(data, list):
            args = tuple(_assert_list_str(data, path=f"[tool.dev-cmd.commands] `{name}`"))
            cwd = project_dir
            accepts_extra_args = False
        else:
            command = _assert_dict_str_keys(data, path=f"[tool.dev-cmd.commands.{name}]")

            for key, val in _assert_dict_str_keys(
                command.pop("env", {}), path=f"[tool.dev-cmd.commands.{name}] `env`"
            ).items():
                if not isinstance(val, str):
                    raise InvalidModelError(
                        f"The env variable {key} must be a string, but given: {val} of type "
                        f"{type(val)}."
                    )
                extra_env.append((key, val))

            try:
                args = tuple(
                    _assert_list_str(
                        command.pop("args"), path=f"[tool.dev-cmd.commands.{name}] `args`"
                    )
                )
            except KeyError:
                raise InvalidModelError(
                    f"The [tool.dev-cmd.commands.{name}] table must define an `args` list."
                )

            cwd = Path(command.pop("cwd", project_dir))
            if not cwd.is_absolute():
                cwd = project_dir / cwd
            cwd = cwd.resolve()
            if not project_dir == Path(os.path.commonpath((project_dir, cwd))):
                raise InvalidModelError(
                    f"The resolved path of [tool.dev-cmd.commands.{name}] `cwd` lies outside the "
                    f"project: {cwd}"
                )

            accepts_extra_args = command.pop("accepts-extra-args", False)
            if not isinstance(accepts_extra_args, bool):
                raise InvalidModelError(
                    f"The [tool.dev-cmd.commands.{name}] `accepts-extra-args` value must be either "
                    f"`true` or `false`, given: {accepts_extra_args} of type "
                    f"{type(accepts_extra_args)}."
                )
            if data:
                raise InvalidModelError(
                    f"Unexpected configuration keys in the [tool.dev-cmd.commands.{name}] table: "
                    f"{' '.join(data)}"
                )

        env = Environment()
        for factors in required_steps[name]:
            factors_suffix = f"-{'-'.join(factors)}" if factors else ""

            used_factors: set[Factor] = set()

            def substitute(text: str) -> str:
                substituted, consumed_factors = env.substitute(text, *factors)
                used_factors.update(consumed_factors)
                return substituted

            substituted_args = [substitute(arg) for arg in args]
            substituted_extra_env = [(key, substitute(value)) for key, value in extra_env]

            unused_factors = [factor for factor in factors if factor not in used_factors]
            if unused_factors:
                if len(unused_factors) == 1:
                    raise InvalidModelError(
                        f"The {name} command was parameterized with unused factor "
                        f"'-{unused_factors[0]}'."
                    )
                else:
                    head = ", ".join(f"'-{factor}'" for factor in unused_factors[:-1])
                    tail = f"'-{factors[-1]}'"
                    raise InvalidModelError(
                        f"The {name} command was parameterized with unused factors "
                        f"{head} and {tail}."
                    )

            yield Command(
                f"{name}{factors_suffix}",
                tuple(substituted_args),
                extra_env=tuple(substituted_extra_env),
                cwd=cwd,
                accepts_extra_args=accepts_extra_args,
            )


def _parse_group(
    task: str,
    group: list[Any],
    all_task_names: Container[str],
    tasks_defined_so_far: Mapping[str, Task],
    commands: Mapping[str, Command],
) -> Group:
    members: list[Command | Task | Group] = []
    for index, member in enumerate(group):
        if isinstance(member, str):
            for item in expand(member):
                try:
                    members.append(commands.get(item) or tasks_defined_so_far[item])
                except KeyError:
                    if item in all_task_names:
                        raise InvalidModelError(
                            f"The [tool.dev-cmd.tasks] step `{task}[{index}]` forward-references "
                            f"task {item!r}. Tasks can only reference other tasks that are defined "
                            f"earlier in the file"
                        )
                    available_tasks = (
                        " ".join(sorted(tasks_defined_so_far)) if tasks_defined_so_far else "<None>"
                    )
                    available_commands = " ".join(sorted(commands))
                    raise InvalidModelError(
                        os.linesep.join(
                            (
                                f"The [tool.dev-cmd.tasks] step `{task}[{index}]` is not the name "
                                f"of a defined command or task: {item!r}",
                                "",
                                f"Available tasks: {available_tasks}",
                                f"Available commands: {available_commands}",
                            )
                        )
                    )
        elif isinstance(member, list):
            members.append(
                _parse_group(
                    task=f"{task}[{index}]",
                    group=member,
                    all_task_names=all_task_names,
                    tasks_defined_so_far=tasks_defined_so_far,
                    commands=commands,
                )
            )
        else:
            raise InvalidModelError(
                f"Expected value at [tool.dev-cmd.tasks] `{task}`[{index}] to be a string "
                f"or a list of strings, but given: {member} of type {type(member)}."
            )
    return Group(members=tuple(members))


def _parse_tasks(tasks: dict[str, Any] | None, commands: Mapping[str, Command]) -> Iterator[Task]:
    if not tasks:
        return

    tasks_by_name: dict[str, Task] = {}
    for name, group in tasks.items():
        if name in commands:
            raise InvalidModelError(
                f"The task {name!r} collides with command {name!r}. Tasks and commands share the "
                f"same namespace and the names must be unique."
            )
        if not isinstance(group, list):
            raise InvalidModelError(
                f"Expected value at [tool.dev-cmd.tasks] `{name}` to be a list containing "
                f"strings or lists of strings, but given: {group} of type {type(group)}."
            )
        task = Task(
            name=name,
            steps=_parse_group(
                task=name,
                group=group,
                all_task_names=frozenset(tasks),
                tasks_defined_so_far=tasks_by_name,
                commands=commands,
            ),
        )
        tasks_by_name[name] = task
        yield task


def _parse_default(
    default: Any, commands: Mapping[str, Command], tasks: Mapping[str, Task]
) -> Command | Task | None:
    if default is None:
        if len(commands) == 1:
            return next(iter(commands.values()))
        return None

    if not isinstance(default, str):
        raise InvalidModelError(
            f"Expected [tool.dev-cmd] `default` to be a string but given: {default} of type "
            f"{type(default)}."
        )

    try:
        return tasks.get(default) or commands[default]
    except KeyError:
        raise InvalidModelError(
            os.linesep.join(
                (
                    f"The [tool.dev-cmd] `default` {default!r} is not the name of a defined "
                    "command or task.",
                    "",
                    f"Available tasks: {' '.join(sorted(tasks)) if tasks else '<None>'}",
                    f"Available commands: {' '.join(sorted(commands))}",
                )
            )
        )


def _parse_exit_style(exit_style: Any) -> ExitStyle | None:
    if exit_style is None:
        return None

    if not isinstance(exit_style, str):
        raise InvalidModelError(
            f"Expected [tool.dev-cmd] `exit-style` to be a string but given: {exit_style} of type "
            f"{type(exit_style)}."
        )

    try:
        return ExitStyle(exit_style)
    except ValueError:
        raise InvalidModelError(
            f"The [tool.dev-cmd] `exit-style` of {exit_style!r} is not recognized. Valid choices "
            f"are {', '.join(repr(es.value) for es in list(ExitStyle)[:-1])} and "
            f"{list(ExitStyle)[-1].value!r}."
        )


def _parse_grace_period(grace_period: Any) -> float | None:
    if grace_period is None:
        return None

    if not isinstance(grace_period, (int, float)):
        raise InvalidModelError(
            f"Expected [tool.dev-cmd] `grace-period` to be a number but given: {grace_period} of "
            f"type {type(grace_period)}."
        )

    return float(grace_period)


def _iter_all_required_step_names(
    value: Any, tasks_data: Mapping[str, Any], seen: Set[str]
) -> Iterator[str]:
    if isinstance(value, str) and value not in seen:
        for name in expand(value):
            seen.add(name)
            yield name
            if task_data := tasks_data.get(name):
                yield from _iter_all_required_step_names(task_data, tasks_data, seen)
    elif isinstance(value, list):
        for item in value:
            yield from _iter_all_required_step_names(item, tasks_data, seen)


def _gather_all_required_step_names(
    requested_step_names: Iterable[str], tasks_data: Mapping[str, Any]
) -> tuple[str, ...]:
    required_step_names: list[str] = []
    seen: set[str] = set()
    for requested_step_name in dict.fromkeys(itertools.chain(requested_step_names, tasks_data)):
        required_step_names.extend(
            _iter_all_required_step_names(requested_step_name, tasks_data, seen)
        )
    return tuple(dict.fromkeys(required_step_names))


def parse_dev_config(pyproject_toml: PyProjectToml, *requested_steps: str) -> Configuration:
    pyproject_data = pyproject_toml.parse()
    try:
        dev_cmd_data = _assert_dict_str_keys(
            pyproject_data["tool"]["dev-cmd"], path="[tool.dev-cmd]"
        )  # type: ignore[index]
    except KeyError as e:
        raise InvalidModelError(
            f"The commands, tasks and defaults run-dev acts upon must be defined in the "
            f"[tool.dev-cmd] table in {pyproject_toml}: {e}"
        )

    def pop_dict(key: str, *, path: str) -> dict[str, Any] | None:
        data = dev_cmd_data.pop(key, None)
        return _assert_dict_str_keys(data, path=path) if data else None

    commands_data = pop_dict("commands", path="[tool.dev-cmd.commands]") or {}
    tasks_data = pop_dict("tasks", path="[tool.dev-cmd.tasks]") or {}
    default_step_name = dev_cmd_data.pop("default", None)

    required_steps: defaultdict[str, list[tuple[Factor, ...]]] = defaultdict(list)
    required_step_names = _gather_all_required_step_names(requested_steps, tasks_data)
    known_names = tuple(itertools.chain(commands_data, tasks_data))
    for required_step_name in required_step_names:
        if required_step_name in known_names:
            required_steps[required_step_name].append(())
            continue
        for known_name in known_names:
            if not required_step_name.startswith(f"{known_name}-"):
                continue

            required_steps[known_name].append(
                tuple(
                    Factor(factor)
                    for factor in required_step_name[len(known_name) + 1 :].split("-")
                )
            )
            break

    commands = {
        cmd.name: cmd
        for cmd in _parse_commands(
            commands_data, required_steps, project_dir=pyproject_toml.path.parent
        )
    }
    if not commands:
        raise InvalidModelError(
            "No commands are defined in the [tool.dev-cmd.commands] table. At least one must be "
            "configured to use the dev task runner."
        )

    tasks = {task.name: task for task in _parse_tasks(tasks_data, commands)}
    default = _parse_default(default_step_name, commands, tasks)
    exit_style = _parse_exit_style(dev_cmd_data.pop("exit-style", None))
    grace_period = _parse_grace_period(dev_cmd_data.pop("grace-period", None))

    if dev_cmd_data:
        raise InvalidModelError(
            f"Unexpected configuration keys in the [tool.dev-cmd] table: {' '.join(dev_cmd_data)}"
        )

    return Configuration(
        commands=tuple(commands.values()),
        tasks=tuple(tasks.values()),
        default=default,
        exit_style=exit_style,
        grace_period=grace_period,
        source=pyproject_toml.path,
    )
