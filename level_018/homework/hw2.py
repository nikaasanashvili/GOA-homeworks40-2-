# 2)შექმენით ფუნქცია,რომელსაც გადაეცემა სტრინგებით სავსე სია,რომელი სტრინგის სიგრძეც მეტია 6 ზე დააბრუნეთ ეს სტრინგები ოღონდ შემოტრიალებული და პირველი ასო ქონდეთ დიდი(CAPITALIZE)

def nam(list):
    name_list=[]
    for i in list:
        if len(i) > 6:
            name_list.append(i[::])
    return name_list
print(nam(['nika', 'saba', 'davitii', 'dachi']))