#string data type

""" name = "Md. Amzad Hossain Jacky"
print(f"The data type of name is {type(name)} and the value is {name}") """


#changes the string value to different ways
string_data = "Python is a high level programming language, and it is widely used for web development, data analysis, artificial intelligence, and more."

#uppercase of string
print(f"The uppercase value is {string_data.upper()}")  

#lowercase of string
print(f"The lowercase value is {string_data.lower()}")

#capitalize of string
print(f"The capitalize value is {string_data.capitalize()}")

#title of the sing
print(f"The title value is {string_data.title()}")

#slice of the string 
print(string_data[0:6])
print(string_data[2:6])
print(string_data[2:])
print(string_data[-1:])
print(string_data[-5:])
print(string_data[-5:-2])

#split the string 
#it's actually converted into list
print(f"The split value is {string_data.split(',')}")

#concatenate the string
print(f"The concatenated value is {string_data + ' and it is very powerful!'}")


