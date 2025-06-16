# შექმენით ფუნქცია რომელიც შეამოწმებს არგუმენტად გადაცემულ სტრინგში თუ არის რიცხვი.

def user_input(user):
    nambers=''
    for i in user:
        if i in '1234567890':
            nambers += i
    return nambers
print(user_input('nika1'))


