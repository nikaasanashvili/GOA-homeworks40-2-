# 2)შექმენით ფუნქცია რომელსაც გადაეცემა სახელები,ზოგი სახელი უნდა იყოს დაწყებული დიდი ასოთი ზოგი კი ჩვეულებრივ პატარა ასოებით უნდა იყოს
#  დაწყებული,თქვენი დავალებაა ახალ სიაშ დაამატოთ მხოლოდ ის სახაელები რომელთა პირველი ასოც არის დიდი
def big_leters(name):
    final_list=[]
    list = name.split()
    for i in list:
        if i[0] == i.capitalize():
            final_list.append(i)
    return final_list
print(big_leters(''))
    
