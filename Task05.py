#!/usr/bin/env python
# coding: utf-8

# # Task 5
# Write a program which will ask for two numbers from a user. Then offer a menu to the user giving them a choice of operator:
# e.g. – Enter “a” if you want to add “b” if you want to subtract
# Include +, -, /, *, **(to the power of) and square. Once the user has selected which operator they wish to use, perform the calculation.

# In[26]:


number01 = int(input("Input your first number: "))


# In[27]:


number02 = int(input("Input your second number: "))


# In[37]:


operation = str(input("Which operation would you like to carry out: (Enter “a” if you want to add “b” if you want to subtract “c” if you want to divide “d” if you want to multiply “e” if you want to exponent the number): "))


# In[38]:


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


# In[ ]:




