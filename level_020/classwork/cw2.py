# 3)შექმენით ფუნქცია რომელსაც გადაეცემა სახელები,ეს სახელები ზოგი მთლინად უნდა იყოს დიდი ასოებით დაწერილი 
# ზოგი კი პატარა,თქვენი დავალებაა ახალ სიაშ დაამატოთ მხოლოდ დიდი ასოებით დაწერილი სახელები

def big_str(name):
    final_list=[]
    list = name.split()
    for i in list:
        if i == i.upper():
            final_list.append(i)
    return final_list
print(big_str())
