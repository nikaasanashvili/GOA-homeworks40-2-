# 3)შექმენი ფუნქცია როომელსაც გადაეცემა სახელებით სავსე სია,თქვენი დავალებაა დააბრუნოთ თითოეული ელემენტის ინდექსი(არ გამოიყენოთ len ფუნქცია)

def list_index(name):
    index=0
    index_list=[]
    index_list.append(index)
    for i in name:
        index += 1 
        index_list.append(index)
    index_list.pop(-1)
    return index_list
print(list_index(['nika','saba','dachi','daviti']))