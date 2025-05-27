# 2)შექმენი ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია,თქვენი დავალებაა დააბრუნოთ ახალი სია სადაც გექნებათ მხოლოდ ლუწი რიცხვები

list=[10, 5, 2, 7, 8, 4, 5, 11, 10]

def luwi(num):
    luwi_list=[]
    for i in num:
        if i % 2 == 0:
            luwi_list.append(i)
    return luwi_list
print(luwi(list))