def number():
    for i in range(1,6):
        print(i)
number()

def add(x,y):
    print(x+y)
add(22,55)

def multipl(x,y):
    print(x*y)
multipl(3,3)

def square(x):
    print(x*x)
square(6)

def cube(x):
    print(x*x*x)
cube(4)

def even(x):
    if x%2==0:
        print("even")
    else:
        print("odd")
even(2)

def num (x):
    if x > 0:
        print("postive")
    elif x < 0:
        print("negative")
    else:
        print("zero")
num(1)

def largest(x,y):
    if x>y:
         print("x is greater than y")
    else:
         print("x is smaller than y")
largest(57,88)

def prime(x):
    fact = 0
    for i in range(1,x+1):
        if x%i==0:
            fact+=1
    if fact==2:
        print("prime")
    else:
        print("not prime")
prime(2)