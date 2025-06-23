🐍 Django Learning Project 

Welcome to my Django learning repository! 

This repository includes all practical code examples--starting from project creation, routing, templates, models, forms, admin, database, and more.
---
## 📂 Project Structure

mystart/
├── mystart/ # Main Django settings directory
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── news/ # App: For news listing/details
│ ├── models.py
│ ├── views.py
│ ├── admin.py
│ └── ...
├── service/ # App: For services/products
│ ├── models.py
│ ├── views.py
│ └── ...
├── templates/ # HTML templates
│ ├── base.html
│ ├── MY PROJECT.html
│ └── newsDetails.html
├── static/ # Static files (images, CSS, JS)
│ └── ...
└── manage.py # Django management script


🚀 Features Covered

✅ Django Project Setup  
✅ Templates & Static Files  
✅ URL Routing  
✅ Models & Migrations  
✅ Django Admin Panel  
✅ Forms & Form Validation  
✅ GET/POST Methods  
✅ Session Management  
✅ Pagination  
✅ Search Functionality  
✅ Calculator, Even/Odd, Marksheet App  
✅ News/Service App with Admin Add/Edit  
✅ HTML + Django Template Language  
✅ and many more...

---

## 🛠 Technologies Used

- 🐍 Python 3.x
- 🌐 Django 4.x/5.x
- 💾 SQLite3 (default)
- 🖼️ HTML, CSS
- 🧠 Bootstrap (optional)
- 📦 TinyMCE (for rich text editing)


 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/django-learning-wscubetech.git
   cd django-learning-wscubetech

   Create virtual environment & activate:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Run migrations:

python manage.py migrate
Create admin user:

python manage.py createsuperuser
Start development server:

python manage.py runserver
Open your browser and go to:

http://127.0.0.1:8000/

Learnings So Far
How Django follows MVT (Model-View-Template) pattern.

How to use Django’s ORM for database operations.

Importance of Django admin and form validation.

Handling GET/POST, pagination, search bars, and dynamic URLs.
