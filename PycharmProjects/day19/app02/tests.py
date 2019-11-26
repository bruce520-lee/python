from django.test import TestCase

# Create your tests here.


# dict = {'name':'alex','age':23}

# for k,v in dict.items():
#     print(k,v)

# for k in dict:
#     print(k,dict[k])


# value = dict.get('name')
# print(value)
#
# value1 = dict['name']
# print(value1)

# print(dict.items())


class choose(object):
    def __init__(self,age):
        self.age = age

    def print_age(self):
        print(self)
        print('age is %s'%self.age)
        return self.age

    def foo(self):
        print('hello')

    @classmethod
    def judge(cls):
        print(cls)
        # cls().foo()
        print(cls())
        # if cls.print_age(cls.age) >= 18 and cls.print_age(cls.age) <= 22:
        #     print('expected')
        # else:
        #     print('out of range')

c = choose(21)
c.print_age()
c.judge()