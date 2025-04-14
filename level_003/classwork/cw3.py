#  მომხმარებელს შემოატანინე ორი სტრინგი და for loop-ით დაითვალე  ორივეში სიმბოლოების რაოდენობა. შემდეგ დაპრინტეთ არის თუ არა ერთმანეთის ტოლი სიმბოლოების რაოდენობა. 
name=input("enter your anme: ")
surname=input("enter your surname: ")
num_count=0
surname_count=0


for i in name:
    num_count = num_count + 1

print(num_count)



    

surname_count=0
for i in surname:
    surname_count = surname_count + 1

print(surname_count)



print(surname_count == num_count)

