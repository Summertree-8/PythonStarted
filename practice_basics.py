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
# print(dictionary['F'])
#
print(dictionary.get('F'))





































