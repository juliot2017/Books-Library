# Books Library API

A backend REST API for managing a books library, built with Python and FastAPI.

The project provides API endpoints for creating, retrieving, updating, and deleting books. It also includes database migrations and environment-based configuration for sensitive credentials.

## 🚀 Features

- Create books
- Get a list of books
- Get a single book
- Update book information
- Delete a book
- RESTful API architecture
- Database integration
- Database migrations with Alembic
- Environment variable configuration
- API documentation with Swagger UI
- Automatic request validation using Pydantic

## 🛠️ Technologies

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- Uvicorn
- Docker
- Git & GitHub

## 📁 Project Structure

```text
bookly/
├── .github/
│   └── workflows/
│       └── build-deploy.yml
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── README
│   └── script.py.mako
├── src/
│   ├── books/
│   ├── core/
│   │   ├── config.py
│   │   └── mail.py
│   └── __init__.py
├── tests/
├── .env
├── .gitignore
├── alembic.ini
├── docker-compose-dev.yml
├── docker-compose-prod.yml
├── Dockerfile
├── requirements.txt
└── README.md