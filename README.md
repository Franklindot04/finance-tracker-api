# Finance Tracker API 📊  
Production‑Ready FastAPI Backend with AWS ECS Fargate & Terraform

A lightweight, modular, and production‑ready **FastAPI** backend for tracking personal expenses — fully containerized with **Docker** and deployed to **AWS ECS Fargate** using **Terraform**.

This project demonstrates real‑world DevOps practices:
- Infrastructure as Code (**Terraform**)
- Containerization (**Docker**)
- Cloud deployment (**AWS ECS Fargate + ALB + RDS**)
- Secure VPC networking
- Logs and observability with **CloudWatch**
- CI/CD‑ready architecture

---

## 🧰 Built With

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-009688?logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-003B57?logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-ef4444?logo=pydantic&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-844FBA?logo=terraform&logoColor=white)
![AWS ECS](https://img.shields.io/badge/AWS-ECS%20Fargate-orange?logo=amazonaws&logoColor=white)

---

## 🚀 Features

- **JWT‑based authentication** (register + login)  
- **CRUD operations** for expenses  
- **SQLite** locally, **PostgreSQL (RDS)** in production  
- Modular **FastAPI** architecture (api/core/models/schemas)  
- **Dockerfile** + **docker‑compose** for local containerized runs  
- Interactive **Swagger UI** at `/docs`  
- Production deployment on **AWS ECS Fargate**  
- Infrastructure managed with **Terraform**  

---

## 🛠️ Tech Stack

### Backend
- FastAPI  
- Python 3.11  
- SQLAlchemy ORM  
- Pydantic v2  
- Uvicorn  

### Infrastructure
- Terraform  
- AWS ECS Fargate  
- AWS ECR  
- AWS RDS (PostgreSQL)  
- AWS Application Load Balancer (ALB)  
- AWS VPC (public + private subnets)  
- AWS CloudWatch Logs  
- IAM roles & policies  

---

## 🏗️ High‑Level Architecture

    Internet
        |
    Application Load Balancer (HTTP :80, public subnets)
        |
    ECS Fargate Task (FastAPI container, private subnets)
        |
    RDS PostgreSQL (private subnets)

VPC:
- Public subnets: ALB, NAT Gateway  
- Private subnets: ECS tasks, RDS  
- Security groups: least‑privilege access between ALB → ECS → RDS  

---

## 📂 Project Structure

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
    │   ├── utils/
    │   └── main.py
    │
    ├── infra/                  # Terraform IaC
    │   ├── main.tf             # Root module wiring
    │   ├── vpc.tf              # VPC, subnets, routes, IGW, NAT
    │   ├── ecs.tf              # ECS cluster, task definition, service
    │   ├── rds.tf              # RDS PostgreSQL instance
    │   ├── security.tf         # Security groups, IAM roles/policies
    │   ├── variables.tf        # Input variables
    │   ├── outputs.tf          # ALB DNS, RDS endpoint, etc.
    │   ├── terraform.tfvars.example
    │   └── ...
    │
    ├── Dockerfile
    ├── docker-compose.yml
    ├── .gitignore
    └── README.md

---

## 🔐 Authentication Flow

1. Register a user  
2. Log in to receive an `access_token`  
3. Use the token in the `Authorization` header:

    Authorization: Bearer <your_token_here>

---

## 📌 API Endpoints

### Auth

| Method | Endpoint         | Description          |
|--------|------------------|----------------------|
| POST   | /auth/register   | Register a new user  |
| POST   | /auth/login      | Login and get JWT    |

### Expenses

| Method | Endpoint          | Description               |
|--------|-------------------|---------------------------|
| POST   | /expenses/        | Create an expense         |
| GET    | /expenses/        | Get all expenses          |
| GET    | /expenses/{id}    | Get a single expense      |
| PUT    | /expenses/{id}    | Update an expense         |
| DELETE | /expenses/{id}    | Delete an expense         |

---

## 🧪 Example cURL Commands

### Create an expense

    curl -X POST "http://127.0.0.1:8000/expenses/" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <token>" \
      -d '{
        "title": "Groceries",
        "description": "Weekly food shopping",
        "amount": 45.58,
        "category": "Food"
      }'

### Get all expenses

    curl -X GET "http://127.0.0.1:8000/expenses/" \
      -H "Authorization: Bearer <token>"

---

