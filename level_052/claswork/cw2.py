# 3)დაწერე ფუნქცია, რომელიც მიიღებს სტრინგს და დააბრუნებს ყველაზე გრძელ სიტყვას.
# # მაგ: "I love programming in Python" → "programming".

def longest_txt(txt):
    str_list = txt.split()
    longest_txt = str_list[0]
    for i in str_list:
        if len(i) > len(longest_txt):
            longest_txt = i
    return longest_txt
print(longest_txt("I love programming in Python"))
    