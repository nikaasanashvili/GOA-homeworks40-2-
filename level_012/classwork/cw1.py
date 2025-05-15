# 2) შექმენით ფუნქცია, რომესლაც გადაეცემა მომხმარებლის შემოტანილი ტექსტი და დაითვლით ასო 'a'-ს რაოდენობას. 
# (დიდადაც რომ იყოს დაწერილი ისიც რომ ჩაითვალოს). 

name=input("enter your name: ")

def find_a(name1):
    name1 = name1.lower()
    caunt=0
    for i in name1:
        if i == "a":
            caunt += 1
    return caunt
print(find_a(name))
