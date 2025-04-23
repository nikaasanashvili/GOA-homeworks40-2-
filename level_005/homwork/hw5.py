# 6)მომხმარებელს შემოატანინე ათზე მაღალი რიცხვი,for loop ის გამოყენებით იპოვეთ 5 დან მომხმარებლის შემოტანილ რიცხვამდე ყველა
#  რიცხვის ჯამი,იგივე გააკეთეთ while loop ითაც

num=int(input("enter num: "))

while num < 10:
    num=int(input("The num must be greater than 10: "))

sum=0

for i in range(5, num+1):
    sum += i
print(sum)







number=int(input("enter num: "))

while number < 10:
    number=int(input("The num must be greater than 10: "))

sum_1=5
sum_2=0

while number > 5:
    number += -1
    sum_1 += 1
    sum_2 += sum_1

print(sum_2)