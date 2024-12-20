
def get_letter_grade(f_avg):
    if f_avg >= 97.0:
        return "A+"
    elif f_avg >= 94.0:
        return "A"
    elif f_avg >= 90.0:
        return "A-"
    elif f_avg >= 87.0:
        return "B+"
    elif f_avg >= 84.0:
        return "B"
    elif f_avg >= 80.0:
        return "B-"
    elif f_avg >= 77.0:
        return "C+"
    elif f_avg >= 74.0:
        return "C"
    elif f_avg >= 70.0:
        return "C-"
    elif f_avg >= 67.0:
        return "D+"
    elif f_avg >= 64.0:
        return "D"
    elif f_avg >= 60.0:
        return "D-"
    else:
        return "F"

str_name = input("Name of the person that we are calculating the grades for: ")

try:
    i_test1 = int(input("Test 1: "))
    i_test2 = int(input("Test 2: "))
    i_test3 = int(input("Test 3: "))
    i_test4 = int(input("Test 4: "))
except ValueError:
    print("Please enter valid whole numbers for the test scores.")
    exit()

str_drop_lowest = input("Do you wish to drop the lowest grade? Y/N: ").upper()

if str_drop_lowest != 'Y' and str_drop_lowest != 'N':
    print("Enter Y or N to Drop the Lowest Grade.")
    exit()

if i_test1 < 0 or i_test2 < 0 or i_test3 < 0 or i_test4 < 0:
    print("Test scores must be greater than 0.")
    exit()

if str_drop_lowest == 'Y':
    if i_test1 <= i_test2 and i_test1 <= i_test3 and i_test1 <= i_test4:
        f_avg = (i_test2 + i_test3 + i_test4) / 3
    elif i_test2 <= i_test1 and i_test2 <= i_test3 and i_test2 <= i_test4:
        f_avg = (i_test1 + i_test3 + i_test4) / 3
    elif i_test3 <= i_test1 and i_test3 <= i_test2 and i_test3 <= i_test4:
        f_avg = (i_test1 + i_test2 + i_test4) / 3
    else:
        f_avg = (i_test1 + i_test2 + i_test3) / 3
else:
    f_avg = (i_test1 + i_test2 + i_test3 + i_test4) / 4

str_letter_grade = get_letter_grade(f_avg)

print(f"\n{str_name} test average is: {f_avg:.1f}")
print(f"Letter Grade for the test is: {str_letter_grade}")
