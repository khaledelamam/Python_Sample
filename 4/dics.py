try:
 m=input('final_grade:')
 m=int(m)
 dic={'sub':'math','final_grade':0}
 result=dic['final_grade']=m
 print(result)
except ValueError:
 print('please enter a valid number')
except TypeError:
 print('please enter right type') 