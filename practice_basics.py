'''
Created on 2022/01/03
practice 100 basic programming by python

'''

#1
name = 'str1'
name2 = "str2"

print('I am{}. We are{}.'.format(name, name2))
print(f'I am{name}. We are{name2}.')

#2
print('hi\nbye')

#3
print("10進数=%d，16進数=%x，10進浮動小数点=%f" %(16, 16, 16))

#4
print('hello'.upper())
print('WORLD'.lower())

#5
message='hello\nI am a robot'
print(message)
print(message.split('\n'))

#6
messages = message.split('\n')
print(messages)
print(''.join(messages))
print('XXXX'.join(messages))

#7
message = '　　test for deleting blanks　　　'
print(message.strip())

#8
message = 'today is sunny'
print(message.replace('sunny', 'rainy'))

#9
message='the sky is so beautiful'
print(message.find('so'))

#10
x=1
print(type(x))
print(type(str(x)))

x=1.52
print(type(x))
print(x)
print(type(str(x)))
print(str(x))

x=[1,2,3]
print(type(x))
print(x)
print(type(str(x)))
print(str(x))

x = dict(name='john', birth='US')
print(type(x))
print(x)
print(type(str(x)))
print(str(x))

#11
a,b = 'sba', 'gasba'
print(a in b)
a,b = 'xdh', 'xjake'
print(a in b)

#12
numbers=[0,3,8,-4,9,1]
print(numbers[1])
print(numbers[-1])
numbers.append(2)
print(numbers)

#13
numbers.insert(0,5)
print(numbers)
numbers.insert(-1,-3)
print(numbers)

#14
#delete he number itself
print(numbers)
numbers.remove(5)
print(numbers)
numbers.remove(3)
print(numbers)
#delete index
numbers.pop(2)
print(numbers)

#15
numbers = [0,8,-4,9,-3,2]
def isEven(number):
    if number % 2 == 0:
        print(f'This number, {number} is even')
        return True
    else:
        print(f'This number, {number} is odd')
        return False

print(isEven(2))

print(list(filter(isEven, numbers)))

#16
numbers = [0,8,-4,9,-3,2]
print(numbers.index(-4))

#17
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

#18
dictionary = {
    'A': 'apple',
    'B': 'cherry',
    'C': 'kwi',
    'D': 'water',
    'E': 'melon'
}
print(dictionary)
dictionary.pop('A')
print(dictionary)
dictionary.pop('B')
print(dictionary)
dictionary.clear()
print(dictionary)

#19
dictionary = {
    'A': 'apple',
    'B': 'cherry',
    'C': 'kwi',
    'D': 'water',
    'E': 'melon'
}
print(dictionary.keys())
print(dictionary.values())
print('apple' in dictionary.values())
for key, value in dictionary.items():
    print(f'key is {key}, value is {value}')

#20
dictionary = {
    'A': 'apple',
    'B': 'cherry',
    'C': 'kwi',
    'D': 'water',
    'E': 'melon'
}

print(dictionary['C'])
print(dictionary['E'])
# print(dictionary['F'])

print(dictionary.get('C'))
print(dictionary.get('E'))
print(dictionary.get('F'))

#21
num = 6
if num > 0:
    print('plus')
elif num == 0:
    print('zero')
else:
    print('minus')

#22
a = -7
# if (a % 2 == 0) & (a>=0) & (a < 10):
if 0 <= a < 10 and a % 2 == 0:
    print('1桁偶数')
elif a % 2 == 1 and a < 0:
    print('負の奇数')
else:
    print('整数')

#23
names = ['John', 'Kevin', 'Louis']
for name in names:
    print(name)

#24
for i in range(10, 20):
    print(i)

#25
for i in range(10):
    if i == 6:
        print('finish')
        break
    print(i)

#26
for i in range(10):
    if i == 3:
        continue
    print(i)

#27
lasts = ['Smith', 'White', 'Sato']
firsts = ['Amy', 'James', 'Jones']
for last, first in zip(lasts, firsts):
    print (last+first)

