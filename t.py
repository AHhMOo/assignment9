fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
    
def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)  
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit:.2f} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
        return celsius
    except ValueError:
        print("Invalid input. Please enter a valid number for Fahrenheit temperature.")
        return None

    finally:
        print("Thank you for using the weather forecast application!")
        
fahrenheit_to_celsius (fahrenheit)