# CLI Task Tracker

A small command-line app for saving and managing tasks with Python. 
Tasks are stored in a `tasks.json` file in your home folder, so they remain available between runs.

## Requirements

- Python 3.8 or newer
- No third-party packages

## Install

Recommended: install it with [pipx](https://pipx.pypa.io). The `task-cli`
command will then be available from your terminal:

```powershell
pipx install git+https://github.com/rathoreshivank/task-tracker-cli.git
```

You can also install it with pip:

```powershell
pip install git+https://github.com/rathoreshivank/task-tracker-cli.git
```

With pip, make sure the environment's scripts folder is on your PATH to run
`task-cli` directly.

## Run without installing

From the project folder, run the Python file directly:

```powershell
python task_cli.py <command>
```

For example:

```powershell
python task_cli.py list
```

## Usage

```powershell
task-cli <command>
```

## Commands

### Add a task

```powershell
task-cli add "Buy groceries"
```

Put the entire description in quotes if it contains spaces. Blank descriptions
are rejected.

### List tasks

```powershell
task-cli list
```

Filter by status:

```powershell
task-cli list todo
task-cli list in-progress
task-cli list done
```

Valid statuses are `todo`, `in-progress`, and `done`.

### Update a task description

```powershell
task-cli update 1 "Buy groceries and fruit"
```

Replace `1` with the task ID shown by `list`. Descriptions cannot be blank.

### Change a task's status

```powershell
task-cli mark-in-progress 1
task-cli mark-done 1
```

Replace `1` with the task ID.

### Delete a task

```powershell
task-cli delete 1
```

Deleting a task removes it from `tasks.json`.

## Data file

The app creates or updates `tasks.json` in your home folder (~/tasks.json).
Each task has an ID, description, status, creation time, and last-updated time.
If the data file is missing, the app starts with an empty task list. If its
JSON is corrupted or its task entries are invalid, the app reports an error;
fix the file or restore a valid copy before running a command that reads tasks.