#28
lasts = ['Smith', 'White', 'Sato']
for i, last in enumerate(lasts):
    print(f'{i} is {last}')

#29
nums = []
for i in range(5):
    nums.append(i*2)
    print(nums)

numbers = [2*i for i in range(5)]
print(numbers)

#30
num = 0
# if num == 0:
#     print('error')
# ans = 10 / num
# print(ans)
try:
    print(f'ans : {10/num}')
except:
    print('error')

#31
num = 0
try:
    print(f'ans: {10 / num}')
except ZeroDivisionError as e:
    print(e)

#32

def divide(a,b):
    try:
        print(f'ans: {a/b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)

divide(10, 'aaa')

#33
def divide(a,b):
    try:
        print(f'ans: {a/b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    else:
        print('no problem')

divide(10, 3)

#34
def divide(a,b):
    try:
        print(f'ans: {a/b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    finally:
        print('all process finished')

divide(10, 3)
divide(10, 0)
divide(10, 'aaaa')

#35
def divide(a,b):
    try:
        print(f'ans: {a/b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        pass
    finally:
        print('all process finished')

divide(10, 3)
divide(10, 'aaaa')

#36
class Person:
    nationality = 'Japan'

    def say_hello(self):
        print(f'hello, my nationality is {self.nationality}')

person = Person()
print(person.nationality)
person.say_hello()

#37
class Person:
    nationality = 'Japan'

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'hello, my nationality is {self.nationality}')

    def say_my_name(self):
        print(f'my name is {self.name}')

Jennie = Person('Jennie')
print(Jennie.nationality)
print(Jennie.name)
Jennie.say_my_name()

#38
class Person:
    nationality = 'Japan'

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'hello, my nationality is {self.nationality}')

    def say_my_name(self):
        print(f'my name is {self.name}')

class Kid(Person):
    def say_hello(self, age):
        print(f'hello, my name is {self.name}. I am {age} years old.')

kid = Kid('Jane')
print(kid.name)
print(kid.nationality)
kid.say_hello(12)

#39
'''
need review
private, public
'''
class Person:
    __nationality = 'Japan'

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'hello, my nationality is {self.nationality}')

    def __say_my_name(self):
        print(f'my name is {self.name}')

Jennie = Person('Jennie')
#AttributeError: 'Person' object has no attribute '__nationality'
# print(Jennie.__nationality)
print(Jennie.name)
#AttributeError: 'Person' object has no attribute 'say_my_name'
# Jennie.say_my_name()

#40
# file = open(r"C:\Users\XXXXXX\Desktop\sample_python100.txt")
# text = file.read()
# file.close()

# print(text)

#41
# with open(r"C:\Users\XXXXXX\Desktop\sample_python100.txt", 'r') as f:
#     text = f.read()
#     print(text)

#42
import json
# with open(r"C:\Users\XXXXXX\Downloads\sample.json", 'r') as f:
#     data = json.load(f)
# print(data)
# print(data["storename"])

#43
# import os
# for curDir, dirs, files in os.walk('.'):
#     # print(files)
#     # print(dirs)
#     for file in files:
#         print(f'{curDir}/{file}')

#44
# import os
# lists = os.listdir('.')
# print(lists.sort())

#45
# os.path.abspath('')

#46
# os.path.basename('')

#47
# os.path.exists('xyz/')
# os.path.exists('')

#48
# os.path.isdir('xyz/')

#49
# os.path.isfile('')

#50
# print(os.path.join(curDir, file))

#51
# os.mkdir('test_new_dir')

#52
# os.remove('')

#53
# os.rename('before', 'after')

#56
# os.environ['PATH']

#57
# os.system('la -a')
# print(os.popen('ls -a').read())

#58
import numpy as np
a = np.array([1,2,3,4])
print(a)
print(a.shape)

#59
b = np.array([[1,2], [3,4]])
print(b)
print(b.shape)

#60
c = np.zeros(8)
print(c)
print(c.shape)
d = np.zeros((4,3))
print(d)
print(d.shape)
e = np.eye(5)
print(e)
print(e.shape)




















