# ✈️ TravelEase

TravelEase is a full-stack travel booking web application built using Flask and SQLite. It provides a simple and user-friendly platform where users can explore destinations, create an account, log in securely, book trips, view their bookings, and cancel bookings.

> This project was created for educational and demonstration purposes.

---

## ✨ Features

- 🌍 Explore popular travel destinations
- 👤 User registration
- 🔐 Secure user login and logout
- 🔒 Password hashing for improved security
- ✈️ Create travel bookings
- 📋 View personal bookings
- ❌ Cancel existing bookings
- 💾 SQLite database integration
- 📱 Responsive web design
- 💬 Booking success and cancellation messages
- 🧭 About and Contact sections

---

## 🛠️ Technologies Used

### Backend
- Python
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- WTForms
- Werkzeug

### Frontend
- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### Database
- SQLite

### Version Control
- Git
- GitHub

---

## 📁 Project Structure

```text
TravelEase/
│
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── images/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── booking.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── my_bookings.html
│   │   └── register.html
│   │
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   └── routes.py
│
├── .gitignore
├── config.py
├── requirements.txt
└── run.py