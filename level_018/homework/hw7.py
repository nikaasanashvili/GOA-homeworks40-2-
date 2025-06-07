# 7)შექმენით ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა იპოვოთ ამ სიაში მხოლოდ ლუწ ინდექსზე მდგომი ელემენტების საშუალო არითმეტიკული

def sashvalo(namber):
    list=0
    nam=0
    for i in range(0, len(namber)+1):
        if i % 2 == 0:
            list += i
            nam += 1
    return list // nam

          
print(sashvalo([1,2,3,4,5,6,7,8,9]))
