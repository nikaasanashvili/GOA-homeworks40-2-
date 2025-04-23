# 2) მომხმარებელს შემოატანინე პაროლი მანამ სანამ ამ პაროლის მნიშვნელობა არ იქნება 'GOA BEST' და თუ შემოიტანა პაროლი სწორად, დაპრინტე 'ყოჩაღ, პაროლი სწორია'.

passwod='GOA BEST'
user_password=input("enter password: ")


while user_password != passwod:
    print("paroli arasworia")
    user_password=input("enter password: ")

print("yoxhag paroli swria")