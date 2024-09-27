# we can write string in four types
'hi'
"hi"
"""hi"""
'''hi'''

# concatination

name = "SAI"
print('Welcome to the class ' + name) 

# concatination with user input

name = input('Enter the name!:\n')
print('Welcome to the class ' + name) 

name = input('Enter the name!:\n')
message="hello "+ name  + ' welcome to the class'
print(message) 


# format (method of string)

name = input(' hello! user Enter the name!:\n')
message='hello {var1}, welcome to the class '.format(var1=name)
print(message) 


# using f function

name = input(' hello! user Enter the name!:\n')
message=f'hello {name}, welcome to the class '
print(message) 







