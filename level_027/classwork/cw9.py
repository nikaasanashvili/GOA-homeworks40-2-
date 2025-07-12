# 10)შექმენი ფუნქცია სადაც მოთავსებული გექნება სტრინგები,შენი დავალებაა რომ ეს სტრინგები გადაიყვანო ახალ სიაში მაგრამ მათ პირველი 
# ასო იყოს დიდი ახალ სიაში

def big_leter(list):
    final_list=[]
    for i in list:
        final_list.append(i.capitalize())
    return final_list
print(big_leter([]))
