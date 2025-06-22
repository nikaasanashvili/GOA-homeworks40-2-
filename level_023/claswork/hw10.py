# 10)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგებით სავსე სია,შენი დავალებაა გაიგო,თუ ეს სიტყვა არის capitalize მაგ შემთხვევაში დაამატა მსსგავსი სტრინგები
#  სხვა სიაში,თუ სიტყვა არის upper დაამატე ეს სტრინგი სხვა ახალ სიაში,და თუ ეს სიტყვა არის lower მაშინ დაამატე ეს სიტყვები სხვა ახალ სიაში,შემდეგ სამივე 
# სიაში მოცემული ელემენტები დააბრუნეთ ოღონდ სტრინგის სახით და თითოეული სტრინგი ერთმანეთსგან დაშორებული იიყოს $ ნიშნით

def txt(list):
    capitalize_list=[]
    upper_list=[]
    lower_list=[]
    for i in list:
        if i == i.capitalize():
            capitalize_list.append(i)
        elif i == i.upper():
            upper_list.append(i)
        elif i == i.lower():
            lower_list.append(i)
    return "$".join(lower_list, upper_list, capitalize_list) 
print(txt([]))