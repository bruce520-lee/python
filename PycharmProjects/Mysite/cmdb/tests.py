from django.test import TestCase

# Create your tests here.



# print('ha'.center(50,'-'))


# a = int(input('a:'))
# print(a)

# for i in range(10,0,-1):
#     print(i)
#
# print('hello\nhhh')

# list = []
# for i in range(1,10):
#     for j in range(1,10):
#         num = 0
#         num = i * j
#         temp = ('%s'+'*''%s'+'=%s')%(i,j,num)
#         list.append(temp)
#         # print(list)
#         print(temp)
        # h = []
        # h.append((i,j))
    # print(('%s'+'*''%s'+'=%s')%(i,j,num))

# print(h)

# list = []
# for i in range(10):
#     for j in range(10):
#         temp = i * j
#
#         list.append(temp)
#         print(list)

# print('hello','hh')


# for i in range(1,10):
#     for j in range(i,10):
#         print('%d*%d=%d' % (i,j,i*j),end=' ')
#     print(end='\n')



import os

DIR_PATH = os.path.dirname(os.path.dirname(__file__))
print(DIR_PATH)
#
upload_path = os.path.join(DIR_PATH,'upload')
path = os.path.join(upload_path,'ff.txt')
print(path)
# print(os.path.dirname(path))

f = open(path,mode='rb')
f1 = f.readline()
f2 = f1.decode()
print(type(f2),f2)