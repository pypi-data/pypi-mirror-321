import os
from datetime import datetime
from pathlib import Path
from typing import Optional

import pyperclip
import typer
from tabulate import tabulate

from command_storage.controller.app import get_cmds
from command_storage.initializer import app
from command_storage.models.constants import DEFAULT_LIST_LIMIT
from command_storage.models.enums import arguments as arguments_enums
from command_storage.models.enums import error as error_enums

DEFAULT_FILE_LOCATION = Path().joinpath(f"command_storage_export_{datetime.now()}.json")

_INITIAL_KEY = typer.Argument(
    None,
    help=arguments_enums.Arguments.KEY.value.description,
)
_INITIAL_LIMIT = typer.Option(
    DEFAULT_LIST_LIMIT,
    arguments_enums.Arguments.LIMIT.value.long,
    arguments_enums.Arguments.LIMIT.value.short,
    help=arguments_enums.Arguments.LIMIT.value.description,
)
_INITIAL_FILE = typer.Option(
    DEFAULT_FILE_LOCATION,
    arguments_enums.Arguments.FILE.value.long,
    arguments_enums.Arguments.FILE.value.short,
    help=arguments_enums.Arguments.FILE.value.description,
)
_INITIAL_COPY_KEY = typer.Argument(
    None,
    help=arguments_enums.Arguments.KEY.value.description,
)


@app.command()
def list(key: Optional[str] = _INITIAL_KEY, limit: int = _INITIAL_LIMIT) -> None:
    """Show list of all stored commands. Also supports fuzzy matching on key. Run 'cmds
    list --help' to see how."""
    cmds = get_cmds()

    if key:
        all_commands = cmds.list_fuzzy(key, limit)
    else:
        all_commands = cmds.list(limit)

    if all_commands.error != error_enums.Error.SUCCESS:
        typer.secho(f"Error in fetching commands: '{all_commands.error}'", fg=typer.colors.RED)
        raise typer.Exit(1)

    if len(all_commands.commands) == 0:
        if key:
            msg = f"There are no commands in cmds matching with {key}"
        else:
            msg = "There are no commands in cmds"
        typer.secho(msg, fg=typer.colors.RED)
        raise typer.Exit()

    # echo commands
    table = []
    headers = ["Key", "Command", "Description"]
    terminal_width_columns: int = os.get_terminal_size().columns

    for key, command in all_commands.commands.items():
        _command = command.command
        description = command.description
        row = [f"'{key}'", f"'{_command}'", f"'{description}'" if description else ""]
        table.append(row)

    typer.secho(
        tabulate(
            table,
            headers=headers,
            tablefmt="grid",
            maxcolwidths=[int(terminal_width_columns // 4), int(terminal_width_columns // 4), int(terminal_width_columns // 4)],
        ),
        fg=typer.colors.CYAN,
    )


@app.command()
def export(file: str = _INITIAL_FILE) -> None:
    """Exports all stored commands into a JSON file."""
    cmds = get_cmds()
    all_commands = cmds.list(0)

    if all_commands.error != error_enums.Error.SUCCESS:
        typer.secho(f"Error in fetching commands: '{all_commands.error}'", fg=typer.colors.RED)
        raise typer.Exit(1)

    if len(all_commands.commands) == 0:
        msg = "There are no commands in cmds"
        typer.secho(msg, fg=typer.colors.RED)
        raise typer.Exit()

    export_error = cmds.export_json(all_commands, file)

    if export_error == error_enums.Error.SUCCESS:
        typer.secho(
            f"Successfully exported file to path: {file}: '{export_error}'",
            fg=typer.colors.GREEN,
        )
    else:
        typer.secho(
            f"Exporting file to path: {file} failed with '{export_error}'",
            fg=typer.colors.RED,
        )


@app.command()
def copy(key: str = _INITIAL_COPY_KEY) -> None:
    """Allows copying a command by its key."""
    cmds = get_cmds()

    all_commands = cmds.list(0)

    if all_commands.error != error_enums.Error.SUCCESS:
        typer.secho(f"Error in fetching commands: '{all_commands.error}'", fg=typer.colors.RED)
        raise typer.Exit(1)

    if key not in all_commands.commands:
        msg = f"There is no commands in cmds with key {key}"
        typer.secho(msg, fg=typer.colors.RED)
        raise typer.Exit()

    pyperclip.copy(all_commands.commands[key].command)

    typer.secho(
        "Copied",
        fg=typer.colors.GREEN,
    )
