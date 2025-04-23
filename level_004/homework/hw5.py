# 6) მომხმარებელს შემოატანინე რიცხვი და ამ რიცხვის ჩათვლით ყველა რიცხვი შეკრიბე და ეს ჯამი დაპრინტე.

num=int(input("enter num: "))
sum=0
num_1=1

while num_1 <= num:
    num_1 += 1
    sum += num_1

print(sum)