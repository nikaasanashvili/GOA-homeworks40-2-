# 4) მომხმარებელს შემოატანინეთ ტექსტი და ამ ტექსტში დაითვალეთ რიცხვების რაოდენობა.

name=input("enter your name: ")

def raodenoba(nam):
    djt="0123456789"
    count=0
    for i in name:
        if i in djt:
            count += 1
    return count

print(raodenoba(name))