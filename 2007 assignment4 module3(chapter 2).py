#!/usr/bin/env python
# coding: utf-8

# In[1]:


#length of a string
str = input("Enter a string: ")
counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)


# In[1]:


#number of characters in string
test_str = "GeeksforGeeks"
   
all_freq = {} 
  
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
  
  
print ("Count of all characters in GeeksforGeeks is :\n "
                                        +  str(all_freq)) 


# In[2]:


#strings
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))


# In[5]:


#upper and lower cases
user_input = input("What's your favourite language? ")
print("My favourite language is ", user_input.upper())
print("My favourite language is ", user_input.lower())


# In[6]:


#substring to string
str1 = 'The quick brown fox jumps over the lazy dog.'
print()
print(str1.count("fox"))
print()


# In[8]:


#converting string to list
def Convert(string): 
    li = list(string.split(" ")) 
    return li 
       
str1 = str(input("enter string:"))
print(Convert(str1)) 


# In[10]:


#deletion of a character
def remove(string, i):  
    a = string[ : i]   
    b = string[i + 1: ]  
    return a + b 
if __name__ == '__main__': 
      
    string = str(input("enter string:")) 
    i = 5
    print(remove(string, i)) 


# In[14]:


#to print every character
a=str(input("enter the string:"))
for i in a:
 print(i)


# In[15]:


#length of string without len function
string=("refrigerator")
count=0
for i in string:
      count=count+1
print("Length of the string is:")
print(count)


# In[ ]:




