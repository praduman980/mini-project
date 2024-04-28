class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_inventory(self):
        print("Inventory:")
        print("------------------------------")
        print("ID\tName\t\tPrice\tQuantity")
        print("------------------------------")
        for i, item in enumerate(self.items):
            print(f"{i+1}\t{item.name}\t\t₹{item.price}\t{item.quantity}")
        print("------------------------------")

    def check_balance(self, amount, balance):
        if amount <= balance:
            return True
        else:
            return False

# Sample items in the inventory
inventory = Inventory()
inventory.add_item(Item("Chips", 10, 100))
inventory.add_item(Item("Kurkure", 20, 80))
inventory.add_item(Item("Cold Drink", 30, 50))
inventory.add_item(Item("Watermelon", 40, 40))
inventory.add_item(Item("Mango", 50, 30))
inventory.add_item(Item("Almonds", 60, 20))

# User's balance
balance = 1000

# List to store the user's purchases
user_purchases = []

while True:
    print("\nYour Balance:", balance)
    inventory.display_inventory()
    
    if not inventory.items:
        print("Inventory is empty. No products available.")
        break
    
    choice = input("Enter the ID(s) of the item(s) you want to buy (separated by comma) (press 'q' to quit): ")
    
    if choice.lower() == 'q':
        break
    
    try:
        choices = [int(c.strip()) for c in choice.split(',')]
        valid_choice = True
        for c in choices:
            if c <= 0 or c > len(inventory.items):
                valid_choice = False
                break
        if valid_choice:
            quantities = input("Enter the quantity(s) (separated by comma): ")
            quantities = [int(q.strip()) for q in quantities.split(',')]
            if len(choices) == len(quantities):
                valid_quantity = True
                for q in quantities:
                    if q <= 0:
                        valid_quantity = False
                        break
                if valid_quantity:
                    purchase_valid = True
                    total_amount = 0
                    for c, q in zip(choices, quantities):
                        item = inventory.items[c-1]
                        if q > item.quantity:
                            print(f"Insufficient quantity in stock for {item.name}")
                            purchase_valid = False
                            break
                        total_amount += q * item.price
                    if purchase_valid and inventory.check_balance(total_amount, balance):
                        print("\nItems Purchased:")
                        print("------------------------------")
                        for c, q in zip(choices, quantities):
                            item = inventory.items[c-1]
                            print(f"{q} {item.name} - ₹{q * item.price}")
                            item.quantity -= q
                            user_purchases.append((item.name, q, q * item.price))
                        print("------------------------------")
                        print(f"Total Bill: ₹{total_amount}")
                        balance -= total_amount
                        print(f"Remaining Balance: ₹{balance}")
                        print("------------------------------")
                    else:
                        add_balance = input("Insufficient balance! Do you want to add a significant amount? (y/n): ")
                        if add_balance.lower() == 'y':
                            try:
                                significant_amount = int(input("Enter the significant amount you want to add: "))
                                balance += significant_amount
                                print(f"Amount added successfully! Your new balance is: ₹{balance}")
                            except ValueError:
                                print("Invalid input! Please enter a valid amount.")
                        else:
                            print("Transaction canceled.")
                else:
                    print("Invalid quantity!")
            else:
                print("Number of choices and quantities do not match!")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter valid IDs and quantities.")

print("\nThank you for shopping with us!")   
