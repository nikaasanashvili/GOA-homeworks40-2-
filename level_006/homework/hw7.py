# 8)მომხმარებელს შემოატანინე რიცხვი,შენი დავალებაა გაიგო,თუ მომხმ შემოტანილი რიცხვი მეტია 30 ზე დაუპრინტე რომ ზრდასრული ხარ ,
# თუ ასაკი უდრის 30 უთხარი რომ შენ ხარ 30 წლის და თუ ასაკი ნაკლებია 30 უთხარი რომ კარგი ასაკი გაქვს

user_age=int(input("enter your age: "))

if user_age < 30:
    print("kargi asaki gaqvs")
elif user_age > 30:
    print("zrdasruli xar")
else:
    print("30 wlis xar")