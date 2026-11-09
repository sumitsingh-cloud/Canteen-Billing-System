from canteen_pkg import (
    display_menu,
    add_item,
    calculate_bill,
    apply_discount,
    generate_receipt
)
print("WELCOME TO COLLEGE CANTEEN")
order = {}
while True:
    print("\n===== MAIN MENU =====")
    print("1. View Food Menu")
    print("2. Add Food Item")
    print("3. View Current Order")
    print("4. Generate Bill")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        display_menu()
    elif choice == "2":
        display_menu()
        try:
            food_choice = int(input("Enter food number: "))
            quantity = int(input("Enter quantity: "))
            order = add_item(order, food_choice, quantity)
        except ValueError:
            print("Please enter numbers only!")
    elif choice == "3":
        print("\nYOUR CURRENT ORDER:")
        print(order)
    elif choice == "4":
        if not order:
            print("Your order is empty!")
        else:
            subtotal = calculate_bill(order)
            final_amount = apply_discount(subtotal)
            generate_receipt(
                order,
                subtotal,
                final_amount
            )
            break
    elif choice == "5":
        print("Thank you for visiting!")
        break
    else:
        print("Invalid choice! Please try again.")