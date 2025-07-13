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



---

## 📦 Sample Postman Request

1. GET /classes

<img width="664" height="428" alt="{0E7135A2-BA83-4BD6-9443-073B18701C5D}" src="https://github.com/user-attachments/assets/0e674c3e-c061-4212-ab59-9960d9a22da2" />

2. POST /book

<img width="661" height="378" alt="{7A6F7A8F-9122-40C0-A72E-E73693A66B5E}" src="https://github.com/user-attachments/assets/4e042253-72e3-4977-99e8-65ce1fbebc40" />

3. GET /bookings

<img width="664" height="428" alt="{921CD3A2-9C77-48CC-A69F-8A3FB3B363B3}" src="https://github.com/user-attachments/assets/f85bb0e3-50ce-456e-af37-f6fa125fbef2" />
