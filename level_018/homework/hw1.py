# 1)შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია,თქვენი დავვალებაა იპოვოთ ამ სიიდან ყველაზე პატარა და ყველაზე დიდი რიცხვები

def max_min(nambers):
    max_namber= nambers[0]
    min_namber= nambers[0]
    for i in nambers:
        if i > max_namber:
            max_namber = i
        elif i < min_namber:
            min_namber = i
    return max_namber, min_namber
print(max_min([2,4,1,5,8,9,3]))