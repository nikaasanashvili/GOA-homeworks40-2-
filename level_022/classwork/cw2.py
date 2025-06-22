# 2)მომხმარებელს შემოატანინეთ რაიმე რიცხვი,სანამ მომხმარებელი არ შემოიყვანს 10 ზე ნაკლებ რიცხვს გაუმეორეთ რომ 
# თავიდან შემოიტანოს,თან არასწორად შემოყვანილი მნიშნველობები ჩაამატეთ სიაში

user_namber=int(input("enter namber: "))
list=[]

while user_namber > 10:
    list.append(user_namber)
    user_namber=int(input("enter namber: "))