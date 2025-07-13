# 5)შექმენი ფუნქცია რომელსაც გადასცემ სიას,თქვენი დავალებაა ახალ სიაში დაამატოთ ეს სახელები ოღონდ ყველა ასო იყოს დიდი ამ სტრინგებში

def str_list(list):
    final_list=[]
    for i in list:
        final_list.append(i.upper())
    return final_list
print(str_list([]))