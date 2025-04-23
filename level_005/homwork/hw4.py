# 5)მომხმარებელს შემოატანინე რიცხვი,for loop ის გამოყენებით 
# გამოიტანე თითოეული რიცხვი ერთიდან ამ რიცხვამდე,იგივე გააკეთეთ While loop-ით

nam=int(input("enter nam: "))
count=1

while nam +1 > count:
    print(count)
    count += 1



nam_1=int(input("enter nam: "))

for i in range(1, nam_1 + 1):
    print(i)