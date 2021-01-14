#!/usr/bin/env python
# coding: utf-8

# # As an extension to the motorbike task that costs £2000 and loses 10% of its value every year. Using a loop, print the value of the bike every following year until it falls below £1000 by using a function and passing in parameters.

# In[25]:



def function_1(MCost):
    MotorbikeCost = MCost
    year = 1
    while MotorbikeCost > 1000:
        MotorbikeCost = MotorbikeCost * 0.9
        year = year + 1 
        output = "The value of a motorbike at year " + str(year) + " is: " + str(MotorbikeCost)
        print(output)
    return output


message = function_1(2000)
print(message)
    

