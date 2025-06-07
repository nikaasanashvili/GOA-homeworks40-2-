# 5)1 დან 50 მდე გამოიტანეთ მხოლოდ ის რიცხვები რომლებიც იყოფიან 5 ზეც და 3 ზეც,შეასრულეთ while loop / for loop ორივეთი

def gamyofebi():
    for i in range(0,51):
        if i % 5 == 0 and i % 3 == 0:
            print(i)

    namber=0
    while namber != 50:
        namber += 1
        if namber % 5 == 0 and namber % 3 == 0:
            print(namber)
print(gamyofebi())