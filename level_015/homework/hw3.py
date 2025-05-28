# 4)შექმენი ფუნქცია რომელიც მომხმარებელს შემოატანინებს რიცხვს და სტრინგს,თქვენი დავლაებაა გამოიტანოთ მომხმარებლის შემოტანილი სტრინგიდან
#  მომხმარებლის შემოტალინ რიცხვზე(ინდექსზე )მდგომი ასო

nam=int(input('enter namber: '))
name=input("enter name: ")

def nam_str(user_namber, user_name):
    return user_name[user_namber]
print(nam_str(nam, name))