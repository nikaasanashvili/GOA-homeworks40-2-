# შექმენით ფუნქცია რომელსაც გადაეცემა სხვადასხვა მონაცემთა ტიპით სავსე სია, თქვენი მიზანია ამ სიიდან მარტო სტრინგ ტიპის მონაცემები დააბრუნოთ ახალ სიაში

def string(list):
    str_list=[]
    for i in list:
        if type(i) == str:
            str_list.append(i)
    return str_list
print(string([]))
