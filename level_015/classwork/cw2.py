# 3)შექმენი ფუნქცია როომელსაც გადაეცემა სტრინგი --> fortoxali,თქვენი დავალებაა დააბრუნოთ თითოეული ასოს ინდექსი სიის სახით 
# (არ გამოიყენოთ len ფუნქცია)

def fortoxali(fruit):
    list=[]
    for i in fruit:
        list.append(fruit.find(i))
    return(list)
print(fortoxali('fortoxali'))

