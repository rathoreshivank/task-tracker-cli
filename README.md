# CLI Task Tracker

A small command-line app for managing tasks with Python. Add tasks, mark them in progress or done, and filter them by status. Tasks are saved in a `tasks.json` file in your home folder, so they remain available between runs.

## Requirements

- Python 3.8 or newer
- No third-party packages

## Install

Install with [pipx](https://pipx.pypa.io). This makes the `task-cli` command work from any terminal:

```powershell
pipx install https://github.com/rathoreshivank/task-tracker-cli/archive/refs/tags/v1.1.0.zip
```

Or with pip:

```powershell
pip install https://github.com/rathoreshivank/task-tracker-cli/archive/refs/tags/v1.1.0.zip
```

If you have Git installed, this also works:

```powershell
pipx install git+https://github.com/rathoreshivank/task-tracker-cli.git
```

To uninstall:

```powershell
pipx uninstall task-tracker-cli
```

## Usage

Run `task-cli` without a command to enter interactive mode. See [Interactive mode](#interactive-mode) for details.

You can also run a command directly from your terminal:

```powershell
task-cli <command>
```

Run `task-cli help` to see all commands.

## Interactive mode

Start interactive mode by running `task-cli` without a command:

```powershell
task-cli
```

At the `task>` prompt, enter commands directly, without the `task-cli` prefix. For example:

```text
task> add "Buy groceries"
task> list
task> mark-done 1
```

Descriptions containing spaces should be surrounded by quotes. Type `help` to see the available commands, or `exit` or `quit` to leave interactive mode. Pressing Ctrl+C also exits.

## Commands

### Add a task

```powershell
task-cli add "Buy groceries"
```

Put the whole description in quotes. Blank descriptions are rejected.

### List tasks

```powershell
task-cli list
task-cli list todo
task-cli list in-progress
task-cli list done
```

### Update a task description

```powershell
task-cli update 1 "Buy groceries and fruit"
```

Replace `1` with the task ID shown by `list`.

### Change a task's status

```powershell
task-cli mark-in-progress 1
task-cli mark-done 1
```

### Delete a task

```powershell
task-cli delete 1
```

### Clear all tasks

```powershell
task-cli clear
task-cli clear-all
```

Both commands ask you to type `yes` before deleting all tasks. Any other response cancels the operation.

## Task statuses

Every task has one of three statuses: `todo`, `in-progress`, or `done`.

## Data file

Tasks are stored in `tasks.json` in your home folder (`C:\Users\<you>\tasks.json` on Windows, `~/tasks.json` on Mac and Linux). Each task has an ID, description, status, creation time and last-updated time.

- If the file is missing, the app starts with an empty list and creates it on the first save.
- If the file is corrupted or has invalid entries, the app shows an error instead of overwriting your data. Fix the file or delete it, then try again.

## Run without installing

```powershell
python task_cli.py <command>
```