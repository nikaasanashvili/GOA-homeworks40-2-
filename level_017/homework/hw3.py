# 4. შექმენით ფუნქცია, რომელსაც გადაეცემა სია, თქვენი დავალებაა გამოიტანოთ ყველაზე დიდი რიცხვი. (max ფუნქცია არ გამოიყენოთ)

def max_namber(namber):
    list_namber= namber[0]
    for i in namber:
        if i > list_namber:
            list_namber = i
    return list_namber

print(max_namber([1,2,3,8,5,]))