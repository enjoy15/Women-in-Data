#!/usr/bin/env python
# coding: utf-8

# # Task 4
# # A motorbike costs £2000 and loses 10% of its value every year. Using a loop, print the value of the bike every following year until it falls below £1000.

# In[6]:


MotorbikeCost = 2000
year = 1
while MotorbikeCost > 1000:
    MotorbikeCost = MotorbikeCost * 0.9
    year = year + 1
    print ("The value of a motorbike at year " + str(year) + " is: " + str(MotorbikeCost))


# In[ ]:




