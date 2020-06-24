#!/usr/bin/env python
# coding: utf-8

# In[3]:


#comparing two values
a=input("enter first value:")
b=input("enter second value:")
if a==b:
    print("both the values are equal!!")
else:
    print("the values are not equal!!")


# In[4]:


#comparing three values
a=input("enter first value:")
b=input("enter second value:")
c=input("enter third value:")
all = a==b and b==c and c==a
print("all are equal!",all)
any = a==b or b==c or c==a
print("any of three are equal!!",any)


# In[20]:


#comparing to 5
print("Enter first number")
first = int(input())
print("Enter second number")
second = int(input())
c= first+second
if c>5:
    print("sum is greateer")
elif c==5:
    print("they are equal")
else:
    print("sum is smaller")


# In[18]:


#passing marks
pm=35
marks = float(input())
print("Marks is greater than passing marks:", marks>pm)


# In[28]:


#max of three numbers
def biggest(a,b,c):
    if a>b and a>c :
        print("Biggest Number=",a)
    elif b>a and b>c:
        print("Biggest Number=",b)
    elif a==b:
        print("a=b") 
    elif a==c: 
         print("a=c")
    elif b==c:
        print("b=c")
    else:
        print("Biggest Number=",c)    
biggest(2,8,1)


# In[ ]:




