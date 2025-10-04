# 3)დაწერეთ ფუნქცია double_numbers(lst), რომელიც აბრუნებს ახალ სიას, სადაც თითოეული ელემენტი ორმაგია.

def double_numbers(lst):
    list=[]
    for i in lst:
        list.append(str(i) * 2)
    return list
print(double_numbers([]))
