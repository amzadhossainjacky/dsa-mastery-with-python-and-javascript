#type function is used to check the data type of a variable in python
""" age = 29
print (f"The data type of age is:{age} and the type is {type(age)}") """

#different data types in python 
#int, float. complex, bool, str, list, tuple, set, dict

#integer data type
""" num1 = 10
print(f"The data type of num1 is {num1} and the type is {type(num1)}") """

#float data type
""" num2 = 10.3
print(f"The data type of num2 is {num2} and the type is {type(num2)})") """

#complex data type 
""" num3 = 2 + 3j
print(f"The data type of num3 is {num3} and the type is {type(num3)}") """

#boolean data type
""" present = True
print(f"The data type of present is {present} and the type is {type(present)}") """

#string data  type
""" name = "Md. Amzad Hossain Jacky" 
print(f"The data type of name is {name} and the type is {type(name)}") """

#list data type
""" fruits = ["apple", "banana", "cherry"]
print(f"The data type of fruits is {fruits} and the type is {type(fruits)}") """

#another way of create a list
""" skills = list(("Python", "Java", "C++"))
print(f"The data type of skills is {skills} and the type is {type(skills)}") """

#tuple data type
""" numbers = (1,2,5,3,6)
print(f"The data type of numbers is {numbers} and the type is {type(numbers)}") """

#set data type
""" fruits = {"apple", "banana", "cherry"}
print(f"The data type of fruits is {fruits} and the type is {type(fruits)}") """

#dictionary data type
""" person = {
    "name":  "Md. Amzad Hossain Jacky",
    "age": 29,
    "city": "Dhaka",
}
print(f"The data type of person is {person} and the type is {type(person)})")
 """


#project: Build a Student Management System that stores:
""" Student Name
Student ID
Age
GPA
Is Enrolled
Courses (List)
Grades (Tuple)
Clubs (Set)
Student Profile (Dictionary)

Display all the information in a clean, readable format and print the data type of every variable. """

#Give the student information
student_name  = input("Enter the student name: ")
student_id = int(input("Enter the student ID: "))
student_age = int(input("Enter the student age: "))
student_gpa = float(input("Enter the student GPA: "))

