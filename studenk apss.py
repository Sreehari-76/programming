try:
    mark = int(input("Enter a number"))
    if mark<0 and mark>100:
        raise Exception("vaild mark")
execpt: