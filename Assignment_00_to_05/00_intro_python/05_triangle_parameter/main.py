def triangle_parameter():
  side1 = float(input("Enter the length of the first side: "))
  side2 = float(input("Enter the length of the second side: "))
  side3 = float(input("Enter the length of the third side: " ))

  print("The perimeter of the triangle is " + str(side1 + side2 + side3))

if __name__ == "__main__":
  triangle_parameter()