## 🐳 Running Locally (Docker)

    docker-compose up --build

---

## 🧭 Running Locally (without Docker)

    uvicorn app.main:app --reload

---

## ⚙️ Environment Variables

### Local
- `DATABASE_URL` — defaults to SQLite (e.g. `sqlite:///./finance.db`)  
- `JWT_SECRET_KEY`  
- `JWT_ALGORITHM` (e.g. `HS256`)  
- `ACCESS_TOKEN_EXPIRE_MINUTES`  

### Production (AWS)
- `DATABASE_URL` — RDS PostgreSQL connection string  
- `JWT_SECRET_KEY` — stored securely (e.g. SSM / Secrets Manager)  
- `JWT_ALGORITHM`  
- `ACCESS_TOKEN_EXPIRE_MINUTES`  

---

## ☁️ AWS Infrastructure (Terraform)

### VPC & Networking
- VPC with CIDR block  
- Public subnets (ALB, NAT Gateway)  
- Private subnets (ECS tasks, RDS)  
- Internet Gateway + NAT Gateway  
- Route tables and associations  

### ECS & ALB
- ECS Cluster  
- Task Definition (FastAPI container)  
- ECS Service (Fargate)  
- Application Load Balancer (HTTP 80)  
- Target Group + Listener  
- Health checks for FastAPI (e.g. `/docs` or `/`)  

### Database (RDS)
- PostgreSQL instance in private subnets  
- Security group allowing traffic only from ECS tasks  
- Outputs for RDS endpoint  

### Security & IAM
- Security groups:
  - ALB → ECS  
  - ECS → RDS  
- IAM roles and policies for:
  - ECS task execution (ECR pull, CloudWatch logs)  
  - ECS task role (app‑level permissions if needed)  

### Variables & Outputs
- `variables.tf` — input variables (region, VPC CIDR, DB config, etc.)  
- `outputs.tf` — ALB DNS name, RDS endpoint, etc.  
- `terraform.tfvars.example` — template for real `terraform.tfvars` (not committed)  

---

## 🚀 Deploying to AWS (Terraform + ECS Fargate)

> Ensure `terraform.tfvars` is created locally (not committed) based on `terraform.tfvars.example`.

### 1. Initialize Terraform

    cd infra
    terraform init

### 2. Preview the infrastructure

    terraform plan

### 3. Apply the infrastructure

    terraform apply

This will create:
- VPC, subnets, routes, gateways  
- ECS cluster, ALB, target group, listener  
- RDS PostgreSQL instance  
- Security groups, IAM roles  
- CloudWatch log groups  

### 4. Build & Push Docker Image to ECR

From project root:

    docker build -t finance-api .
    docker tag finance-api:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/finance-api:latest
    docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/finance-api:latest

### 5. ECS Service

- ECS Fargate service is configured to pull the image from ECR  
- When the new image tag is used, ECS deploys a new task revision  

### 6. Access the API via ALB

Use the ALB DNS name from Terraform outputs:

    http://<alb_dns_name>/docs

---

## 📸 Screenshots (Suggested)

Add these to the README once captured:
- Terraform project structure  
- `terraform apply` successful output  
- AWS VPC view (subnets, routes)  
- ECS Cluster and Service  
- Task Definition details  
- ECR repository with pushed image  
- RDS PostgreSQL instance  
- ALB configuration + target group (healthy)  
- CloudWatch logs for ECS task  
- FastAPI `/docs` via ALB DNS  

---

## 🔒 Security Considerations

- No secrets committed  
- `.gitignore` excludes:
  - `terraform.tfvars`
  - `terraform.tfstate` / `terraform.tfstate.backup`
  - `.terraform/`
  - `.terraform.lock.hcl`
  - `__pycache__/`, `*.pyc`
  - `.DS_Store`
  - `.vscode/`
  - `finance.db`
- RDS in private subnets, not publicly accessible  
- ECS tasks communicate with RDS via security groups  
- ALB is the only public entry point  

---

## 🌱 Future Improvements

- Add categories & budgets  
- Add monthly reports and analytics  
- Add user‑specific dashboards  
- Add CI/CD pipeline (GitHub Actions → ECS Fargate)  
- Add CloudWatch alarms + autoscaling policies  
- Add WAF in front of ALB  

---

## 📄 License

This project is licensed under the **MIT License**.
