#!/usr/bin/env python
# coding: utf-8

# In[1]:


#read an entire text of a file
def file_read(file1):
        txt = open(file1)
        print(txt.read())

file_read('file1.txt')


# In[2]:


#read first n lines of a file
a_file = open("file2.txt")
number_of_lines = 3

for i in range(number_of_lines):
    line = a_file.readline()
    print(line)


# In[3]:


#append txt to a file n display txt
def file_read(file3):
        from itertools import islice
        with open(file3, "w") as myfile:
                myfile.write("Python Exercises\n")
                myfile.write("Java Exercises")
        txt = open(file3)
        print(txt.read())
file_read('file3.txt')


# In[4]:


#read last n lines of a file
import sys
import os
def file_read_from_tail(file4,lines):
        bufsize = 8192
        fsize = os.stat(file4).st_size
        iter = 0
        with open(file4) as f:
                if bufsize > fsize:
                        bufsize = fsize-1
                        data = []
                        while True:
                                iter +=1
                                f.seek(fsize-bufsize*iter)
                                data.extend(f.readlines())
                                if len(data) >= lines or f.tell() == 0:
                                        print(''.join(data[-lines:]))
                                        break

file_read_from_tail('file4.txt',2)


# In[5]:


#read a file line by line and store it into a variable
def file_read(file5):
        with open (file5, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('file5.txt')


# In[6]:


#read a file line by line and store it into a list
def file_read(file6):
        with open(file6) as f:     
                content_list = f.readlines()
                print(content_list)

file_read('file6.txt')


# In[7]:


#read a file line by line and store it into a array
def file_read(file7):
        content_array = []
        with open(file7) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_array.append(line)
                print(content_array)

file_read('file7.txt')


# In[8]:


#to count number of lines in a  text file
file = open("file8.txt","r") 
Counter = 0

Content = file.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1
          
print("This is the number of lines in the file") 
print(Counter) 


# In[9]:


#get the file size of a plain file
def file_size(file9):
        import os
        statinfo = os.stat(file9)
        return statinfo.st_size

print("File size in bytes of a plain file: ",file_size("file9.txt"))


# In[11]:


#copy contents of one file to another
with open("bcd.txt") as f:
    with open("nfile.txt", "w") as f1:
        for line in f:
            f1.write(line)


# In[12]:


#sum all the items in a list
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))


# In[13]:


#multiplies all the items in the list
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([1,2,-8]))


# In[14]:


#largest and smallest number from list
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))


# In[15]:


#remove duplicates from the list
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)


# In[16]:


#check list is empty of not
l = []
if not l:
  print("List is empty")


# In[17]:


#clone or copy a list
def Cloning(li1): 
    li_copy = li1[:] 
    return li_copy 
  
li1 = [4, 8, 2, 10, 15, 18] 
li2 = Cloning(li1) 
print("Original List:", li1) 
print("After Cloning:", li2)


# In[18]:


#print specified list after removing the 0th,4th and 5th elements
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)


# In[21]:


#to print numbers of specified list after removing even numbers from it
# list with EVEN and ODD number
list = [11, 22, 33, 44, 55]
print ("Original list:")
print(list)
# which are EVEN (divisible by 2)
for i  in list:
	if(i%2 == 0):
	    list.remove(i)
print("list after removing EVEN numbers:")
print(list)


# In[22]:


#shuffle and print a specified list
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)


# In[1]:


#difference between the two lists
list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
print(total_diff)


# In[ ]:




