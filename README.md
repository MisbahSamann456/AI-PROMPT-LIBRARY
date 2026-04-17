# 🚀 AI Prompt Library

A full-stack application to manage AI Image Generation Prompts with a clean API and interactive UI.

---

## ⚡ Live Features

- View all prompts
- Add prompts (API)
- Complexity tagging (1–10)
- Dynamic frontend rendering
- View count system (simulated)

---

## 🛠 Tech Stack

- Frontend: Angular
- Backend: Django (without DRF)
- Database: SQLite (for fast local setup)
- Cache: Redis (conceptual, fallback used)

---

## ⚡ How to Run

### Backend
```bash
cd backend
python manage.py migrate
python manage.py runserver
