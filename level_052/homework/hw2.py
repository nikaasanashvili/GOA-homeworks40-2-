# 2)დაწერეთ ფუნქცია categorize_numbers(lst), რომელიც იღებს რიცხვების სიას და ამოწმებს თუ რიცხვი:

# "positive" – დადებითი რიცხვები

# "negative" – უარყოფითი რიცხვები

# "zero" – ნულების რაოდენობა

def categorize_numbers(lst):
    for i in lst:
        if i > 0:
            print('positive')
        elif i < 0:
            print('negative')
        else:
            print('zero')
print(categorize_numbers([]))