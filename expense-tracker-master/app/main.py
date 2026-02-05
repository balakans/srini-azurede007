import requests
from utils import logger,BASE_URL

def show_menu():
    print("\n===== Expense Tracker Client =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Delete Expense")
    print("4. View All Categories")
    print("0. Exit")
    choice = input("Enter choice: ")
    return choice.strip()

def print_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n{:<5} {:<20} {:<10} {:<12} {:<15}".format("ID", "Description", "Amount", "Date", "Category"))
    print("-" * 65)
    for e in expenses:
        print("{:<5} {:<20} {:<10} {:<12} {:<15}".format(
            e.get("id", "-"),
            e.get("description", "-"),
            e.get("amount", "-"),
            e.get("date", "-"),
            e.get("category", "-")
        ))
def print_categories(categories):
    if not categories:
        print("No categories found.")
        return

    print("\n{:<5} {:<20}".format("ID", "Name"))
    print("-" * 30)
    for c in categories:
        print("{:<5} {:<20}".format(c.get("id", "-"), c.get("name", "-")))

def main():
    while True:
        choice = show_menu()

        try:
            if choice == "1":
                desc = input("Enter description: ")
                amount = float(input("Enter amount: "))
                date = input("Enter date (YYYY-MM-DD): ")
                cat_id = input("Enter category_id (or leave blank): ")
                cat_id = int(cat_id) if cat_id else None
                payload = {"description": desc, "amount": amount, "date": date, "category_id": cat_id}

                try:
                    r = requests.post(f"{BASE_URL}/add_expense", json=payload)
                    r.raise_for_status()
                    print(r.json())
                    logger.info(f"Added expense: {payload}")
                except requests.exceptions.RequestException as req_err:
                    logger.error(f"Request error while adding expense: {req_err}")
                    print("Failed to add expense. Check logs for details.")

            elif choice == "2":
                try:
                    r = requests.get(f"{BASE_URL}/get_expenses")
                    r.raise_for_status()
                    expenses = r.json()
                    print_expenses(expenses)
                    logger.info(f"Fetched {len(expenses)} expenses")
                except requests.exceptions.RequestException as req_err:
                    logger.error(f"Request error while fetching expenses: {req_err}")
                    print("Failed to fetch expenses. Check logs for details.")

            elif choice == "3":
                expense_id = input("Enter expense ID to delete: ")
                if not expense_id.isdigit():
                    print("Invalid ID.")
                    continue
                expense_id = int(expense_id)
                try:
                    r = requests.delete(f"{BASE_URL}/delete_expense/{expense_id}")
                    r.raise_for_status()
                    print(r.json())
                    logger.info(f"Deleted expense ID: {expense_id}")
                except requests.exceptions.RequestException as req_err:
                    logger.error(f"Request error while deleting expense ID {expense_id}: {req_err}")
                    print("Failed to delete expense. Check logs for details.")

            elif choice == "4":
                try:
                    r = requests.get(f"{BASE_URL}/get_categories")
                    r.raise_for_status()
                    categories = r.json()
                    print_categories(categories)
                    logger.info(f"Fetched {len(categories)} categories")
                except requests.exceptions.RequestException as req_err:
                    logger.error(f"Request error while fetching categories: {req_err}")
                    print("Failed to fetch categories. Check logs for details.")

            elif choice == "0":
                print("Exiting...")
                logger.info("User exited the program")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError as ve:
            logger.error(f"Invalid input: {ve}")
            print("Invalid input. Please enter correct values.")

        except Exception as e:
            logger.exception(f"Unexpected error: {e}")
            print("An unexpected error occurred. Check logs for details.")

if __name__ == "__main__":
    main()