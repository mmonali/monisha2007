#!/usr/bin/env python
# coding: utf-8

# In[1]:


#max of 3 numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if (a >= b) and (a >= b):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c

print("The largest number is", largest)


# In[9]:


#reversing a string
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
s =str(input("enter the string:"))
  
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using loops) is : ",end="") 
print (reverse(s)) 


# In[7]:


#checking prime number
num =int(input("enter a number:"))
if num > 1:
   
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
else:
   print(num,"is not a prime number")


# In[18]:


#sum of squares
def sqsum(n) :
   sm = 0
   for i in range(1, n+1) :
      sm = sm + pow(i,2)
   return sm
n = int(input("enter n value:"))
print(sqsum(n))


# In[ ]:


#try,else

