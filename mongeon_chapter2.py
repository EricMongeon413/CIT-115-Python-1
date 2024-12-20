principal = float(input("Enter the starting principal: "))
interest_rate = float(input("Enter the annual interest: ")) / 100
compounding_times = int(input("How many times per year is the interest compounded?: "))
years = int(input("For how many years will the account earn intrest?: "))

future_value = principal * (1 + interest_rate / compounding_times) ** (compounding_times * years)

print(f"At the end of {years} years you will have: ${future_value:.2f}")