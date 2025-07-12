# 4)შექმენით სია სადაც შეიყვანთ განსხვავებული მონაცემთთა ტიპის ელემენტებს,თქვენი დავალებაა ინტეჯერები ჩაამატო ერთ ახალ სიაშ 
# და სტრინგები ჩაამატო სხვა ახალ სიაში


list=[10,'nika',10.4, 'goa', 11]
int_list=[]
str_list=[]

for i in list:
    if type(i) == str:
        str_list.append(i)
    elif type(i) == int:
        int_list.append(i)
        