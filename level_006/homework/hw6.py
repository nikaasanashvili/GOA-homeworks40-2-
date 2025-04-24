# 7)for loop ის გამოყენებით ერთიდან 20 გამოიტანეთ ყველა რიცხვის ჯამი,იგივე შეასრულეთ while loop

sum=0

for i in range(1, 20):
    sum += i
    print(sum)



sum_1=0
sum_2=0

while sum_1 != 20:
    sum_1 += 1
    sum_2 += sum_1
    print(sum_2)
