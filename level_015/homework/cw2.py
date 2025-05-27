# 3)შექმენი ფუნქცია როომელსაც გადაეცემა სტრინგი --> fortoxali,თქვენი დავალებაა დააბრუნოთ თითოეული ასოს ინდექსი სიის სახით (არ გამოიყენოთ len ფუნქცია)


def str_index(name):
    index=0
    index_list=[]
    index_list.append(index)
    for i in name:
        index += 1 
        index_list.append(index)
    index_list.pop(-1)
    return index_list
print(str_index('fortoxali'))