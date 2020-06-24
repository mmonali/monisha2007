#!/usr/bin/env python
# coding: utf-8

# In[4]:


#area of circle
import math
r = float(input("Enter the radius of the circle: "))
area = math.pi* r * r
print("%.2f" %area)


# In[5]:


#area oof regular polygon
from math import tan, pi
n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)


# In[6]:


#area of segment of circle
def sectorarea():
    pi=22/7
    radius = float(input('Radius of Circle: '))
    angle = float(input('angle measure: '))
    if angle >= 360:
        print("Angle is not possible")
        return
    sur_area = (pi*radius**2) * (angle/360)
    print("Sector Area: ", sur_area)

sectorarea()


# In[9]:


#shuffling list
import random  
l1 = [100,1,2,3,30,40,"hai","hello"]  
print ("The original list is : " + str(l1)) 
for i in range(len(l1)-1, 0, -1): 
    j = random.randint(0, i + 1)  
l1[i], l1[j] = l1[j], l1[i]  
print ("The shuffled list is : " +  str(l1)) 


# In[12]:


#math function
import math
math.sin(60)


# In[13]:


math.cos(pi)


# In[14]:


math.tan(90)


# In[23]:


print(math.degrees(0.8660254037844386))


# In[24]:


print('e^x (using exp() function) is :', math.exp(5)-8)


# In[25]:


math.sqrt(400)


# In[28]:


math.log(1024, 2)


# In[29]:


math.log(1024,10)


# In[30]:


print('Floor value is :', math.floor(23.56))
print('Ceiling value is :', math.ceil(23.56))


# In[ ]:




