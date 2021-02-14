#this will be a very basic 2 value console calculator
userChoice = input("What would you like to do?\nAdd\nSubtract\nMultiply\nDivide\nModulus\n")
num1 = float(input("Select your first number\n"))
num2 = float(input("Select your second number\n"))
if userChoice == "Add" or userChoice == "add":
  sum = num1 + num2
elif userChoice == "Subtract" or userChoice == "subtract":
  sum = num1 - num2
elif userChoice == "Multiply" or userChoice == "multiply":
  sum = num1 * num2
elif userChoice == "Divide" or userChoice == "divide":
  sum = num1 / num2
elif userChoice == "Modulus" or userChoice == "modulus":
  sum = num1 % num2
else:
  print("Error")

print(round(sum, 2))

