# 6) მომხმარებელს შემოატანინეთ რიცხვი. შემდეგ სიტყვა სანამ არ შემოიტანს 'გაჩერდი!', ეგ ყველაფერი დაამატეთ ახალ სიაში და ამ სიიდან 
# მომხმარებლის შემოტანილი რიცხვი რაც არის, იმაზე მდგომი სიტყვის ჩათვლით გამოიტანეთ ამ სიიდან სიტყვებ

def my_name(user_name, user_namber):
    list=[]
    list.append((user_name))
    while user_name != 'gacherdi':
        user_name=input("enter your name: ")
        list.append(user_name)
    return list[:user_namber:]
print(my_name(input("enter your name: "), int(input('enter nam: '))))
