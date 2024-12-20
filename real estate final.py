def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            
            if value <= 0:
                print("Input a number that is greater than 0.")
                continue
            
            return value
        
        except ValueError:
            print("Input a number that is greater than 0.")

def getMedian(sales_list):
    list_length = len(sales_list)
    if list_length == 0:
        return 0
    
    if list_length % 2 != 0:
        return sales_list[list_length // 2]
    
    else:
        mid_right = list_length // 2
        mid_left = mid_right - 1
        return (sales_list[mid_left] + sales_list[mid_right]) / 2

def main():
    sales_list = []
    
    while True:
        sales_price = getFloatInput("Enter property sales value: ")
        sales_list.append(sales_price)
        
        while True:
            continue_input = input("Enter another value Y or N: ").strip().upper()
            
            if continue_input == 'Y':
                break
            elif continue_input == 'N':
                break
        
        if continue_input == 'N':
            break
    
    sales_list.sort()
    
    print ()
    for i, sale in enumerate(sales_list, start=1):
        print(f"Property {i}: ${sale:,.2f}")
    
    min_value = min(sales_list)
    max_value = max(sales_list)
    total_value = sum(sales_list)
    avg_value = total_value / len(sales_list)
    median_value = getMedian(sales_list)
    commission = total_value * 0.03
    
    print(f"Minimum: ${min_value:,.2f}")
    print(f"Maximum: ${max_value:,.2f}")
    print(f"Total: ${total_value:,.2f}")
    print(f"Average: ${avg_value:,.2f}")
    print(f"Median: ${median_value:,.2f}")
    print(f"Commission: ${commission:,.2f}")

if __name__ == "__main__":
    main()