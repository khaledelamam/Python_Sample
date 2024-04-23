# x='hello khaled'
# y=x.count('e')
# z=x.count('a')
# c=x.count('o')
# print(y+z+c)

# l=[5,0,9,8,3]
# l.sort()
# print(l)

# l=[5,0,9,8,3]
# l.reverse()
# print(l)

# x='iti in the iti'
# y=x.count('iti')
# print(y)

# name='nour'
# y=name.replace('o','')
# z=name.replace('u','')
# print(y)
# print(z)

# x='hi'
# y=x.find('i')
# print(y)
def m_p (height):
    for i in range(1, height + 1):
        space = " " * (height - i)
        blocks = "*" * (2 * i - 1)
        print(space+blocks)