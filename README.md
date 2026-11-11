# Canteen Billing System

A simple menu-driven **Python** program that manages food orders, calculates the bill, applies a discount automatically, and prints a formatted receipt.

> **Course:** Python Programming (25BCA3C03) | **Activity 2:** Python Package Development
> **Department:** CS and IT, JAIN (Deemed-to-be University) | **Semester:** 3rd
> **Submitted to:** Dr. Ramkumar Krishnamoorthy

---

## Student Details

| S. No. | USN | Name |
|:------:|-----|------|
| 1 | 25BCAR0411 | Sumit Singh |

---

## Problem Statement

Prepare an itemized bill for a canteen, apply the discount, and show the final amount.

## Features

- Shows a numbered **menu** of 6 canteen items with prices
- The user simply types the **item number** and **quantity**, and the item is added to the order
- Adding the same item again increases its quantity (no duplicate lines)
- Option to **view the current order** at any time
- **Automatic 10% discount** on bills of Rs. 200 or more
- Prints a neat **itemized receipt** with the subtotal, discount and final amount
- **Input validation:** wrong food number, letters instead of numbers, zero/negative quantity, wrong menu choice, and generating a bill with an empty order are all handled

### Menu

| No. | Item | Price |
|:---:|------|------:|
| 1 | Sandwich | Rs. 70 |
| 2 | Burger | Rs. 80 |
| 3 | Pizza | Rs. 120 |
| 4 | Chai | Rs. 10 |
| 5 | Samosa | Rs. 20 |
| 6 | Coffee | Rs. 30 |

### Discount Rule

| Subtotal | Discount |
|----------|----------|
| Less than Rs. 200 | 0% |
| Rs. 200 or more | 10% |

**Calculation:**
```
discount     = subtotal x 10 / 100      (only if subtotal >= 200)
final amount = subtotal - discount
```

**Example:** Subtotal Rs. 200 -> Discount Rs. 20 -> Final Amount Rs. 180

---

## Project Structure

```
CanteenBilling/
├── canteen_pkg/            # user-defined Python package
│   ├── __init__.py         # makes the folder a package, exposes the functions
│   └── ActualTask.py       # menu and function definitions
├── main.py                 # executable program (run this file)
├── sample_output.txt       # sample run of the program
└── README.md
```

### Functions in `canteen_pkg/ActualTask.py`

| Function | Purpose |
|----------|---------|
| `display_menu()` | Prints the canteen menu |
| `add_item(order, choice, quantity)` | Validates the choice and quantity, then adds the item to the order (or increases its quantity) and returns the order |
| `calculate_bill(order)` | Returns the subtotal of the order |
| `apply_discount(total)` | Gives 10% off when the total is Rs. 200 or more and returns the final amount |
| `generate_receipt(order, subtotal, final_amount)` | Prints the itemized receipt |

---

## How to Run

**Requirements:** Python 3 installed. No extra libraries are needed.

```bash
# 1. Clone the repository
git clone <YOUR-GITHUB-REPO-URL>

# 2. Go into the project folder
cd CanteenBilling

# 3. Run the program
python main.py
```

(On some systems use `python3 main.py` instead.)

### How to use the program

1. The **MAIN MENU** appears. Type an option number and press Enter.
   - `1` - View the food menu
   - `2` - Add a food item
   - `3` - View the current order
   - `4` - Generate the bill
   - `5` - Exit
2. For option `2`, type the **food number**, then the **quantity**. The item is added.
3. Repeat for more items.
4. Choose `4` to print the final receipt (the program ends after the bill is generated).

---

## Sample Output

```
WELCOME TO COLLEGE CANTEEN

===== MAIN MENU =====
1. View Food Menu
2. Add Food Item
3. View Current Order
4. Generate Bill
5. Exit
Enter your choice: 2

===  College Canteen Menu===
1. Sandwich Rs. 70
2. Burger Rs. 80
3. Pizza Rs. 120
4. Chai Rs. 10
5. Samosa Rs. 20
6. Coffee Rs. 30
Enter food number: 1
Enter quantity: 2
Sandwich added successfully!
        ... (more items added) ...
Enter your choice: 3

YOUR CURRENT ORDER:
{'Sandwich': 2, 'Pizza': 1, 'Chai': 5}

Enter your choice: 4
Discount: Rs. 31.0
Final Amount: Rs. 279.0

================================
       COLLEGE CANTEEN
            RECEIPT
================================
Item        Qty    Price    Total
--------------------------------
Sandwich    2    Rs. 70    Rs. 140
Pizza    1    Rs. 120    Rs. 120
Chai    5    Rs. 10    Rs. 50
--------------------------------
Subtotal: Rs. 310.00
Discount: Rs. 31.00
Final Amount: Rs. 279.00
================================
      THANK YOU! VISIT AGAIN
================================
```

A full test run (including invalid inputs) is saved in [`sample_output.txt`](sample_output.txt).

---

## Test Cases

| # | Test | Input | Expected result |
|---|------|-------|-----------------|
| 1 | Normal bill, no discount | Pizza x1, Sandwich x1 | Subtotal 190.00, discount 0.00, **final 190.00** |
| 2 | Bill exactly at Rs. 200 | Pizza x1, Burger x1 | Subtotal 200.00, discount 20.00, **final 180.00** |
| 3 | Bill above Rs. 200 | Sandwich x2, Pizza x1, Chai x5 | Subtotal 310.00, discount 31.00, **final 279.00** |
| 4 | Same item added twice | Chai x2, then Chai x3 | One entry: `{'Chai': 5}` |
| 5 | Generate bill with empty order | `4` before ordering | "Your order is empty!" |
| 6 | Invalid food number | `99` | "Invalid food choice!" |
| 7 | Letters instead of numbers | `abc` | "Please enter numbers only!" |
| 8 | Zero quantity | `0` | "Quantity must be greater than zero!" |
| 9 | Negative quantity | `-2` | "Quantity must be greater than zero!" |
| 10 | Invalid main menu option | `9` | "Invalid choice! Please try again." |

All the above test cases passed.

---

## Python Concepts Used

- **Unit 1:** `print`, `input`, `if/elif/else`, `while` and `for` loops, strings, functions
- **Unit 2:** dictionaries (the menu and the order), tuples (menu entries such as `("Pizza", 120)`)
- **Unit 3:** exception handling (`try/except ValueError`)
- **Package development:** a user-defined package (`canteen_pkg`) with `__init__.py` and a module, imported in `main.py`


## Learning Outcomes

This project helped me understand how to create a user-defined Python package, organize code into modules, develop reusable functions, handle user input, and perform project testing.

---

Developed as part of Activity 2 - Python Package Development, JAIN (Deemed-to-be University)
