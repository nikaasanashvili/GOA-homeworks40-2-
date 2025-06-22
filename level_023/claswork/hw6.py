# 6)შექმენი ფუნქცია რომელსაც გადაეცემა სია,ამ სიაში მოთავსებული უნდა იყოს როგორც სტრინგები ასევე ინტეჯერები,შენი დავალებაა 
# სიიდან ამოშალო მხოლოდ სტრინგის ტიპის ელემენტები,რაც შეეხება ინტეჯერებს ჩაამატეთ ახალ სიაში


def remove_str(list):
    int_list=[]
    for i in list:
        if type(i) == int:
            int_list.append(i)
        elif type(i) == str:
            list.remove(i)
    return int_list
print(remove_str([]))