#!/usr/bin/python
# Filename:test.py

def sayHello():
    print 'Hello World!'  # block belonging to the function


sayHello()  # call the function


def printMax(a, b):
    if a > b:
        print a, 'is maxinum'
    else:
        print b, 'is maxinum'


printMax(2, 6)
x = 86.5
y = 4345.4
printMax(x, y)


def func(x):
    print 'x is', x
    x = 34
    print 'Changed local x to', x


x = 50
func(x)
print x


def func2():
    global x
    print "x is", x
    x = 2
    print "x is changed to 2, right?", x


x = 55
func2()
print "Value of x is", x


def say(message, times=1):
    print message * times


say("Hello\n", 3)


def func3(a, b=5, c=10):
    '''Prints the maximum of two numbers.
    The two values must be integers.'''
    print a, b, c


func3(56)

print func3.__doc__
