# AI Prompt Library

A full-stack library application to manage AI Image Generation Prompts.

## Tech Stack

- **Frontend**: Angular 17
- **Backend**: Django 4.2 (Python)
- **Database**: PostgreSQL 15
- **Cache**: Redis 7

## Quick Start

```bash
docker-compose up --build
```

Once all services are running:
- Frontend: http://localhost:4200
- Backend API: http://localhost:8000/api

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/prompts/` | List all prompts |
| POST | `/api/prompts/` | Create a new prompt |
| GET | `/api/prompts/:id/` | Get single prompt (increments view count) |

## Data Model

**Prompt**
- `id`: UUID (Primary Key)
- `title`: String (max 200 chars)
- `content`: Text
- `complexity`: Integer (1-10)
- `created_at`: Datetime

## Architecture Decisions

### 1. Redis as Source of Truth for View Counts
View counts are stored exclusively in Redis for:
- High-performance increments (atomic INCR operation)
- Reduced database load
- Fast reads on hot content

### 2. Django Without DRF
Built API using Django's native `JsonResponse` to demonstrate:
- Understanding of core Django
- Manual JSON serialization
- Decorator-based view patterns

### 3. UUID Primary Keys
Using UUIDs instead of integers to:
- Prevent ID enumeration attacks
- Support future distributed systems
- Avoid exposing business metrics

## Project Structure

```
ai-prompt-library/
├── docker-compose.yml
├── backend/
│   ├── config/          # Django settings
│   ├── prompts/         # Prompts app
│   ├── manage.py
│   └── requirements.txt
└── frontend/
    └── src/
        └── app/
            ├── app.module.ts
            ├── prompt.service.ts
            ├── prompt-list/
            ├── prompt-detail/
            └── prompt-form/
```

## Validation Rules

**Frontend (Reactive Forms)**
- Title: Min 3 characters
- Content: Min 20 characters
- Complexity: 1-10

**Backend**
- Mirrors frontend validation
- Returns structured error responses

## Development

### Backend Only
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Only
```bash
cd frontend
npm install
npm start
```

## Bonus Features Available

The architecture supports easy addition of:
- JWT Authentication (PyJWT included)
- Tagging System (Many-to-Many ready)
- Deployment (SQLite fallback in settings)
