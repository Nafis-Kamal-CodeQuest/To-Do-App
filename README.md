# 📝 Task Manager (CLI Todo App)

A simple command-line **Task Manager** built with Python.  
This project was created to practice **file handling, modular programming, and basic CRUD operations** in Python.

---

## 🚀 Features
- ➕ **Add Tasks** – Save new todos into a file  
- 📋 **View Tasks** – Display all saved tasks with numbering  
- ✏️ **Edit Tasks** – Update existing tasks by index  
- ❌ **Delete Tasks** – Remove tasks by index  
- 💾 **Persistent Storage** – Tasks are saved in `todos.txt` and loaded on each run  

---

## 🛠️ Tech Stack
- **Language**: Python 3  
- **Storage**: Text File (`todos.txt`)  

---

## 📂 Project Structure
📁 todo-app
│── main.py # Main menu loop
│── functions.py # Core task functions (CRUD)
│── todos.txt # Task storage (auto-created if missing)
│── README.md # Project documentation


---

## ▶️ Usage

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/todo-app.git
   cd todo-app


Run the program:

python main.py


Follow the on-screen menu:

----- Welcome To Task Manager -----
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Exit

📸 Example
----- Welcome To Task Manager -----
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Exit
Enter your choice: 1
Write the task: Buy groceries
✅ Task Added

🌟 Future Improvements

Add task priorities and due dates

Store tasks in JSON or SQLite instead of plain text

Build a GUI (Tkinter/PyQt) or a Flask web version

Add a search/filter option
