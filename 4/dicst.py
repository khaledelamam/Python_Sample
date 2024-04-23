try:
 n=input('grade:')
 n=int(n)
 dicst={'name':'khaled','subject':'math','grade':0}
 result1=dicst['grade']=n
 print(result1)
except ValueError:
 print('please enter a valid number')
except TypeError:
 print('please enter right type')