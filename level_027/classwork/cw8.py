# 8)შექმენი ფუნქცია სადაც მოათავსებთ სტრინგებს პატარა ასოებით,შენი დავალებაა ახალ სიაში დაამატო ეს სტრინგები მაგრამ ახალ სიაშ ჩაემატნონ დიდი ასოებით

def big_leters(list):
    final_list=[]
    for i in list:
        final_list.append(i.upper())
    return final_list
print(big_leters([]))
