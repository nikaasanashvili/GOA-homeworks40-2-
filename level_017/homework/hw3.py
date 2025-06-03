# 4. შექმენით ფუნქცია, რომელსაც გადაეცემა სია, თქვენი დავალებაა გამოიტანოთ ყველაზე დიდი რიცხვი. (max ფუნქცია არ გამოიყენოთ)

def max_namber(namber):
    for i in namber:
        for j in namber:
            if i > j:
                return i
print(max_namber([1,2,3,4,5,]))