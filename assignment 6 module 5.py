#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sum all the items in the list
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Sum of elements in given list is :", sum(lst))


# In[2]:


#create a list of empty dictionaries
n = 5
l = [{} for _ in range(n)]
print(l)


# In[3]:


#access dictionary keys element by index
num = {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(num)[0])


# In[4]:


#iterate over dictionaries using for loops
d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key])


# In[5]:


#sum all items in a dictionary
my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values()))


# In[5]:


#concatenate
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)


# In[6]:


#creating a tuple with different data types
tuplex = ("tuple", False, 3.2, 1)
print(tuplex)


# In[7]:


#creating a tuple
tuplex = 5, 10, 15, 20, 25
print(tuplex)
#Create a tuple of one item
tuplex = 5,
print(tuplex)


# In[10]:


#convert a tuple to a string
def convertTuple(tup): 
     str = ''.join(tup) 
     return str
tuple = ('g', 'e', 'e', 'k', 's') 
str = convertTuple(tuple) 
print(str) 


# In[13]:


#slice a tuple
my_tuple = ('a', 'b', 'c', 'd')
print(my_tuple[1])
print(my_tuple[-1])


# In[18]:


#length of the tuple
tuple1, tuple2 = (123, 'xyz', 'zara'), (456, 'abc')
print ("First tuple length : ", len(tuple1))
print ("Second tuple length : ", len(tuple2))


# In[20]:


#convert tuple to dictionary
tuplex = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuplex))


# In[21]:


#reverse a tuple
def Reverse(tuples): 
	new_tup = tuples[::-1] 
	return new_tup 
	
# Driver Code 
tuples = ('z','a','d','f','g','e','e','k') 
print(Reverse(tuples)) 


# In[25]:


#convert list of tuples into a dictionary
# Python code to convert into dictionary 

def Convert(tup, di): 
    for a, b in tup: 
     di.setdefault(a, []).append(b) 
    return di 
 
tups = [("akash", 10), ("gaurav", 12), ("anand", 14), 
("suraj", 20), ("akhil", 25), ("ashish", 30)] 
dictionary = {} 
print (Convert(tups, dictionary)) 


# In[27]:


#convert list to tuple 
def convert(list): 
    return (*list, ) 

list = [1, 2, 3, 4] 
print(convert(list)) 


# In[30]:


#what is dictionary in python????
file_object  = open("assignment6.txt", "r")


# In[ ]:




