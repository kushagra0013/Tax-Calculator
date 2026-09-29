NEW_SLABS = [
    (300000, 0.00),
    (600000, 0.05),
    (900000, 0.10),
    (1200000, 0.15),
    (1500000, 0.20),
    (float("inf"), 0.30),
]

OLD_SLABS = [
    (250000, 0.00),
    (500000, 0.05),
    (1000000, 0.20),
    (float("inf"), 0.30),
]

CESS_RATE = 0.04 
HISTORY_FILE = "history.txt"


def calculate_tax(income, slabs):
    tax = 0
    lower = 0
    for upper, rate in slabs:
        if income > lower:
            taxable_part = min(income, upper) - lower
            tax += taxable_part * rate
            lower = upper
    return tax


def add_cess(tax):
    return tax + tax * CESS_RATE


def get_income():
    while True:
        try:
            income = float(input("Enter annual income (Rs.): "))
            if income < 0:
                print("Income cannot be negative.")
            else:
                return income
        except ValueError:
            print("Please enter a valid number.")


def save_to_history(income, new_tax, old_tax):
    with open(HISTORY_FILE, "a") as f:
        f.write(f"Income: {income:.2f} | New: {new_tax:.2f} | Old: {old_tax:.2f}\n")


def show_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            lines = f.readlines()
        if not lines:
            print("No history yet.")
        else:
            print("\n--- Past Calculations ---")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No history yet.")


def calculate_and_compare():
    income = get_income()

    new_tax = add_cess(calculate_tax(income, NEW_SLABS))
    old_tax = add_cess(calculate_tax(income, OLD_SLABS))

    print("\n--- Result (includes 4% cess) ---")
    print(f"Income         : Rs. {income:,.2f}")
    print(f"New Regime Tax : Rs. {new_tax:,.2f}")
    print(f"Old Regime Tax : Rs. {old_tax:,.2f}")

    if new_tax < old_tax:
        print(f"New Regime saves you Rs. {old_tax - new_tax:,.2f}")
    elif old_tax < new_tax:
        print(f"Old Regime saves you Rs. {new_tax - old_tax:,.2f}")
    else:
        print("Both regimes give the same tax.")

    save_to_history(income, new_tax, old_tax)


def main():
    print("=" * 40)
    print("   INCOME TAX CALCULATOR (FY 2024-25)")
    print("=" * 40)

    while True:
        print("\n1. Calculate tax")
        print("2. View history")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            calculate_and_compare()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("Thank you for using the Tax Calculator!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()