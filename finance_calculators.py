import math

print("Investment- to calculate the amount of\
    interest you'll earn on your investment"
      "\nBond- to calculate the amount you'll have to pay on a home loan")

# User input is converted to lowercase
user_choice = input("Enter either 'investment' or 'bond' from\
 the menu above to proceed: ").lower()


# If user inputs 'Investment', data is collected to
# calculate total investment return
if user_choice == "investment":
    print("You chose investment")
    amount_inv = float(input("Enter investment amount: R"))
    interest_rate = float(input("Enter interest rate: "))
    interest_rate_calc = (interest_rate / 100)
    num_of_years = int(input("Enter investment period in years: "))
    interest_type = input("Select between 'simple interest' \
and 'compound interest: ").lower()
    if interest_type == "simple interest":
        total_amount = (amount_inv + (amount_inv * 
                                      interest_rate_calc * num_of_years))
        print(f"Your bond repayment is R{total_amount}")
    elif interest_type == "compound interest":
        total_amount = (amount_inv * math.pow(
            (1 + interest_rate_calc), num_of_years))
        print(f"Your total investment return is R{total_amount}")
    else:
        ("Invalid input. please enter 'simple interest' or\
    'compound interest'")
        
# If user inputs 'bond', data is collected to
# calculate their bond repayment
elif user_choice == "bond":
    print("You chose bond")
      
    house_value = float(input("Enter current value of home: "))
    house_interest = float(input("Enter interest rate: "))
    house_interest_calc = (house_interest / 100)/12
    num_of_months = int(input("Enter repayment period in months: "))
    repayment = ((house_interest_calc * house_value)
                 / (1-(1 + house_interest_calc) ** (- num_of_months)))
    print(f"Your bond repayment is R{repayment}")
    
else:
    print("Invalid input. please enter 'investment' or 'bond'")