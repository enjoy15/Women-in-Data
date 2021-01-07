#!/usr/bin/env python
# coding: utf-8

# # Task 1
# # Write a program that does the following:
# # a) Stores a random number (1-10) in a variable – see hint below

# In[23]:


import random
rand_number = random.randint(0,10)
print(rand_number)


# # b) Asks a user for their name and stores this in a variable.

# In[21]:


myName = input("What is your name?")


# # c) Asks a user to guess the number between 1 and 10

# In[24]:


guess = int(input("Take a guess (number between 1 and 10):"))


# # d) Tells the user whether they have guessed correctly.

# In[37]:


if guess == rand_number:
    print("Good job," + myName + "! You guessed my number")
else:
    print("Wrong, better luck next time")


# In[ ]:




