# 3) შექმენით ფუნქცია რომელსაც არგუმენტად სია, ამ სიაში უნდა იყოს სხვადასხვა ტიპის მონაცემები და დაითვალოს რამდენი სტრინგ ტიპის მონაცემი არის

list=['nika', 'saba', 'daviti', 10, 15, 6.8, ]

def count_str(list1):
    count=0
    for i in list1:
        if type(i) == str:
            count += 1
    return count
print(count_str(list))