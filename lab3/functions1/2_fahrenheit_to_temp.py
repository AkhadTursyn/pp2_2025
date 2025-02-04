def calculator(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = calculator(fahrenheit)
print(f"{fahrenheit}°F = {celsius:.2f}°C")