# 7)შექმენით ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა იპოვოთ ამ სიაში მხოლოდ ლუწ ინდექსზე მდგომი ელემენტების საშუალო არითმეტიკული

def sashvalo(namber):
    sum=0
    index=0
    for i in range(0, len(namber)+1):
        if i % 2 == 0:
            sum += i
            index += 1
    return sum // index         
print(sashvalo([1,2,3,4,5,6,7,8,9]))



