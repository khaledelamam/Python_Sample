# #list =muteable  able to change 
l = [1,2,3,4.5,'yehia']
# print(l[0])

# for location
# for i,element in enumerate (l):
#     if element=='yehia':
#         print(i)
# location for one place  
# print(l.index('yehia'))

# for element in l:
#     print(element)

#fpr loop
# for i in range(5):
#     print('yehia')

# for i in range(5):
#     if i ==0:
#         print('i is equal zero')

# x=0
# for element in l:
#     print(x)
#     x=x+1

# x=len(l)
# # print(x)
# for i in range(x):
#     print(i)

#enumerate = sperate list and select loction for it too
# for i,element in enumerate(l):
#     print(i)
#     print(element)
#     print()

#pop = split from the data in the list 
# print(l.pop(1))
# print(l.pop())

#append add data in list 
# l.append('ahmed')
# print(l)

#insert add and the location to put in it 
# l.insert (0,'alaa')
# print (l)

#remove
# l.remove('yehia')
# print (l)

#from list to list 
# l2=['ahmed','omar']
# l.extend(l2)
# print(l)

#check
# print('yehia' in l)

#min ,max
# numbers=[1,2,3,4,5]
# print (min(numbers))
# print(max(numbers))

#input

#name=input()
# print(f"hello {name}")

# l=[]
# x=input("enter the list :")
# x=int(x)
# for i in range(x):
#     l.append(i)

# print(l)

#start from 1 not 0
# l=[]
# x=input("enter the list :")
# x=int(x)
# for i in range(x):
#     l.append(i+1)

# print(l)

# # change data type from input()
# x=input()
# x=int(x)
# result=x+1
# print(x)

# another way to change input() data type
# x=int(input())
# result=x+1
# print(result)

#tuple = immuteable not able to change 
# t=(1,2,3,4,5)
# print(t)

#tuple
t=(1,2,3,4,5)
# print(t[0])
# print(len(t))
# print (1 in t)

# #from tuple to other 
# t2=(6,7)
# result =t+t2
# print(result)

# # count tuple
# for element in t:
#     print(element)

#know data type for anything
# print(type(l))

#dictionary =muteable
# d={'name' : 'khaled','age': 20 }
# print(d.keys())
# print(d.values())
# print(d.items())
# print(len(d))

# #key of anothoer key
# d={'name' : {'age': 20} }
# print(d['name']['age'])
#to change key from dirction 
d={'name':'yehia'}
# d['age']=20
# d['age']=30
# d['name']='amr'
# print(d)

# for key in d.keys():
#     print (key)

# for value in d.values():
#     print (value)

# for item in d.items():
#     print (item)    
# from dictionary to other
# d={'name':'yehia'}
# d2={'age':20}
# d.update (d2)
# print(d)
#clear dictionary
# d.clear()

#delete
# d={'name':'yehia','age':20}
# del(d['age'])
# print(d)

#for ;oop (start ,end ,step)
# for i in range (1,11):
#     print(i)

# for i in range (1,11,2):
#     print(i)

# while loop i don't know how many time i will loop
# day=0
# while day<7:
#     print ('.')
#     day=day+1


# week = True
# day=0
# while week:
#     if day ==0:
#      day=day+1
#      continue
#     if day >7:
#        break 
#     print ('.')
#     day=day+1   

# function
# def kh(name):
#     print('hello')
# kh()    

# def kh(name):
#     print(f'you name is {name}')
# kh(name= 'khaled') 

# def kh(name,age):
#     print(f'you name is {name}')
#     print(f'you age is {age}')
# kh(name= 'khaled',age=20)  


# def kh(name,age):
#     print(f'you name is {name}')
#     print(f'you age is {age}')
#     age=age+10
#     return age
# result=kh(name= 'khaled',age=20)  
# print(result)


# kh(name='mohamed',age=80)