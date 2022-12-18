print('Hello World');

"""Multiple variable initialization
    # x y z
"""
x=y=z="I am a string"

print(x)    # I am a string
print(y)    # I am a string
print(z)    # I am a string

print("\n")

"""Unpack a collection
"""
fruits = ['apple', 'mango', 'cherry']

x ,y ,z = fruits

print(x)    # apple
print(y)    # mango
print(z)    # cherry

print("\n")

'''Global Variable
'''
var = "Hi"
def func():
    print(var + " Divye!!")
func()

print('\n')

var = "Hi"
def func():
    var = "Hello"
    print(var + " Divye!!")
func()

print('\n')

var = "Hi"
def func():
    global var
    var = "Hello"
func()
print(var + " Divye!!")

print('\n')
