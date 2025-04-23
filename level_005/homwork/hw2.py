# 3)შექმენი ორი ცვლადი ერთში შეინახე შენი სახელი მეორეში შენი ასაკი,შენი დავალებაა შეამოწმო,თუ ასაკი მეტია 18ზე ამ შემთხვევის შიგნით უნდა შეამოწმო
#  შემდეგი პირობა,თუ სახელი ემთხვევა შენს სახელს დაუპრინტე we have same names and we are adults,სხვა შემთხვევაში კი დაუპრინტე 
# we dot have same names but we are adults,ბოლოს დავუბრუნდეთ ასაკს და შევამოწმოთ თუ
#  ასაკი ნაკლებია 18ზე დაპრინტეთ we dont have same names and we are not adults
my_name="nika"
my_age="17"

user_name=input("enter your name: ")
user_age=int(input("enter your age: "))

if user_age > 18:
    if user_name == my_age:
        if user_name == my_name:
            