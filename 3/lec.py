#args 
#----
# def sum(*args):
#     result=0
#     for number in args:
#      result=result+number
#     return result
# value=sum()  
# print(value)

#kwargs
#------
# def new(**kwargs):
#     if kwargs['grade']>=50:
#         print(f"you pass the course mr/ms {kwargs ['name']}")
#     else:
#         print(f"you did not pass the course mr/ms {kwargs ['name']}")
# new(name='khaled',age=20,grade =60) 
# new(name='moh',age=20,grade =40) 
# new(name='ah',age=20,grade =90) 

#--------------------------------------------------------------------------
#global scope
# name='yehia'
# def outer():
#     name='ali'
#     def inner():
#         print(name)
#     inner() 
# outer()     
# print(name) 

#global +inner+outer
#--------------------
# student={'name':'khaled','grade':20}
# def student_info(std):
#     print(std['name'])

#     def check_info(grade):
#         if grade >=50:
#          print('you passed')
#         else:
#            print('you failed')
#     check_info(std['grade'])

# student_info(student)  
#--------------------------------------------------
#global bayrga3 la7d el 2a5er
#---------------------------
# def outer():
#     global name
#     print(name)
#     name='ali'
#     def inner(): 
#         print(name)
#     inner()
# name='yehia'
# outer()  
#---------------------------
#non local  bayrga3 5twa wa7da gwa el function
#----------------------------------------------
# def outer():
#     name='ali'
#     def inner():
#         nonlocal name
#         print(name)
#     inner()
# name='yehia'
# print(name)
# outer()        
#-----------------------------------
#file
#-----
f1=open('lec03.txt','r')
#read file
#---------
# print(f1.read())
# line1=f1.readline()
#read line
#---------
# print(line1)
# line2=f1.readline()
# print(line2)

#read character
#--------------
# line2=f1.read(2)
# print(line2)
#----------------------
# for line in f1:
#     print(line)
#---------------------
# write
#-------
student={'name':'khaled','grade':20}
# f1=open ('student.txt','w')
# f1.write (f"his name is {student['name']} his grade {student ['grade']}")
# f1.close()
#------------------------------------------------------------------------------
# append
#-------
# student2={'name':'ahmed','grade':20}
# f1=open('student.txt','a')
# f1.write (f"\nhis name is {student2['name']} his grade {student2 ['grade']}")
# f1.close()
#----------------------------------------------------------------------------------
# \n anzel line 
#--------------