def teacher1():
    from dicst import result1
    from dics import result
    try:    
      grade=result1/result>=0.5
      print(f"you pass")
    except ZeroDivisionError:
       print('please enter in final grade number more than zero')
    else:
       print(f"you failed")

teacher1()

