import sys
import json
import os
from datetime import datetime
import shlex

FILE_NAME = os.path.join(os.path.expanduser("~"), "tasks.json")

REQUIRED_KEYS = ["id", "description", "status", "createdAt", "updatedAt"]

# task validation
def is_valid_task(task):
    if not isinstance(task, dict):
        return False
    for key in REQUIRED_KEYS:
        if key not in task:
            return False
    if not isinstance(task["id"], int):
        return False
    if task["status"] not in ["todo", "in-progress", "done"]:
        return False
    return True

def load_tasks():
    """Load saved tasks, or start with an empty list when no file exists."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            tasks = json.load(file)
            if not isinstance(tasks, list):
                print("Error: tasks.json must contain a list of tasks.")
                sys.exit(1)
            for task in tasks:
                if not is_valid_task(task):
                    print("Error: tasks.json has an invalid task entry. Fix or delete the file.")
                    sys.exit(1)
            return tasks
            
                  
    except json.JSONDecodeError:
        print("tasks.json is corrupted. Fix or delete it, then try again")
        sys.exit(1)


def save_tasks(tasks):
    """Write the current task list to disk as readable JSON."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def interactive_mode():
    print("Task Tracker CLI. Type 'help' for commands, 'exit' to quit.")
    while True:
        try:
            line = input("task> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not line:
            continue
        if line in ("exit", "quit"):
            break

        try:
            parts = shlex.split(line)
        except ValueError:
            print("Unbalanced quotes. Try again.")
            continue

        sys.argv = ["task-cli"] + parts
        main()

def main():
    if len(sys.argv) < 2:
        interactive_mode()
        return

    command = sys.argv[1]
    
    if command in ("help", "-h", "--help"):
        print_help()  

    elif command == "add":
        if len(sys.argv) < 3:
            print('Please provide a task. Example: add "Buy groceries"')
            return
        if len(sys.argv) > 3:
            print('Task description must be one argument. Put quotes around the whole description, e.g. add "Buy groceries".')
            return
        add_task(sys.argv[2])

    elif command == "list":
        if len(sys.argv) > 3:
            print("Provide at most one status: list [todo | in-progress | done].")
            return

        status = None
        if len(sys.argv) == 3:
            status = sys.argv[2]
            if status not in ["todo", "in-progress", "done"]:
                print(f"Unknown status '{status}'. Choose todo, in-progress, or done.")
                return
        list_tasks(status)

    elif command == "update":
        if len(sys.argv) < 4:
            print('Usage: update <id> "new description"')
            return
        if len(sys.argv) > 4:
            print('Description must be one argument. Put quotes around the whole description, e.g. update 1 "Buy groceries".')
            return
        if not sys.argv[2].isdigit():
            print("ID must be a number")
            return
        update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: delete <id>")
            return
        if len(sys.argv) > 3:
            print("Provide only one task ID. Usage: delete <id>")
            return
        if not sys.argv[2].isdigit():
            print("ID must be a number")
            return
        delete_task(int(sys.argv[2]))

    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Usage: mark-done <id>")
            return
        if len(sys.argv) > 3:
            print("Provide only one task ID. Usage: mark-done <id>")
            return
        if not sys.argv[2].isdigit():
            print("ID must be a number")
            return
        update_Status(int(sys.argv[2]), "done")

    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Usage: mark-in-progress <id>")
            return
        if len(sys.argv) > 3:
            print("Provide only one task ID. Usage: mark-in-progress <id>")
            return
        if not sys.argv[2].isdigit():
            print("ID must be a number")
            return
        update_Status(int(sys.argv[2]), "in-progress")

    else:
        print("Unknown command:", command)
        print("Run 'task-cli help' to see all commands.")
        

# add task
def add_task(description):
    description = description.strip()
    if not description:
        print("Description cannot be empty.")
        return
    
    tasks =  load_tasks()

    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else: 
        new_id = 1

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_id})")

# list task
def list_tasks(status=None):
    tasks = load_tasks()
    
    if status is not None:
        tasks = [task for task in tasks if task["status"] == status]

    if not tasks:
        if status is None:
            print("No tasks found.")
        else:
            print(f"No tasks with status '{status}'.")
        return
    
    for task in tasks:
        print(f"[{task['id']}] {task['description']} ({task['status']})")

# update_task
def update_task(task_id, new_Descriptions):
    new_Descriptions = new_Descriptions.strip()
    if not new_Descriptions:
        print("Description cannot be empty.")
        return
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_Descriptions
            task["updatedAt"] =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    # NO MATCH FOUND
    print(f"Task with ID {task_id} not found")

# delete task
def delete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} deleted successfully")
            return

    print(f"Task with ID {task_id} not found")

# status update
def update_Status(status_id, new_status):
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == status_id:
            task["status"] = new_status
            task["updatedAt"] =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks)
            print(f"Task {status_id} marked as {new_status}")
            return
    print(f"Task with ID {status_id} not found")

def print_help():
    print("""Task Tracker CLI

Usage: task-cli <command> [arguments]

Commands:
  add "description"          Add a new task
  list                       Show all tasks
  list todo                  Show tasks not started
  list in-progress           Show tasks in progress
  list done                  Show completed tasks
  update <id> "description"  Change a task's description
  delete <id>                Delete a task
  mark-in-progress <id>      Mark a task as in progress
  mark-done <id>             Mark a task as done
  help                       Show this message

Examples:
  task-cli add "Buy groceries"
  task-cli mark-done 1
""")

if __name__ == "__main__":
    main()