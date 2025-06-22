# 5)შექმენით ფუნქცია რომელსაც გადაეცემა სია,ამ სიაში მოთავსებული იქნება როგორც სტრინგები ასევე ინტეჯერები,თქვენი დავალებაა
#  გაიგოთ სოაში მყოფი სტრინგების რაოდენობა და ასევე უნდა გაიგოთ სიაში მყოფი ინტეჯერების ჯამი


def int_str(list):
    caunt_str=0
    sum=0
    caunt_int=0
    for i in list:
        if type(i) ==  int:
            caunt_int += 1
        elif type(i) == str:
            caunt_str += 1
            sum += i
    return sum
print(int_str([]))
