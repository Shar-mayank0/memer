# Meme Generator and Sharing App - Backend

This project is the backend for a Meme Generator and Sharing application built with Django and Django REST Framework. Users can register, log in, upload meme templates, create and store memes, and share them via unique URLs.

---

## 📌 Objective

Develop a robust and scalable backend system using Django for a Meme Generator and Sharing App with secure authentication, template management, meme creation, and sharing features.

---

## ✅ Core Features

- User Authentication & Authorization (JWT-based)
- Meme Template Upload, List, and Delete
- Meme Creation from Templates with Custom Text
- Meme Storage and Association with Users
- Unique URL-Based Meme Sharing
- User Gallery (List/Delete User Memes)
- Public Meme Feed
- Rate Limiting on Meme Creation

---

## 🌟 Bonus Features (Optional)

- Social Authentication (Google, Facebook)
- Image Moderation and NSFW Detection
- Like, Comment, Save Memes
- Meme Analytics (Views, Shares, Likes)
- Admin Dashboard for Users and Memes

---

## 🧱 Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- PostgreSQL / SQLite
- JWT Authentication (`djangorestframework-simplejwt`)
- Cloud or Local File Storage (AWS S3 optional)
- Swagger/OpenAPI for API Docs

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/meme-backend.git
cd meme-backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file using `.env.example` as reference:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Start the Server

```bash
python manage.py runserver
```

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 📄 API Documentation

API documentation is available at `/swagger/` or `/docs/` route (based on implementation).

---

## 📁 Project Structure (planned)

```
meme-backend/
├── config/             # Django project settings
├── users/              # User registration and JWT auth
├── templates/          # Meme template upload/list/delete
├── memes/              # Meme creation, storage, sharing
├── media/              # Uploaded and generated images
├── .env.example        # Sample environment config
├── requirements.txt    # Dependencies
├── README.md           # This file
```

---

## 📬 Submission

- Upload code to a GitHub repository (public/private).
- Fill out the submission form: [Submission Form](https://forms.gle/17V2DA2P1VUR4nou5)
- Deadline: **June 27**

---

## 📜 License

This project is provided as part of an internship assignment and is intended for educational purposes only.

