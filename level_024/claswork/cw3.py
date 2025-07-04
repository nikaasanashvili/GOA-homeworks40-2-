# 3)შექმენით ფუნქცია რომელიც გაიგებს სიაში მყოფი ლუწი რიცხვების ჯამს


def sum_luwi(list):
    sum=0
    for i in list:
        if i % 2 == 0:
            sum += i
