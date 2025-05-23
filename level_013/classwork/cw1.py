# 2) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი სიტყვა და ამ სიტყვაში დაითვლის ასო "k'ს რაოდენობას. 
# დააიგნოროს ქეის სენსიტიურობა.

name=input("enter your name: ")

def find_k(user_name):
    user_name.lower()
    k=0
    for i in user_name:
        if i == 'k':
            k += 1
    return k
print(find_k(name))