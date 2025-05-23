# 3) შექმენით ფუნქცია, რომელიც მომხმარებლის შემოტანილ float ტიპის მოცანემს გახლიჩავს. შედეგი ასე რომ იყოს :  19.27 => 19 + 0.27 


num=float(input("enter float num: "))

def FLOAT(number):
    num1 = int(number)
    return str(number) + '+' +  str(num1 - num)
print(FLOAT(num))