def cel_to_fah(c):
    return (c * 9/5) + 32

def fah_to_cel (f):
    return (f-32) * 5/9 

def cel_to_kel(c):
    return c + 273.15

def kel_to_cel(k):
    return k - 273.15

def fah_to_kel(f):
    return (f - 32) * 5/9 + 273.15

def kel_to_fah (k):
    return (k - 273.15) * 9/5 +32    

print("Temperature Converter\n")
print("1. Celsius to Fahrenheit\n")
print("2. Fahrenheit to Celsius\n")
print("3. Celsius to Kelvin\n")
print("4. Kelvin to Celsius\n")
print("5. Fahrenheit to Kelvin\n")
print("6. Kelvin to Fahrenheit\n")
choice = input("Choice from 1-6: ")
# °C °F K

try:
    if choice == "1":
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C is {cel_to_fah(c):.2f}°F")

    elif choice == "2" :
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F is {fah_to_cel(f):.2f}°C")

    elif choice == "3" :
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C is {cel_to_kel(c):.2f}K")

    elif choice == "4" :
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k}K is {kel_to_cel(k):.2f}°C")

    elif choice == "5" :
        f = float(input("Enter temperature in Fahrenheit: "))
        print(f"{f}°F is {fah_to_kel(f):.2f}K")

    elif choice == "6" :
        k = float(input("Enter temperature in Kelvin: "))
        print(f"{k}K is {kel_to_fah(k):.2f}°F")

    else:
        print("Invalid Choice!")
except ValueError:
    print("Invalid input! Please enter a numeric temperature.")
