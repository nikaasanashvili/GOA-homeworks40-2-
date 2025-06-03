# 5) შექმენით ფუნქცია, რომელიც მომხმარებელს შემოატანინებს სახელს სანამ არ შემოიტანს თქვენს სახელს. თან ჩაამატეთ ახალ სიაში.
#  და დააბრუნეთ ეს სია და რამდენი ელემენტისგან შედგება.

def my_name(user_name):
    list=[]
    list.append((user_name))
    while user_name != 'nika':
        user_name=input("enter your name: ")
        list.append(user_name)
    return list , len(list)
print(my_name(input("enter your name: ")))