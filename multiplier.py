'''
Adapt the code from one of the functions above to create a new function called 'multiplier'.
The user should be able to input two numbers that are stored in variables.
The function should multiply the two variables together and return the result to a variable in the main program.
The main program should output the variable containing the result returned from the function.
'''

input_one= int(input("enter a number "))
input_two= int(input("enter another number "))

def multiplier():
  return input_one * input_two

output_num = multiplier()
print(output_num)
