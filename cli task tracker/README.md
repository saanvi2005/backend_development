# 📝 CLI Task Tracker

A simple **Command Line Interface (CLI) Task Tracker** built in Python that helps you manage your tasks directly from the terminal. You can add, update, delete, and list tasks with different statuses, and all data is stored persistently using a JSON file.

This project is beginner-friendly and focuses on understanding **CLI arguments, file handling, JSON, and basic CRUD operations**.

---

## ✨ Features

* ➕ Add new tasks
* ✏️ Update task description or status
* ❌ Delete tasks
* 📋 List all tasks
* 🔍 Filter tasks by status:

  * Todo
  * In Progress
  * Done
* 💾 Persistent storage using `tasks.json`

---

## 🛠️ Tech Stack

* Python 3
* Built-in modules only:

  * `json`
  * `os`
  * `sys`
  * `datetime`

---

## 📁 Project Structure

```
cli task tracker/
│
├── main.py        # Main CLI application
├── tasks.json     # Stores all tasks (auto-created)
└── README.md
```

---

## 🚀 How to Run

### 1️⃣ Navigate to the project folder

```bash
cd "path/to/cli task tracker"
```

### 2️⃣ Run commands using Python

General format:

```bash
python main.py <command> <arguments>
```

---

## 📌 Commands & Usage

### ➕ Add a Task

```bash
python main.py add "do maths homework"
```

---

### ✏️ Update a Task

```bash
python main.py update 1
```

You will be prompted to choose whether to update:

* task description
* task status

---

### ❌ Delete a Task

```bash
python main.py delete 1
```

---

### 📋 List Tasks

* **All tasks**

```bash
python main.py list_all
```

* **Todo tasks**

```bash
python main.py list_todo
```

* **In progress tasks**

```bash
python main.py list_inprogress
```

* **Completed tasks**

```bash
python main.py list_done
```

---

## 📂 Data Storage Format (`tasks.json`)

Example:

```json
{
  "1": {
    "id": 1,
    "description": "do maths homework",
    "status": "todo",
    "createdAt": "2026-01-16 01:45:22",
    "updatedAt": "2026-01-16 01:45:22"
  }
}
```

---

## ⚠️ Important Notes

* Always wrap task descriptions in **quotes**
* Task IDs are auto-generated
* The `tasks.json` file is created automatically if it doesn’t exist

---

## 🌱 Learning Outcomes

This project helps you understand:

* Command-line arguments (`sys.argv`)
* File handling in Python
* JSON-based persistence
* CRUD operations
* Writing real-world Python scripts

---

## 🔮 Future Improvements

* Add `mark_done` command
* Add priority levels
* Colored CLI output
* Help command (`python main.py help`)
* Convert to a pip-installable package

---

## 👩‍💻 Author

**Saanvi**
Built as a learning project to explore Python and CLI applications 🚀

---

⭐ If you liked this project, feel free to improve it and build more on top of it!
