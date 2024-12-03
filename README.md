# Django Real-Time Chat Application

## Overview

This is a modern, responsive real-time chat application built with Django, featuring a sleek user interface and robust messaging functionality.

## Features

- 🚀 Real-time messaging
- 💬 User authentication
- 📱 Responsive design
- 🎨 Modern, clean UI
- 🔒 Secure communication

## Prerequisites

- Python 3.8+
- Django 3.2+
- pip
- virtualenv (recommended)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ikhwanand/django-chat-app.git
cd django-chat-app
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run Development Server

```bash
python manage.py runserver
```

## Project Structure

```
django-chat-app/
│
├── chat/                # Main chat application
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── static/              # Static files
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/           # HTML templates
│   └── chat/
│
├── requirements.txt     # Project dependencies
├── manage.py            # Django management script
└── README.md            # Project documentation
```

## Technologies Used

- Backend: Django
- Frontend: HTML5, CSS3, JavaScript
- Database: SQLite (default)
- Real-time: Django Channels (WebSocket)

## Customization

- Modify `settings.py` for configuration
- Adjust CSS in `static/css/` for UI changes
- Extend models in `chat/models.py`

## Security

- Uses Django's built-in authentication
- Implements CSRF protection
- Secure WebSocket connections

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/django-chat-app](https://github.com/yourusername/django-chat-app)

---

**Note**: Replace placeholders like `yourusername` and `your.email@example.com` with your actual information.
