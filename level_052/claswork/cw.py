# 1)დაწერე ფუნქცია, რომელიც მიიღებს რიცხვს და დააბრუნებს მის ციფრებს ზრდადობით დალაგებულს სიაში.
# მაგ: 40251 -> [0,1,2,4,5].

def sort_list(list):
    sorted_list=[]
    for i in str(list):
        if i not in sorted_list:
            sorted_list.append(int(i))
    return set(sorted_list)
print(sort_list(40251))