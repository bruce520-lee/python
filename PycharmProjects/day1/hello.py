# print('hello')
# import os
#
# print(os.path.dirname(__file__))
#
# print(os.path.dirname(os.path.dirname(__file__)))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


print(100%3)
L = []
for a in range(1900-1,2020+1,1):
    # print(a)
    if a%4 == 0 and a%100 != 0 or a%400 == 0:
        L.append(a)
print(L)