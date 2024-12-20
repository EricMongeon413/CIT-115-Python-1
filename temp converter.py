print("Eric Mongeon's Temp Converter")

flt_temperature = input("Enter a temperature: ")

try:
    flt_temperature = float(flt_temperature)  
except ValueError:
    print("Error: You must enter a numeric value for the temperature.")
    exit()

str_unit = input("Is this temperature in Fahrenheit (F) or Celsius (C)? ").strip()

if str_unit not in ['F', 'f', 'C', 'c']:
    print("You must enter a F or C")
    exit()

if str_unit in ['F', 'f']:
    if flt_temperature > 212:
        print("Error: Temperature can not be > 212F")
    else:
        flt_celsius = (5.0 / 9) * (flt_temperature - 32)
        print(f"The Celsius equivalent is: {flt_celsius:.1f}")
elif str_unit in ['C', 'c']:
    if flt_temperature > 100:
        print("Error: Temperature can not be > 100C")
    else:
        flt_fahrenheit = ((9.0 / 5.0) * flt_temperature) + 32
        print(f"The Fahrenheit equivalent is: {flt_fahrenheit:.1f}")
