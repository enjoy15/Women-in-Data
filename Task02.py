#!/usr/bin/env python
# coding: utf-8

# # Task02
# # Write a program that asks a user for their favourite number between 1 and 100 and then tells them a joke based on the number. You should use a minimum of 3 jokes.

# In[14]:


guess = int(input("Your favourite number(between 1 and 100):"))


# In[15]:


if guess <= 25:
    print("My daughter received this e-mail from a prospective student prior to the start of the semester: “Dear Professor, I won’t be able to come to any of your classes or meet for any of the tests. Is this a problem?”")
elif guess <= 50:
    print("An exercise for people who are out of shape: Begin with a five-pound potato bag in each hand. Extend your arms straight out from your sides, hold them there for a full minute, and then relax. After a few weeks, move up to ten-pound potato bags. Then try 50-pound potato bags, and eventually try to get to where you can lift a 100-pound potato bag in each hand and hold your arms straight for more than a full minute. Once you feel confident at that level, put a potato in each bag.")
elif guess <= 75:
    print("Scene: With a patient in my medical exam room Me: How old are your kids? Patient: Forty-four and 39 from my wife who passed away, and from my second wife, 15 and 13. Me: That’s quite the age difference! Patient: Well, the older ones didn’t give me any grandkids, so I made my own.")
else:
    print("Helvetica and Times New Roman walk into a bar.“Get out of here!” shouts the bartender. “We don’t serve your type.”")


# In[ ]:




