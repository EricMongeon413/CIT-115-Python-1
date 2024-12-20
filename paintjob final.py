import math

def getFloatInput(strPrompt):

    while True:
        try:
            fValue = float(input(strPrompt))
            if fValue <= 0:
                print("Error: Value must be positive and non-zero.")
                continue
            return fValue
        except ValueError:
            print("Error: Please enter a valid numeric value.")

def getGallonsOfPaint(fWallSquareFeet, fFeetPerGallon):

    return math.ceil(fWallSquareFeet / fFeetPerGallon)

def getLaborHours(fLaborHoursPerGallon, iGallons):

    return fLaborHoursPerGallon * iGallons

def getLaborCost(fLaborHours, fLaborChargePerHour):

    return fLaborHours * fLaborChargePerHour

def getPaintCost(iGallons, fPaintPrice):

    return iGallons * fPaintPrice

def getSalesTax(strState):

    strState = strState.upper()
    tax_rates = {
        'CT': 0.06,
        'MA': 0.0625,
        'ME': 0.085,
        'NH': 0.0,
        'RI': 0.07,
        'VT': 0.06
    }
    return tax_rates.get(strState, 0)

def showCostEstimate(iGallons, 
                     fLaborHours, fPaintCost, fLaborCost, fSalesTax):
    # Calculate total costs
    fSubtotal = fPaintCost + fLaborCost
    fTaxAmount = fSubtotal * fSalesTax
    fTotalCost = fSubtotal + fTaxAmount

    # Create output strings
    output_lines = [
        f"Gallons of paint: {iGallons}",
        f"Hours of labor: {fLaborHours:.2f}",
        f"Paint charges: ${fPaintCost:.2f}",
        f"Labor charges: ${fLaborCost:.2f}",
        f"Tax: ${fTaxAmount:.2f}",
        f"Total Cost: ${fTotalCost:.2f}"
    ]

    # Print to screen
    for line in output_lines:
        print(line)

    # Write to file
    strFileName = f"{strCustomerLastName}_PaintJobOutput.txt"
    with open(strFileName, 'w') as file:
        file.write("\n".join(output_lines))

    print(f"\nFile {strFileName} was created.")

def main():
    # Input variables
    fWallSquareFeet = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter paint price per gallon: ")
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    fLaborChargePerHour = getFloatInput("Labor charge per hour: ")

    # Get state and customer name
    strState = input("State job is in: ")
    strCustomerLastName = input("Customer's Last name: ")

    # Calculations
    iGallons = getGallonsOfPaint(fWallSquareFeet, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iGallons)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iGallons, fPaintPrice)
    fSalesTax = getSalesTax(strState)

    # Display cost estimate
    showCostEstimate(iGallons, fLaborHours, fPaintCost, 
                     fLaborCost, fSalesTax)

if __name__ == "__main__":
    main()