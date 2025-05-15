#   1) მომხმარებელს შეეკითხეთ ორი რიცხვი შემდეგ კი შექმენით ფუნქცია რომელსაც არგუმენტად გადასცემთ ამ ორ რიცხვს ხოლო ფუნქცია დააბრუნებს 
#  ამ ორი რიცხვის ჯამს, ასევე გააკეთე ასეთი 4 ფუნქცია სხვადასხვა მათემატიკური მოქმედებებისთვის, გამოიყენეთ პარამეტრები და არგუმენტად გადაეცით
#  მომხარებლის შემოტანილი რიცხვები


nam1=int(input("enter num 1: "))
nam2=int(input("enter num 2: "))

def gamrevleba(nam1, nam2):
    return nam1 * nam2
print(gamrevleba(nam1, nam2))


def gayofa(nam1, nam2):
    return nam1 % nam2
print(gayofa(nam1, nam2))


def mimateba(nam1, nam2):
    return nam1 + nam2
print(mimateba(nam1, nam2))


def gamokleba(nam1, nam2):
    return nam1 - nam2
print(gamokleba(nam1, nam2))