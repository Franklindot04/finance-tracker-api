from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.expense import Expense
from app.models.user import User
from app.schemas.expense import ExpenseCreate, Expense as ExpenseSchema
from app.api.auth import get_current_user

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.get("/", response_model=list[ExpenseSchema])
def get_expenses(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(Expense).filter(Expense.user_id == current_user.id).all()


@router.get("/{expense_id}", response_model=ExpenseSchema)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    expense = (
        db.query(Expense)
        .filter(Expense.id == expense_id, Expense.user_id == current_user.id)
        .first()
    )
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense


@router.get("/filter/", response_model=list[ExpenseSchema])
def filter_expenses(
    min_amount: float | None = None,
    max_amount: float | None = None,
    category: str | None = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    query = db.query(Expense).filter(Expense.user_id == current_user.id)

    if min_amount is not None:
        query = query.filter(Expense.amount >= min_amount)
    if max_amount is not None:
        query = query.filter(Expense.amount <= max_amount)
    if category is not None:
        query = query.filter(Expense.category == category)

    return query.all()


@router.get("/summary/")
def get_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    expenses = db.query(Expense).filter(Expense.user_id == current_user.id).all()
    total = sum(e.amount for e in expenses)
    count = len(expenses)
    return {"total_amount": total, "count": count}


@router.post("/", response_model=ExpenseSchema)
def create_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_expense = Expense(
        description=expense.description,
        amount=expense.amount,
        category=expense.category,
        user_id=current_user.id,
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@router.put("/{expense_id}", response_model=ExpenseSchema)
def update_expense(
    expense_id: int,
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_expense = (
        db.query(Expense)
        .filter(Expense.id == expense_id, Expense.user_id == current_user.id)
        .first()
    )
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db_expense.description = expense.description
    db_expense.amount = expense.amount
    db_expense.category = expense.category

    db.commit()
    db.refresh(db_expense)
    return db_expense


@router.delete("/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_expense = (
        db.query(Expense)
        .filter(Expense.id == expense_id, Expense.user_id == current_user.id)
        .first()
    )
    if not db_expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(db_expense)
    db.commit()
    return {"message": "Expense deleted successfully"}

