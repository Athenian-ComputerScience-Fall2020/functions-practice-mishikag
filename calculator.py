'''
Collaborators: none
jake shienberg 
'''

def add(x,y):
  return x + y

def subtract(x,y):
  return x-y

def divide(x,y):
  return x/y

def multiply(x,y):
  return x*y

calc_num_one = int(input("enter a number "))
calc_num_two = int(input("enter another number "))

input_one = int(input("enter 1 to add, 2 to subtract, 3 to divide, and 4 to multiply "))

if input_one == 1:
    print(add(calc_num_one,calc_num_two))
elif input_one == 2:
    print(subtract(calc_num_one,calc_num_two))

if input_one == 3:
    print(divide(calc_num_one,calc_num_two))
elif input_one == 4:
    print(multiply(calc_num_one,calc_num_two))
