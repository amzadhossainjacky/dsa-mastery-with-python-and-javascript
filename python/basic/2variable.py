#variable

""" name = "John"
print(name) """

#arithmetic operators
""" x = 2
y = 33
z = x + y
print(z)
 """

#multiple variable assignment
""" x, y, z = "orange", "banana", "Cherry"
print(x, y, z)
 """

#type checking
""" x = 6
print("The type of x is:", type(x))
name = "John"
print("The type of name is:", type(name)) """

#swapping variable values
""" x = 5
y = 10
x, y = y, x
print("After swapping x:", x, "y:", y)
 """

#type casting
x = 5
y = "10"
z = 5 + int(y)
print("The sum of x and y is:", z)


## project 
""" Create a Salary Calculator.

Requirements:

Ask for the employee's name.
Ask for the monthly salary.
Ask for the bonus.
Ask for the tax percentage.
Calculate:
Gross Salary = Salary + Bonus
Tax Amount
Net Salary
Print a salary slip. 

===== Salary Slip =====

Employee: Jacky

Salary : 50000
Bonus  : 5000
Gross  : 55000
Tax    : 5500
Net    : 49500 

"""

#taken inputs from user
employee_name = input("Enter employee's name: ")
monthly_salary = float(input("Enter monthly salary: "))
bonus = float(input("Enter bonus:"))
tax_percentage = float(input("Enter tax percentage: "))

# calculating the gross salary
gross_salary = monthly_salary + bonus
tax_amount = (tax_percentage /100) * gross_salary
net_salary = gross_salary - tax_amount

print("\n ===== Salary Slip =====")
print(f"Employee: name: {employee_name}")
print(f"Salary : {monthly_salary}")
print(f"Bonus : {bonus}")
print(f"Gross : {gross_salary}")
print(f"Tax : {tax_amount}")
print(f"Net : {net_salary}")








