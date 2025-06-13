# 6)მომხმარებელს შემოატანინეთ სახელი და WHILE LOOP ის დახმარებით ამ სტრინგიდან გამოიტანეთ ყოველი მეორე ასო,იგივე FOR LOOP ითაც გააკეთეთ

name=input("enter uour name: ")
for i in name:
    print(i)

index=0
while index < len(name):
    print(name[index])
    index += 1
