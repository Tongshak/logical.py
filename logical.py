# A simple calculator app
print("""1. Addition
2. subtraction
3. Multiplication
4. Division
""")
print("Enter two numbers to add")
first_number = input("First Number:")
second_number = input("Second Number:")
sum = float(first_number) + float(second_number)
print(f"{first_number} + {second_number} = {sum:.2f}")

print("Enter two numbers to sub")
firstnumber = input("first number:")
secondnumber = input("second number:")
sub = float(firstnumber) - float(secondnumber)
print(f"{firstnumber} - {secondnumber} = {sub:.2f}")

print("Enter two numbers to mul")
firstnumber = input("first number:")
secondnumber = input("second number:")
mul = float(firstnumber) * float(secondnumber)
print(f"{firstnumber} * {secondnumber} = {mul:.2f}")

print("Enter two numbers to div")
firstnumber = input("first number:")
secondnumber = input("second number:")
div = float(firstnumber) % float(secondnumber)
print(f"{firstnumber} % {secondnumber} = {div:.2f}")

print("Enter two numbers to exp")
firstnumber = input("first number:")
secondnumber = input("second number:")
exp = float(firstnumber) ** float(secondnumber)
print(f"{firstnumber} ** {secondnumber} = {exp:.2f}")
              
              
              
