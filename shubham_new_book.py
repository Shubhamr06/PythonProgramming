#!/usr/bin/env python
# coding: utf-8

# ##must do python
# 

# In[1]:


def add(a,b):
    return a+b

add(1,2)


# In[6]:


def max_of_two(a,b):
    if a>b:
        print(a)
    else:
        print(b)


# In[8]:


max_of_two(1,2)


# In[3]:


def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact =fact*n
            n =n-1
        return fact


# In[4]:


fact(0)


# In[38]:


##fact=1 , a=5 > fact 5 ,a =4 , fact =20 , a =3 , fact =60 , a =2 , fact=120 , a =1 


# In[63]:


def simpleI():
    p=int(input('enter p:'))
    print(p)
    r=float(input('enter r:'))
    print(r)
    t=int(input('enter t:'))
    print(t)

    
    SI=(p*r*t)/100
    print('the simple interest is :' ,SI)


# In[64]:


simpleI()


# In[65]:


a='shubham'
b=2
c=3


# In[66]:


print("{}+{}+{}".format(a,b,c)) ##format sting


# In[68]:


print(f"{a}&{c}") ###new method of foramt sting


# In[7]:


def compoundI():
    p=int(input('enter principal amount'))
    print(p)
    r=float(input('enter rate of interest'))
    print(r)
    n=int(input('enter value of n'))
    print(n)
    t=int(input('enter value of t'))
    print(t)
    
    a=p(1+r/n)
    print(int(a))


# In[8]:


compoundI()


# In[11]:


def areac():
    pi=3.14
    r=float(input('enter radius'))
    area=pi*r*r
    return area


# In[13]:


areac()


# ##Python program to find prime no in an interval

# In[39]:


def primeno():
    lower=int(input('please enter first value'))
    upper=int(input('please enter second value'))
    ##becuase +1 will include last value also
    for num in range(lower,upper+1):
        if num>1:
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                print(num)
        
        
        
                


# In[40]:


primeno()


# In[51]:


#check given no is prime or not:
def checkprime():
    n=int(input('enter no to check prime no'))
    if n>1:
        for i in range(2,int((n/2)+1)):
            if(n%i)==0:
                print('not prime no')
                break
        else:
            print('prime no')
    else:
        print('not prime no')


# In[52]:


checkprime()


# In[1]:


1,2,3,4,5,6,


# In[19]:


def table(n):
    a=1
    while(a<11):
        print(a*n)
        a=a+1
        


# In[20]:


table(2)


# #print fibonacci number
#  -a
# 

# In[5]:


def fib():
    first=0
    second=1
    n=int(input('print value of n: '))
    for i in range(n):
        print(first)
        temp=first
        first=second
        second=second+temp
        
    


# In[6]:


#0,1,1,2,3,5,8,13
fib()


# In[7]:


#printing pattren.... 


# In[5]:


def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact =fact*n
            n =n-1
        return fact


# In[6]:


factorial(0)


# In[1]:


def product():
    n=int(input('enter a positive no: '))
    digit =[int(x) for x in str(n)]
    #print(digit)
    product=1
    for i in digit:
        no=i
        #print(i)
        product=product*i
    print('the products of no is : -->',product)


# In[2]:


product()


# In[24]:


def palindrom():
    n=int(input('enter no you want to check palindrome:/n'))
    print(n)
    digit=[int(x) for x in str(n)]
    print(digit)
    chk=digit[::-1]
    print(chk)
    chk2=[str(x) for x in chk]
    print(chk2)
    a_string="".join(chk2)
    print(a_string)
    a_int=int(a_string)
    print(a_int)
    if a_int==n:
        print('palindrome')
    else:
        print('not palindrome')


# In[28]:


palindrom()


# In[9]:


integers = [1, 2, 3]

strings = [str(integer) for integer in integers]


# In[10]:


strings


# In[46]:


def armstrong():
    n=int(input('enter the value :'))
    digit=[int(x) for x in str(n)]
    order=len(digit)
    #print(digit)
    #print(order)
    sum=0
    for i in digit:
        product=pow(i,order)
        sum=sum+product
        i+=i
    if sum==n:
        print(f"{n} is armstrong no")
    else:
        print(f"{n} is not armstong no")


# In[47]:


armstrong()


# #palindrom no

# In[66]:


def palindrome():
    n=int(input('enter the no \n'))
    print(f"{n} is the entered no . \n")
    temp=n
    reverse=0
    while(n>0):
        digit=n%10
        reverse=reverse*10 + digit
        n=n//10
    print(f"{reverse} , is the revesed no \n")
    if temp==reverse:
        print(f"{temp} , is palindrome no \n")
    else:
        print(f"{temp} ,is not a palindrome no \n")
        
        


# In[67]:


palindrome()


# #123%10---->3
# #123*10=1230 +3 ---> 1233
# #123//10---12 # 3 got removed from the no, so next time loop will take 12 for reversing.

# ###palindrom strings

# In[96]:


def palstring():
    string=input('enter string :\n')
    print(f"{string} is the entered string \n")
    tmp=string
    reverse=""
    for i in string:
        reverse=i+reverse
        #print(reverse)
    print(f"{reverse} is the reversed string \n")
    if reverse==tmp:
        print(f"{tmp} is palindrome string \n")
    else:
        print(f"{tmp} is not palindrome string \n")
    


# In[98]:


palstring()


# In[76]:


""+"m"


# ##sum of squares of first n natural no

# In[134]:


def sumsq():
    n=int(input('enter no :\n'))
    sum=0
    for i in range(1,n+1):
        #print(i)
        sum=sum+pow(i,2)
        i=i+1
    print(f"{sum} is the sum of square of given number \n")
        


# In[135]:


sumsq()


# In[136]:


def cubec():
    n=int(input('enter no :\n'))
    sum=0
    for i in range(1,n+1):
        #print(i)
        sum=sum+pow(i,3)
        i=i+1
    print(f"{sum} is the sum of cube of given number \n")


# In[137]:


cubec()


# In[1]:


n=input('enter number')
for i in (n):
    print(i)


# In[ ]:




