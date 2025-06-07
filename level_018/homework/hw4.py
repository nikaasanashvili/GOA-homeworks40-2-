# 4)1 დან 100 მდე გამოიტანეთ მხოლოდ კენტი რიცხვები,შეასრულეთ while loop / for loop ორივეთი

def kenti():
    for i in range(0, 101, 2):
        print(i)

    namber=0
    while namber != 100:
        namber += 2
        print(namber)
print(kenti())