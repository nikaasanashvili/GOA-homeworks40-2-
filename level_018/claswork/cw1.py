# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სხვადასხვა მონაცემეებით სავსე სია,თქვენი დავალებაა ახალ სიაში ჩააამატოთ მხოლოდ სტრინგ ტიპის მონაცემები


def str_list(txt):
    list=[]
    for i in txt:
        if type(i) == str:
            list.append(i)
    return list
print(str_list([]))