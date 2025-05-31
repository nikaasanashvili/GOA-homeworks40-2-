# 3) შექმენით ფუნქცია რომელსაც გადაეცემა მომხმარებლის შემოტანილი სახელი. იმ შემთხვევაში თუ თქვენი სახელები ემთხვევა ქეის სენსიტიურობის 
# დაიგნორების შემთხვევაშიც, მაშინ დააბრუნოს: გამარჯობა {სახელი}!, სასიამოვნოა თქვენი გაცნობა. სხვა შემთხვევაში გამარჯობა {სახელი}! 

def qeisensitiv(user_name):
    my_name='nika'
    user_name.lower()
    if user_name == my_name:
        return 'gamarjoba ' +(user_name)+ " sasiamovnoa tqveni gacnoba"
    else:
        return 'gamarjoba ' + user_name
print(qeisensitiv(input("enter your name: ")))
