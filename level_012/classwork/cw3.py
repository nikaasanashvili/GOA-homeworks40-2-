# 4) მომხმარებელს შემოატანინეთ ტექსტი და ამ ტექსტში დაითვალეთ რიცხვების რაოდენობა.

name=input("enter your name: ")

def raodenoba(nam):
    namer=["0","1","2","3","4","5","6","7", "8","9"]
    caunt=0
    for i in namer:
        for a in nam:
            if i == a:
                caunt + 1
    return caunt
print(raodenoba(name))