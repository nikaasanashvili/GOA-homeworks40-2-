# 3) შექმენით ფუნქცია რომელსაც გადაეცემა არგუმენტად რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ლუწია ეს რიცხვი თუ კენტი
nam=int(input("enter nam1: "))

def l_k(nam1):
    if nam1 % 2 == 0:
        return "luwia"
    else:
        return "kentia"
print(l_k(nam))