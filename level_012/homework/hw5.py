# 5) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანილ რიცხვს ორობითი სისტემიდან გადაიყვანს ათობითში. 
# თუ სხვა სისტემით შემოიტანა მაშინ დაწეროს რომ არასწორად არის შემოტანილი რიცხვი.



# def bainar(nam):
#     namer=''

#     while nam > 0:
#         remainder= nam % 2
#         namer = str(remainder) + namer
#         nam = nam // 2
#     return namer
# print(bainar(10))


# 5) შექმენით ფუნქცია სადაც მომხმარებელს შემოატანინებს სიტყვას და მანამ უნდა შემოატანინოთ სანამ არ შემოიტანს “საკმარისია”.
#  ყველა შემოტანილი სიტყვა დაამატეთ ახალ სიაში და ეს სია დააბრუნეთ.

# name=(input("enter srr: "))
# list=[]
# list.append(name)

# # while name != "sakmarisia":
# #     name=(input("enter srr: "))
# #     list.append(name)
# # print(list[:-1])


name=(input("enter srr: "))


def Str(Input):
    
    list=[]
    list.append(Input)

    while Input != 'sakmarisia':
        Input=(input('enter str1: '))
        list.append(Input)
    return list[:-1]
print(Str(name))