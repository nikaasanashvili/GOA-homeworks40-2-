# 3)შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ სიას,თქვენი დავალებაა იპოვოთ ამ სიაში მყოფი რიცხვების ჯამი

def sum(num):
    sum1=0
    for i in num:
        sum1 += i
    return sum1
print(sum([10, 5, 3]))