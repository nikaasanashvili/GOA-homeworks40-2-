# 3) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებელის შემოტანილი რიცხვი მნიშნველობად და გაარკვიეთ ამოდის თუ არა ფესვი არ მირცხვიდან.

num=int(input("enter your nam: "))

def fesvi(namber):
    for i in range(0, namber):
        if i * i == namber:
            return i
print(fesvi(num))
