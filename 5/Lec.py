# class cars:
#     def __init__(self,name):
#         self.name=name
#         print(f"{self.name} is car")
# car1=cars('khaled')        
# car2=cars('ahmed')
# ---------------------------------------------
# class member:
#  not_allowed_names = ['Hell','Heck','Shit']
#  user_num=0

#  def __init__(self,first_name,middle_name,last_name,gender):

#   if first_name in  member.not_allowed_names:
#    raise ValueError('name not allowed')
        
#   self.fname=first_name
#   self.mname=middle_name
#   self.lname=last_name
#   self.gender=gender
#   print('a new memeber has been added')
#   member.user_num+=1

# def delete_user(self):
#  member.user_num -=1
#  return f"user{self.fname} deleted"

#   def full_name(self):
#    return f"{self.fname} {self.mname} {self.lname}"
        
    
#   def namewithtitle(self):
#    if self.gender=='male':
#     return f'hello mr . {self.fname}'
        
#   def get_all_info(self):
#    return f"{self.namewithtitle()} , your fullname is {self.full_name()}"

        
# member1=member('khaled','mohamed','abdelaziz','male')
# member2=member('khaled','mohamed','abdelaziz','male')
# member2=member('Hick','Hell','Shit','male')

# print(member1.full_name()) 

# print(member1.namewithtitle())    

# print(member1.get_all_info())   

# print(member1.user_num) 

# print(member2.delete_user())
#-----------------------------------------------------------------------------------------
# inhertance
#------------
class food:
    def __init__(self,name,price):
        self.name=name
        self.price=price
        print('food')
    def eat(self):
        print('eat')
class apple(food):   
    def __init__(self,name,price,amount):
        super(). __init__ (name,price)
        self.amount=amount
        self.price +=10
        print(f'{self.name} ,{self.price} , {self.amount}')

foodtwo=apple('fruit',10,2)

# food_one=food('pizza',20)
# food_one.eat()         
