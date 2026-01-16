import json
import os
import sys
from datetime import datetime

FILE_NAME = "tasks.json"

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_files():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as f:
            json.dump({}, f)
        return {}
    with open(FILE_NAME, 'r') as f:
        return json.load(f)
    
tasks = load_files()

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent= 4)


"""tasks = {1: {"status": "todo", "desc":"do your maths homework" },
         2: {"status": "todo", "desc":"clean your room"},
         3: {"status": "in progress", "desc":"send the email"},
         4: {"status": "complete", "desc":"cook food"},
         5: {"status": "in progress", "desc":"sing in the shower"}}"""

def get_new_id(tasks):
    if not tasks:
        return "1"
    return str(max(map(int, tasks.keys())) + 1)


#add
def add(task):
    
    new_id = get_new_id(tasks)

    tasks[new_id] = {      
        "id": int(new_id),
        "description": task,
        "status": "todo",
        "createdAt": now(),
        "updatedAt": now()
    }

    save_tasks(tasks)

#update
def update(id):
    id = str(id)
    if id not in tasks.keys():
        return "the id is not in ur database"
    else:
        choice = input("would you like to update task or status?")
        if(choice == "task"):
            change = input("write the updated task:")
            tasks[id]["description"] = change
        elif(choice == "status"):
            changest = input("write the updated status:")
            tasks[id]["status"] = changest
            tasks[id]["updatedAt"] = now()

def delete(id):
    id = str(id)
    if id not in tasks.keys():
        return "the id is not in ur database"
    else:
        del tasks[id]

#list all tasks
def show_all():
    for i in tasks.values():
        print("[]",i["description"],"\n")

def show_done():
    for i in tasks.values():
        if i["status"] == "done":
            print("[]",i["description"],"\n")

def show_inp():
    for i in tasks.values():
        if i["status"] == "in progress":
            print("[]",i["description"],"\n")

def show_todo():
    for i in tasks.values():
        if i["status"] == "todo":
            print("[]",i["description"],"\n")

if len(sys.argv) < 2:
    print("you need to give task description")
    sys.exit()

command = sys.argv[1]

if command == "add":
    if len(sys.argv) < 3:
        print("Error: Task description missing")
    else:
        add(sys.argv[2])
if command == "update":
    if len(sys.argv) < 3:
        print("Error: Task description missing")
    else:
        update(sys.argv[2])

if command == "delete":
    if len(sys.argv) < 3:
        print("Error: Task description missing")
    else:
        delete(sys.argv[2])

if command == "list_all":
    show_all()
if command == "list_done":
    show_done()
if command == "list_inprogress":
    show_inp()
if command == "list_todo":
    show_todo()



