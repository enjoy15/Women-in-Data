#!/usr/bin/env python
# coding: utf-8

# # Write a program which will ask for two numbers from a user. Then offer a menu to the user giving them a choice of maths operators. Once the user has selected which operator they wish to use, perform the calculation by using a procedure and passing parameters.

# In[4]:


number01 = int(input("Input your first number: "))
number02 = int(input("Input your second number: "))
operation = str(input("Which operation would you like to carry out: (Enter “a” if you want to add “b” if you want to subtract “c” if you want to divide “d” if you want to multiply “e” if you want to exponent the number): "))

def procedure_1(num1,num2,ope):
    number01 = num1
    number02 = num2
    operation = ope
if operation == "a":
    print (number01 + number02)
elif operation == "b":
    print(number01 - number02)
elif operation == "c":
    print(number01 / number02)
elif operation == "d":
    print(number01 * number02) 
elif operation == "e":    
    print(number01 ** number02)    
else:
    print("Please input a-e") 

