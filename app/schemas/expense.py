from pydantic import BaseModel

class ExpenseBase(BaseModel):
    description: str
    amount: float
    category: str


class ExpenseCreate(ExpenseBase):
    pass


class Expense(ExpenseBase):
    id: int

    class Config:
        from_attributes = True

