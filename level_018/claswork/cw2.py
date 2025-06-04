# 2)შექმენი ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია,თქვენი დავალებაა იპოვოთ მხოლოდ 50 ზე მეტი ტიცხვების საშუალო არითმეტიკული

def aritmetikuli(namber):
    caunt=0
    for i in namber:
        if i > 50:
            caunt += i
    return caunt // len(namber)
print(aritmetikuli([]))