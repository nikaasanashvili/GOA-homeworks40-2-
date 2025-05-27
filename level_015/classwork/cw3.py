# 3)შექმენი ფუნქცია როომელსაც გადაეცემა სახელებით სავსე სია,თქვენი დავალებაა დააბრუნოთ თითოეული ელემენტის ინდექსი(არ გამოიყენოთ len ფუნქცია)
list=['nika', 'saba', 'daviti', 'dachi']

def finde_name(name):
    for i in name:
        return name.index('saba')
print(finde_name(list))
