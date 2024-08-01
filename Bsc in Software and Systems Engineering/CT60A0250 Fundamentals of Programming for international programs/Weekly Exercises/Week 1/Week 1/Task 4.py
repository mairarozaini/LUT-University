celcius = float(input("Enter temperature in celsius: "))
celcius = round(celcius, ndigits = 1)
fahrenheit = round((9/5) * celcius + 32, ndigits = 1)
print(f"{celcius} degree Celsius is equal to {fahrenheit} degree Fahrenheit.")
