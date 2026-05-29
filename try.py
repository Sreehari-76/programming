try:
    num = int(input("Enter a number:"))
    print(10/num) 
except ZeroDivisionError:
    print("cannot divcide by zero")
else:
    print("division succesful")
finally:
    print("program error")