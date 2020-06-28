#!/usr/bin/env python
# coding: utf-8

# In[1]:


#numbers frm 0 to 6(excluding 3 n 6)
for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")


# In[2]:


#counting odd or even numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)


# In[3]:


#reversing a word
word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


# In[1]:


#gcd or hcf
def gcd(a,b): 
        
    if (a == 0): 
        return b 
    if (b == 0): 
        return a 
   
    if (a == b): 
        return a 
  
     
    if (a > b): 
        return gcd(a-b, b) 
    return gcd(a, b-a) 
  
 
a = int(input("enter first num:"))
b = int(input("enter second num:"))
if(gcd(a, b)): 
    print('GCD of', a, 'and', b, 'is', gcd(a, b)) 
else: 
    print('not found') 


# In[3]:


#avg of integers
print ("calculate an average of first n natural numbers")
n = 10
average = 0
sum = 0
for num in range(0,n+1,1):
    sum = sum+num;
average = sum / n
print("Average of first ", n, "natural number is: ", average)


# In[4]:


rows = 4
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')

    print("\r")


# In[5]:


#multiplication table

num = int(input("Enter the number: "))

print("Multiplication Table of", num)
for i in range(1, 11):
   print(num,"X",i,"=",num * i)


# In[6]:


#fibonacci series
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a = b
  b = sum
  sum = a + b


# In[7]:


#binary to decimal
def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    print(decimal)     
      
   
if __name__ == '__main__': 
    binaryToDecimal(100) 
    binaryToDecimal(101) 
    binaryToDecimal(1001) 


# In[ ]:




