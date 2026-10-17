# CLI Task Tracker

A small command-line app for saving and managing tasks with Python. Tasks are
stored in `tasks.json` beside `task_cli.py`, so they remain available between
runs.

## Requirements

- Python 3
- No third-party packages

## Run it

Open a terminal in the project folder and run:

```powershell
python task_cli.py <command>
```

On some systems, use `python3` instead of `python`.

## Commands

### Add a task

```powershell
python task_cli.py add "Buy groceries"
```

Put the entire description in quotes if it contains spaces. Blank descriptions
are rejected.

### List tasks

```powershell
python task_cli.py list
```

Filter by status:

```powershell
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done
```

Valid statuses are `todo`, `in-progress`, and `done`.

### Update a task description

```powershell
python task_cli.py update 1 "Buy groceries and fruit"
```

Replace `1` with the task ID shown by `list`. Descriptions cannot be blank.

### Change a task's status

```powershell
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1
```

Replace `1` with the task ID.

### Delete a task

```powershell
python task_cli.py delete 1
```

Deleting a task removes it from `tasks.json`.

## Data file

The app creates or updates `tasks.json` in the same folder as `task_cli.py`.
Each task has an ID, description, status, creation time, and last-updated time.
If the data file is missing, the app starts with an empty task list. If its
JSON is corrupted or its task entries are invalid, the app reports an error;
fix the file or restore a valid copy before running a command that reads tasks.