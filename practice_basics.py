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









































