# 2) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის სახელი და ასაკი. შეამოწმეთ თუ ასაკი მეტი არის 18-ზე და მისი სახელი არის თქვენი
#  სახელის ტოლი მაშინ დააბრუნოს თქვენ წარმატებით აიღეთ მართვის მოწმობა. სხვა დანარჩენ შემთხვევაში რომ ჩაიჭრნენ


user_age=input("enter your age: ")
user_name=input("enter your name: ")



def gamocda(user_age1, user_name1):
    if int(user_age1 )>= 18 and user_name1 == 'nika':
        return 'gamocda shaabare'
    else:
        return 'chaiweri'
print(gamocda(user_age, user_name))
