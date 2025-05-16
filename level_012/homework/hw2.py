# 2) შექმენით ფუნქცია რომელსაც გადაეცემა სია, ამ სიში უნდა იყოს ყველა ტიპის მონაცემი. დააბრუნეთ ინტეჯეტ ტიპის ელემენტები ახალ სიაში.

list=["nika", 10, 10.5, 'saba']


def String(list):
    String_list=[]
    for i in list:
        if type(i) == int:
            String_list.append(i)
    return String_list
print(String(list))
