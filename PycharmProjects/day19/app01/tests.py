from django.test import TestCase

# Create your tests here.
import os

# path = os.path.dirname(__file__)
#
# print(path)



# dict = {'name':'alex','age':23}
# print(dict.keys())
# print(dict.values())
# print(type(dict))
# print(type(dict.items()))
# print(dict.items())
# for k,v in dict.items():
#     print(k,v)
#
# for k in dict:
#     print(k,dict[k])



# class parent(object):
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def info(self):
#         print('His name is %s,he is %s years old,his gender is %s'%(self.name,self.age,self.gender))
#
# class son(parent):
#     def __init__(self,name,age,gender,email,*args):
#         super(son,self).__init__(name,age,gender)
#         self.email = email
#
#     def e_mail(self):
#         print('His email is %s'%self.email)
#
# class grandson(son):
#     def __init__(self,name,age,gender,email,favor):
#         super(self,grandson).__init__(name,age,gender,email)
#
# s = son('alex',23,'man','')
# s.info()
#
# g = grandson('bill',25,'man','11111','')
# g.info()
# g.e_mail()
# list = []
# a = '123456abcd'
# for i in a:
#     list.append(i)
# print(list)
#
# b= str(list)
# print(type(b))
#
# c = ''.join(list)
# print(c)
# print(type(c))
#
# d = '-'.join(a)
# d = d.split('-',3)
# print(type(d))
# print(d)
#
# d = ''.join(d)
# print(d)
#
# e = d.split('-',6)
# print(e)
#
# f = ''.join(e)
# print(f)


# a = 1,
# print(type(a))
# b = list(a)
# print(b)
#
# t = ['%s:%s'%(x,y) for x in range(2) for y in range(3)]
# print(t)


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#         print(fs)
#     return fs
#
# f1 = count()
#
#
# # for i in range():
#
# m = 1
# n = 2
# a = 1 if m > n else 3
# print(a)

# obj = 'file_path'
# Base_DIR = os.path.dirname(os.path.dirname(__file__))
# File_DIR = os.path.join(Base_DIR,obj)
# print(File_DIR+'/file1')


# f = open('file1','r+')
# f.write('hello')
# f1 = f.readline()
# print(f1)

# import random
#
# num = ''
# ver = ''
# for i in range(4):
#     ver = chr(random.randint(65,90))
#     num = num + ver
# print(num)

# a = 3
# b = 4
# y = a if a > b else b
# print(y)

try:
    a = 10/1
except ZeroDivisionError as e:
    print('division by zero')
finally:
    a = 10%2
    print(a)

def foo(age,**kwargs):
    print(age,kwargs)

foo(1,name='alex',gender='man')