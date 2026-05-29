total = 0 
fail = 0
p = 0
for i in range(1,6):
    mark = int(input("Enter a number"))
    total+=mark
    if mark< 40:
        fail+=1
        print("fail")
    else:
        p += 1
        print("pass ")