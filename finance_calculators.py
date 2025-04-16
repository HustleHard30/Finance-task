import math

print(
    "Investment - to calculate the amount of interest you'll earn on your investment\n"
    "Bond - to calculate the amount you'll have to pay on a home loan"
)

# Get user choice with basic error handling
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# === INVESTMENT OPTION ===
if user_choice == "investment":
    print("You chose Investment")

    try:
        principal = float(input("Enter investment amount (R): "))
        interest_rate = float(input("Enter annual interest rate (%): "))
        years = int(input("Enter investment period in years: "))
        interest_type = input("Choose interest type ('simple' or 'compound'): ").lower()

        rate_decimal = interest_rate / 100

        if interest_type == "simple":
            total_return = principal + (principal * rate_decimal * years)
            print(f"Your total return (Simple Interest) is: R{total_return:.2f}")

        elif interest_type == "compound":
            total_return = principal * math.pow((1 + rate_decimal), years)
            print(f"Your total return (Compound Interest) is: R{total_return:.2f}")

        else:
            print("Invalid interest type. Please enter 'simple' or 'compound'.")

    except ValueError:
        print("Invalid input. Please enter numeric values where required.")

# === BOND OPTION ===
elif user_choice == "bond":
    print("You chose Bond")

    try:
        property_value = float(input("Enter current value of the home (R): "))
        annual_rate = float(input("Enter annual interest rate (%): "))
        repayment_months = int(input("Enter repayment period (months): "))

        monthly_rate = (annual_rate / 100) / 12

        monthly_repayment = (monthly_rate * property_value) / (1 - (1 + monthly_rate) ** (-repayment_months))
        print(f"Your monthly bond repayment is: R{monthly_repayment:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values where required.")

# === INVALID OPTION ===
else:
    print("Invalid selection. Please enter either 'investment' or 'bond'.")
