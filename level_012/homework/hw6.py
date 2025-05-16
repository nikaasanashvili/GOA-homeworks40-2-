# Bonus:
# • შექმენით ფუნქცია სადაც მომხმარებლის შემოტანილი რიცხვის გამყოფების ჯამს დაგვიბრუნებს.

nam=int(input("enter your name: "))

def gamyofebi(namber):

    sum=0
    for i in range(1, namber+1):
        if namber % i == 0:
            sum += i     
    return sum
print(gamyofebi(nam))
      