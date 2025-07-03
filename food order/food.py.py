# ...existing code...
class menuitem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def show(self):
        print(f"{self.name} - shillings {self.price}")

class vegitems(menuitem):
    def get_price(self):
        return self.price

class interitem(menuitem):
    def get_price(self):
        return self.price + 20

class order:
    def __init__(self):
        self.items = []

    def add_items(self, item):
        self.items.append(item)

    def show_bill(self):
        total = 0
        print("\nFinal bill:")
        for item in self.items:
            price = item.get_price()
            print(f"{item.name} - shillings {price}")
            total += price
        print(f"Total: shillings {total}")

class customer:
    def __init__(self, name):
        self.name = name
        self.order = order()

    def place_order(self, menu):
        while True:
            print("\nEnter item number to order (0 to finish):")
            choice = input("Your choice: ")
            if choice == '0':
                break
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(menu):
                    self.order.add_items(menu[choice - 1])
                    print(f"You ordered {menu[choice - 1].name}")
                else:
                    print("Invalid choice, please try again")
            else:
                print("Please enter a valid number.")

    def show_receipt(self):
        print(f"Receipt for {self.name}")
        self.order.show_bill()

menu = [
    vegitems("vegetable salad", 100),
    vegitems("vegetable soup", 150),
    interitem("international pizza", 200),
    interitem("international pasta", 250),
    vegitems("vegetable sandwich", 120),
    interitem("international burger", 300),
    vegitems("vegetable curry", 180),
    interitem("international noodles", 220),
    vegitems("vegetable stir-fry", 160),
    interitem("international rice", 280)
]

print("Welcome to Joshua's restaurant!")
print("Here is our menu:")
for i, item in enumerate(menu, start=1):
    print(f"{i}. ", end="")
    item.show()

customer_name = input("Enter your name: ")
customer_obj = customer(customer_name)
customer_obj.place_order(menu)
customer_obj.show_receipt()
# This code implements a simple restaurant ordering system with a menu, customer orders, and bill generation.