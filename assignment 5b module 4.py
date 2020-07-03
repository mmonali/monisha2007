#!/usr/bin/env python
# coding: utf-8

# In[2]:


#print 1 to 100
for fizzbuzz in range(100):  

    if fizzbuzz % 15 == 0:  
        print("FizzBuzz")                                          
        continue
  
    elif fizzbuzz % 3 == 0:      
        print("Fizz")                                          
        continue
    elif fizzbuzz % 5 == 0:          
        print("Buzz")                                      
        continue
  
    # print numbers 
    print(fizzbuzz) 


# In[3]:


#remove consecutive duplicates from list 
 
x = [1,2,4,7,3,7,8,4,4,9]

previous_value = None
new_lst = []

for elem in x:
   if elem != previous_value:
       new_lst.append(elem)
       previous_value = elem

print(new_lst)


# In[10]:


#find unique element from a list
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)


# In[11]:


#check wheather number is in given range
def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)


# In[12]:


#calculate the number of upper case n lower case letters
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


# In[ ]:




