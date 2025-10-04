# 7)დაწერეთ ფუნქცია index_of_max(lst), რომელიც აბრუნებს სიაში ყველაზე დიდი რიცხვის ინდექსს.

def index_of_max(lst):
    max_num = lst[0]
    for i in lst:
        if i > max_num:
            max_num = i
    return lst.index(max_num)
print(index_of_max([]))
