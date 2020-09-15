'''
Collaborators: 

'''

calc_num_one = int(input("enter a number "))
calc_num_two = int(input("enter another number "))

input_one = int(input("enter 1 to add, 2 to subtract, 3 to divide, and 4 to multiply "))

def add():
  return calc_num_one + calc_num_two

def subtract():
  return calc_num_one - calc_num_two

def divide():
  return calc_num_one / calc_num_two

def multiply():
  return calc_num_one * calc_num_two

output_add = add()
output_sub = subtract()
output_div = divide()
output_mult = multiply()

if input_one == 1:
    print(output_add)
elif input_one == 2:
    print(output_sub)

if input_one == 3:
    print(output_div)
elif input_one == 4:
    print(output_mult)
