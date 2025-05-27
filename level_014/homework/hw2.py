# 3) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილი რიცხვის ჩათვლით დაგვიბრუნებს გამრავლების ტაბულას.

num=int(input("enter your nam: "))

def gamrevleba(user_num):
    for i in range(1, user_num+1):
        print(i*num)
print(gamrevleba(num))


