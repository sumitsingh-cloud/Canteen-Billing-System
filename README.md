# Canteen-Billing-System

About the Project

The Canteen Billing System is a Python-based project developed using a user-defined package. It helps manage food orders, calculate bills, apply discounts, and generate receipts through an interactive menu-driven program.

This project demonstrates Python package creation, modular programming, reusable functions, dictionaries, loops, conditional statements, and input validation.

Features

- Display available food items and prices.
- Add food items to an order.
- Update quantity when the same item is added again.
- Calculate the total bill automatically.
- Apply a 10% discount on bills of ₹200 or more.
- Generate a formatted receipt.
- Validate invalid food choices and quantities.
- Interactive menu-driven interface.

Project Structure

CanteenBilling/
│
├── canteen_pkg/
│   ├── init.py
│   └── ActualTask.py
│
├── main.py
└── README.md

Technologies Used

- Python 3
- User-defined Python packages
- Functions and modules
- Dictionaries and tuples
- Loops and conditional statements
- Exception handling

How to Run

1. Download or clone this repository.
2. Open the project folder in your Python IDE or terminal.
3. Run the following command:

python main.py

Discount Rule

A 10% discount is applied when the subtotal is ₹200 or above.

Example:

- Subtotal: ₹200
- Discount: ₹20
- Final Amount: ₹180

Testing

The project was tested with:

- Normal food orders.
- Empty orders.
- Invalid food choices.
- Zero and negative quantities.
- Duplicate food items.
- Discount calculations below, at, and above ₹200.

All the above test cases passed.

Learning Outcomes

This project helped me understand how to create a user-defined Python package, organize code into modules, develop reusable functions, handle user input, and perform project testing.

Author

Sumit Singh
BCA Student
