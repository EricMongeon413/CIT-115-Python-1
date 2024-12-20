def validate_numeric_input(prompt, allow_zero=False, is_percentage=False, goal_check=False):
    while True:
        try:
            str_value = input(prompt)
            
            num_value = float(str_value)
            
            if is_percentage and num_value < 0:
                print("Input must be a positive numeric value")
                continue

            if goal_check and num_value < 0:
                print("Input must be 0 or greater")
                continue
            
            if not allow_zero and num_value <= 0:
                print("Input must be a positive numeric value")
                continue
            
            return num_value
        
        except ValueError:
            print("Input must be a positive numeric value")

def compound_interest_calculator():
    fltDeposit = validate_numeric_input("What is the Original Deposit (positive value):", allow_zero=False)
    
    fltInterestRatePercent = validate_numeric_input("What is the Interest Rate (positive value): ", 
    is_percentage=True)
    
    intNumMonths = int(validate_numeric_input("What is the Number of Months (positve value): ", 
    allow_zero=False))
    
    fltGoal = validate_numeric_input("What is the Goal Amount (can enter 0 but not a negative): ", 
    allow_zero=True,
    goal_check=True)
    
    fltMonthlyInterestRate = (fltInterestRatePercent / 100) / 12
    
    fltCurrentBalance = fltDeposit

    for intMonth in range(1, intNumMonths + 1):
        fltMonthlyInterest = fltCurrentBalance * fltMonthlyInterestRate
        
        fltCurrentBalance += fltMonthlyInterest
        
        print(f"Month {intMonth}: Account Balance is: $ {fltCurrentBalance:,.2f}")
    
    if fltGoal > 0:
        fltCurrentBalance = fltDeposit
        intMonthsToGoal = 0
        
        while fltCurrentBalance < fltGoal:
            fltMonthlyInterest = fltCurrentBalance * fltMonthlyInterestRate
            
            fltCurrentBalance += fltMonthlyInterest
            
            intMonthsToGoal += 1
        
        print(f"It will take: {intMonthsToGoal:,} months to reach the goal of ${fltCurrentBalance:,.2f}")

if __name__ == "__main__":
    compound_interest_calculator()
