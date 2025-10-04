# 8)დაწერეთ ფუნქცია total_length(words), რომელიც აბრუნებს სიაში არსებული ყველა სტრინგის სიგრძეების ჯამს.

def total_length(words):
    sum=0
    for i in words:
        sum += len(i)
    return sum
print(total_length([]))