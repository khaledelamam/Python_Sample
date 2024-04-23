# thinking
#---------
# student={'name':'khaled','age':20,'address':'cairo'}
# def function_1(std):
#     global student
#     print('name','age','address')
#     function_2()
#     def function_2():
#         nonlocal std
#         f1=open('std.txt','w')
#         fuction_3()
#         def fuction_3():
#             nonlocal f1
#             f1.write(f"his name is {student['name']} and his age {student['age']} and his address {student['address']}")
#             f1.close
# function_1(student)            

# name='khaled'
# f1=open('std.txt','w')
# f1.write(f"his name is {name} ")
# f1.close()
# student={'name':'khaled','age': 20,'address': 'maadi'}
#_--------------------------------------------------------------------------------------------------------------------------------------
# final result
#-------------
# def outer():
#     def inner1():
#        global student
#        f1=open('std.txt','w')
       
#        def inner2():
#         nonlocal f1
#         f1.write(f"his name is {student['name']} and his age is {student['age']} and his address {student['address']} ")
#         f1.close()
#        inner2()
    
#     inner1()

# student={'name':'ahmed','age': 20,'address': 'maadi'}
# outer()  
#-------------------------------------------------------------------------------------------------------------------------------
# def longest_alphabetical_substring(s):
#     current_substring = s[0]
#     longest_substring = s[0]

#     for char in s[1:]:
#         if char >= current_substring[-1]:
#             current_substring += char
#         else:
#             current_substring = char

#         if len(current_substring) > len(longest_substring):
#             longest_substring = current_substring

#     return longest_substring

# # Example usage:
# input_string = "azcbobobegghakl"
# result = longest_alphabetical_substring(input_string)
# print("Longest alphabetical substring:", result)

 

