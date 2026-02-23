# Finance Tracker API 📊

## 🧰 Built With

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-ef4444?logo=pydantic&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-4B8BBE?logo=python&logoColor=white)


A lightweight, production‑ready **FastAPI** backend for tracking personal expenses.  
This project includes **JWT authentication**, **SQLite database**, **Docker support**, and a clean, modular architecture suitable for real-world deployments.

---

## 🚀 Features

- User registration & login (JWT-based authentication)
- Create, read, update, and delete expenses
- SQLite database with SQLAlchemy ORM
- Pydantic schemas for validation
- Fully interactive Swagger documentation
- Dockerfile + docker-compose support
- Clean project structure following best practices

---

## 🛠️ Tech Stack

- **FastAPI**
- **Python 3.11+**
- **SQLite**
- **SQLAlchemy**
- **Pydantic v2**
- **Docker**
- **Uvicorn**

---

## 📂 Project Structure

```
finance-tracker-api/
│
├── app/
│   ├── api/
│   │   ├── auth.py
│   │   └── expenses.py
│   ├── core/
│   │   ├── auth.py
│   │   ├── database.py
│   │   └── security.py
│   ├── models/
│   ├── schemas/
│   └── main.py
│
├── finance.db
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🔐 Authentication Flow

The API uses **JWT Bearer tokens**.

1. Register a user  
2. Log in to receive an \`access_token\`  
3. Use the token in the \`Authorization\` header:

\`\`\`
Authorization: Bearer <your_token_here>
\`\`\`

---

## 📌 API Endpoints

### **Auth**
| Method | Endpoint        | Description        |
|--------|------------------|--------------------|
| POST   | \`/auth/register\` | Register a new user |
| POST   | \`/auth/login\`    | Login and get JWT   |

### **Expenses**
| Method | Endpoint            | Description               |
|--------|----------------------|---------------------------|
| POST   | \`/expenses/\`         | Create an expense         |
| GET    | \`/expenses/\`         | Get all expenses          |
| GET    | \`/expenses/{id}\`     | Get a single expense      |
| PUT    | \`/expenses/{id}\`     | Update an expense         |
| DELETE | \`/expenses/{id}\`     | Delete an expense         |

---

## 🧪 Example cURL Commands

### Create an expense
\`\`\`
curl -X POST "http://127.0.0.1:8000/expenses/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{
    "title": "Groceries",
    "description": "Weekly food shopping",
    "amount": 45.58,
    "category": "Food"
  }'
\`\`\`

### Get all expenses
\`\`\`
curl -X GET "http://127.0.0.1:8000/expenses/" \
  -H "Authorization: Bearer <token>"
\`\`\`

---

## 🐳 Running with Docker

\`\`\`
docker-compose up --build
\`\`\`

---

## 🧭 Running Locally (without Docker)

\`\`\`
uvicorn app.main:app --reload
\`\`\`

---

## 📸 Screenshots

> Screenshots will be added soon:
- Successful registration  
- Successful login  
- Successful POST /expenses  
- Successful GET /expenses  

---

## 🌱 Future Improvements

- Add categories & budgets
- Add monthly reports
- Add user-specific dashboards
- Deploy to AWS ECS Fargate with RDS PostgreSQL
- Add CI/CD pipeline (GitHub Actions → AWS)

---

## ☁️ Production Deployment on AWS

This project is designed to run locally with **SQLite** and scale to production on **AWS** using:

- **Amazon ECS Fargate** for running the Dockerized FastAPI application
- **Amazon RDS (PostgreSQL)** for a managed, production-ready database
- **Application Load Balancer (ALB)** for routing traffic to ECS tasks
- **AWS CloudWatch** for logs and basic monitoring

In production, configuration is provided via environment variables, for example:

- `DATABASE_URL` – PostgreSQL connection string (RDS)
- `JWT_SECRET_KEY` – secret key for signing JWTs
- `JWT_ALGORITHM` – algorithm used for tokens (e.g. HS256)

Locally, the app can still use **SQLite** by default, while the same container image can be deployed to ECS Fargate with a different `DATABASE_URL`.

---

## 📄 License

MIT License


