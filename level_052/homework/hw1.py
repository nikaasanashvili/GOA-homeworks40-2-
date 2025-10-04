# 1)რომელიც იღებს რიცხვების სიას და აბრუნებს ახალ სიას, სადაც არ არის განმეორებადი ელემენტები.

def sort_list(list):
    sorted_list=[]
    for i in list:
        if i not in sorted_list:
            sorted_list.append(int(i))
    return set(sorted_list)
print(sort_list([]))