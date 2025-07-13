# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სხვადასხვა მონაცემთა ტიპები,შენი დავლებაა სიიდან ამოიღო მხოლოდ სტრინგ ტიპის მონაცემები
#  რომლების სიგრძეც არის ნაკლები 5 ზე და იწყება დიდი ასოთი და დაამატო ახალ სიაში,შემდეგ ეს სია დაასორტირე სიგრძის 
# მიხედვით და შემოატრიალეთ

def str_list(list):
    finall_list=[]
    for i in list:
        if type(i) == str and len(i) < 5 and i == i.capitalize():
            finall_list.append(i)
    return sorted(finall_list, key=len, reverse=True)
print(str_list([]))

