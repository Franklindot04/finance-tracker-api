from fastapi import FastAPI
from app.api import auth, expenses
from app.core.database import init_db   # <-- THIS WAS MISSING

app = FastAPI()

# Create tables on startup
init_db()

# Authentication routes
app.include_router(auth.router)

# Expense routes
app.include_router(expenses.router)

@app.get("/")
def root():
    return {"message": "Finance Tracker API is running"}

