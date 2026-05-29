try:
    mark = int(input("Enter your marks"))
    if mark<0 or mark>100:
        raise Exception("invaild mark")
    print("vaild mark")
except:
    print("invaid mark")

