# 🧘‍♀️ Fitness Studio Booking API

A simple Django RESTful API for a fictional fitness studio that allows users to:

- View available fitness classes
- Book a class
- View their own bookings

---

## 📦 Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- SQLite (in-memory DB)
- Logging, validation, timezone support

---

## 🚀 Features

- ✅ View all **upcoming** classes (`GET /classes`)
- ✅ Book a class with email (`POST /book`)
- ✅ Prevent duplicate bookings
- ✅ Prevent booking past or full classes
- ✅ View your bookings by email (`GET /bookings?email=...`)
- ✅ Logs booking actions in console
- ✅ Formatted IST timestamps: `15-07-2025 08 AM`

---

## 🛠 Setup Instructions (Windows)

### 📁 Clone & Setup

```bash
git clone https://github.com/VyshnavR/fitnessbooking.git
cd fitnessbooking

🐍 Create & Activate Virtual Environment
python -m venv env
env\Scripts\activate

📦 Install Dependencies
pip install -r requirements.txt

🛠 Run Migrations
python manage.py migrate

🌱 Load Sample Data
python manage.py loaddata data.json

▶️ Start the Server
python manage.py runserver
