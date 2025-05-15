# 3) მომხმარებელს შემოატანინეთ რიცხვი და სიის სახით დააბრუნეთ ისეთი რიცხვები რომლებიც არ იყოფა მომხმარებლის შემოტანილ რიცხვზე.

nam=int(input("enter num: "))

def ar_iyofa(namber):
    arr=[]
    for i in range(1, namber):
        if namber % i != 0:
            arr.append(i)       
    return arr
print(ar_iyofa(nam))
      