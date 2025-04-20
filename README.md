Tourism Management System - Django
📌 Overview
This is a Tourism Management System built using Django, designed to help travel agencies and tour operators manage bookings, customers, destinations, and payments efficiently.

✨ Features
✅ User Authentication – Register, login, and profile management for customers and admins.
✅ Tour Packages – Add, edit, and manage tour packages with details like pricing, duration, and locations.
✅ Booking System – Customers can book tours, view their bookings, and make payments.
✅ Admin Dashboard – Manage users, tours, bookings, and payments.
✅ Payment Integration – Supports Stripe for secure online payments.
✅ Responsive UI – Works on desktop and mobile devices.

🛠️ Technologies Used
Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap, JavaScript

Database: SQLite (Default), can be configured for PostgreSQL/MySQL

Payment Gateway: Stripe API

Deployment: (Optional) Heroku, AWS, or Docker

🚀 Installation & Setup
1. Clone the Repository
bash
git clone https://github.com/SurajChadha001/Tourism_Management_System_Python.git
cd Tourism_Management_System_Python
2. Set Up a Virtual Environment (Recommended)
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
3. Install Dependencies
bash
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file and add:

env
SECRET_KEY=your_django_secret_key
DEBUG=True
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
5. Apply Migrations & Run Server
bash
python manage.py migrate
python manage.py createsuperuser  
python manage.py runserver
Visit: http://127.0.0.1:8000

🔐 Security Note
Never commit .env or sensitive keys to GitHub.

Use environment variables for SECRET_KEY, STRIPE_SECRET_KEY, etc.

Enable DEBUG=False in production.


📜 License
This project is open-source under the MIT License.

💡 How to Contribute
Fork the repository

Create a new branch (git checkout -b feature-branch)

Commit changes (git commit -m "Add new feature")

Push to the branch (git push origin feature-branch)

Open a Pull Request

