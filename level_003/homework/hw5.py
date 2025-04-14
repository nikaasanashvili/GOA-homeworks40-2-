# 7) მომხმარებელს შემოატანინეთ რიცხვი და დაპრინტე ამ რიცხვის ჩათვლით ყველაფრის ჯამი.

num=int(input("enter num: "))
sum=0

for i in range(0, num+1):
    sum += i

print(sum)
