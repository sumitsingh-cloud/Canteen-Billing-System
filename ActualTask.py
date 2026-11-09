menu={
      1: ("Sandwich",70),
      2: ("Burger", 80),
      3: ("Pizza", 120),
      4: ("Chai",10),
      5: ("Samosa", 20),
      6: ("Coffee", 30)
}
def display_menu():
    print("\n===  College Canteen Menu===")
    print("1. Sandwich Rs. 70")
    print("2. Burger Rs. 80")
    print("3. Pizza Rs. 120")
    print("4. Chai Rs. 10")
    print("5. Samosa Rs. 20")
    print("6. Coffee Rs. 30")

def add_item(order, choice, quantity):
    if choice not in menu:
        print("Invalid food choice!")
        return order
    if quantity <= 0:
        print("Quantity must be greater than zero!")
        return order
    food_name, price = menu[choice]
    if food_name in order:
        order[food_name] += quantity
    else:
        order[food_name] = quantity
    print(food_name, "added successfully!")
    return order

def calculate_bill(order):
    total = 0
    for food_name, quantity in order.items():
        for item_name, price in menu.values():
            if food_name == item_name:
                total = total + (price * quantity)
    return total

def apply_discount(total):
    if total < 0:
        print("Invalid bill amount!")
        return total
    if total >= 200:
        discount = total * 10 / 100
    else:
        discount = 0
    final_amount = total - discount
    print("Discount: Rs.", discount)
    print("Final Amount: Rs.", final_amount)
    return final_amount

def generate_receipt(order, subtotal, final_amount):
    print("\n================================")
    print("       COLLEGE CANTEEN")
    print("           RECEIPT")
    print("================================")
    if not order:
        print("No items in your order.")
    else:
        print("Item        Qty    Price    Total")
        print("--------------------------------")
        for food_name, quantity in order.items():
            for item_name, price in menu.values():
                if food_name == item_name:
                    item_total = price * quantity
                    print(food_name, "  ", quantity,
                          "   Rs.", price,
                          "   Rs.", item_total)
                    
    discount = subtotal - final_amount
    print("--------------------------------")
    print("Subtotal: Rs.", format(subtotal, ".2f"))
    print("Discount: Rs.", format(discount, ".2f"))
    print("Final Amount: Rs.", format(final_amount, ".2f"))
    print("================================")
    print("       THANK YOU! VISIT AGAIN")
    print("================================")