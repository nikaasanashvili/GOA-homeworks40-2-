# 4)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი,თქვენი დავალებაა ეს სტრინგი შემოატრიალოთ,შემდეგ კი ამ
#  დააბრუნოთ შემოტრიალებული  სტრინგს რომ ქონდეს პირველი ასო დიდი


def list(txt):
    final_list=[]
    for i in txt:
        final_list.append(i[::-1].capitalize())
    return final_list
print(list([]))

    
