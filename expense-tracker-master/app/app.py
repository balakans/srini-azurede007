from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils import logger
import db

app = FastAPI()

# Allow frontend (HTML/JS) to call API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================
# Pydantic Models
# ==========================
class Expense(BaseModel):
    description: str
    amount: float
    date: str
    category_id: int | None = None  # Optional category

# READ all Expenses
@app.get("/get_expenses")
def get_expenses():
    try:
        logger.info("Fetching all expenses")
        return db.fetch_expenses()
    except Exception as e:
        logger.error(f"Error in get_expenses: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch expenses")

# CREATE Expense
@app.post("/add_expense")
def add_expense(expense: Expense):
    try:
        logger.info(f"Adding expense: {expense}")
        db.insert_expense(expense.description, expense.amount, expense.date, expense.category_id)
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Error in add_expense: {e}")
        raise HTTPException(status_code=500, detail="Failed to add expense")

# DELETE Expense
@app.delete("/delete_expense/{expense_id}")
def delete_expense(expense_id: int):
    try:
        logger.info(f"Deleting expense with ID: {expense_id}")
        success = db.delete_expense(expense_id)
        if success:
            return {"status": "success", "message": f"Expense {expense_id} deleted"}
        else:
            logger.warning(f"Expense {expense_id} not found")
            raise HTTPException(status_code=404, detail=f"Expense {expense_id} not found")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in delete_expense: {e}")
        raise HTTPException(status_code=500, detail="Failed to delete expense")

# READ all Categories
@app.get("/get_categories")
def get_categories():
    try:
        logger.info("Fetching all categories")
        return db.fetch_categories()
    except Exception as e:
        logger.error(f"Error in get_categories: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch categories")
