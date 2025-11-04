# 📝 To-Do List App (Flask)
A simple and elegant **To-Do List Web Application** built using **Flask (Python)**. It allows users to **add, update, delete, and manage tasks** efficiently — a great project to learn Flask CRUD operations, templates, and database integration.
---
## 🚀 Features
- ✅ Add new tasks  
- ✏️ Edit or update existing tasks  
- 🗑️ Delete tasks  
- 📋 View all tasks in a clean UI  
- 💾 Data persistence using SQLite  
- 🌐 Flask + HTML + CSS + Bootstrap frontend  
- 🧩 Modular structure using Blueprints  
---
## 🛠️ Tech Stack
| Category | Technologies |
|-----------|---------------|
| Backend | Python, Flask |
| Frontend | HTML, CSS, Bootstrap |
| Database | SQLite |
| Server | Gunicorn (for deployment) |
---
## 📂 Project Structure
```
To_Do_list_app1/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   ├── index.html
│   └── base.html
├── static/                 # CSS / JS / Images
│   ├── style.css
│   └── script.js
├── instance/
│   └── todo.db             # SQLite database (auto-created)
└── README.md               # Project documentation
```
---
## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/To_Do_list_app1.git
cd To_Do_list_app1
```
### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the App
```bash
python app.py
```
The app will start running at:  
👉 **http://127.0.0.1:5000/**
---
## 🗄️ Database Setup
The app uses **SQLite** (created automatically when you run it for the first time). If you modify models, you can delete the existing `todo.db` and let Flask recreate it.
---
## 🚀 Deployment (on Render / Railway / Heroku)
1. Push your code to GitHub  
2. Add a `requirements.txt` file  
3. Create a `Procfile` with:
   ```
   web: gunicorn app:app
   ```
4. Deploy using:
   - [Render.com](https://render.com)
   - [Railway.app](https://railway.app)
   - [Heroku](https://heroku.com)
---
## 🧠 Future Enhancements
- 🔐 User authentication system (login/signup)
- 🕒 Task deadlines and reminders
- 🎨 Dark mode toggle
- ☁️ Deploy on cloud with persistent database
---
## 👨‍💻 Author
**Aniket Kumar**  
📧  aniketkumarsonu62@gmail.com
🌐 [https://github.com/CARLOX62](https://github.com/CARLOX62)
---
## 🏷️ License
This project is licensed under the **MIT License** — free to use and modify.
---
⭐ **If you like this project, don’t forget to star it on GitHub!**
