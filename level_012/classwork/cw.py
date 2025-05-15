# 1) შექმენით ფუნქცია, სადაც მოხმარებელს შემოატანინებთ რიცხვს და ამ რიცხვის გამყოფებს დააბრუნებს სიაში.

nam=int(input("enter num: "))



def gamyofebi(namber):

    arr=[]
    for i in range(2, namber):
        if namber % i == 0:
            arr.append(i)       
    return arr
print(gamyofebi(nam))
      