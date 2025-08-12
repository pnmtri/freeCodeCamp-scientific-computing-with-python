class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    title = "Percentage spent by category\n"

    # Calculate total spent and category-wise spent
    spent_per_category = []
    total_spent = 0
    for cat in categories:
        spent = sum(-entry["amount"] for entry in cat.ledger if entry["amount"] < 0)
        spent_per_category.append(spent)
        total_spent += spent

    # Calculate percentage spent for each category, rounded down to nearest 10
    percentages = [int((spend / total_spent) * 100) // 10 * 10 for spend in spent_per_category]

    # Create bar chart
    chart = ""
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    # Add separator line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Prepare category names vertically
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    for i in range(max_len):
        line = "     "
        for name in names:
            line += f"{name[i] if i < len(name) else ' '}  "
        chart += line.rstrip() + "\n"

    return title + chart.rstrip("\n")

# SOME TESTS
print("Test 1: Deposit and Withdraw")
food = Category("Food")
food.deposit(500, "Initial deposit")
food.withdraw(125.75, "Groceries")
print(food)
# Expected balance: 374.25
# Expected ledger shows deposit and withdraw

print("\nTest 2: Transfer")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)
print(clothing)
# Expected: food has 'Transfer to Clothing', clothing has 'Transfer from Food'
# Food balance should be 324.25, Clothing should have 50.00

print("\nTest 3: Overdraw Attempt")
result = food.withdraw(1000, "Too much")
print("Withdrawal successful?", result)
# Expected: False, no change in ledger
print(food)

print("\nTest 4: Spend Chart")
entertainment = Category("Entertainment")
entertainment.deposit(300)
entertainment.withdraw(150, "Movies and games")

chart = create_spend_chart([food, clothing, entertainment])
print(chart)
# Should show correct percentage bars for each category

