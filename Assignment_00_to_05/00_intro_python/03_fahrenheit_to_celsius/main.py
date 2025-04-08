def fahrenheit_to_celsius():
  fahrenheit = float(input("Enter temperature in Fahrenheit: "))
  celsius = (fahrenheit - 32) * 5/9
  print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius.")

if __name__ == "__main__":
  fahrenheit_to_celsius()