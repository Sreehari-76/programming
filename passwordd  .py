try:
    pin = (input("Enter ypur pin"))
    if len(pin)!=6:
        raise Exception("weak password")
    print("strong password")
except:
    print("weak password")

