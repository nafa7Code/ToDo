# 📝 Smart ToDo App

A modern and user-friendly task management web application built with **Django**. Designed to help users organize their daily tasks efficiently with authentication, task tracking, and a responsive interface.

---

## 🌟 Features

- ✅ User authentication (signup, login, logout)
- 🧠 Personalized task dashboard per user
- 🗓️ Add, edit, mark as done/undone, and delete tasks
- 📱 Responsive UI with clean modern design (RTL support)
- 📸 Integrated media for custom design (e.g., login illustration)
- 🔒 Access control (only logged-in users can access their tasks)

---

## 🏗️ Technologies

- **Backend**: Django 5.x
- **Frontend**: Bootstrap 5 RTL
- **Authentication**: Django built-in auth system
- **Database**: SQLite (default, can be changed to PostgreSQL)
- **Deployment Ready**: Media/static structure and templates organized

---

## 🚀 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/todo-app.git
cd todo-app

Create virtual environment & install dependencies:

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt

python manage.py migrate

Create superuser (optional):

python manage.py createsuperuser

