# 4) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია სადაც იქნება სხვადასხვა ტიპის მონაცემი. გაიგეთ ამ სიაში რიცხვების ჯამი 

list=['str', 'nika', 10, 29, 10.8, 'saba', 10, 15, 11,]

def list_sum(nam):
    sum=0
    for i in nam:
        if type(i) == int:
            sum += i
    return  sum
print(list_sum(list))