# 9)შექმენით ფუნქცია,რომელსაც გადაეცემა სტრინგებით სავსე სია,შენი დავალებაა შეამოწმო,თუ სტრინგი შეიცავს კენტი რაოდენობის
#  ასობგერას,მაგ შემთხვევაში ჩაამატეთ ახალ სიაში,ხოლო თ შეიცავს ლუწი რაოდენობის ასობგერას შენი დავალებაა ესენიც ჩაამატო ახალ სიაშ 
# ოღნდ მათ ასოები იყოს დიდი

def kent_luwi(str_list):
    kenti_list=[]
    luwi_list=[]
    for i in str_list:
        if len(i) % 2 != 0:
            kenti_list.append(i)
        elif len(i) % 2 == 0:
            luwi_list.append(i.upper())
    return kenti_list, luwi_list
print(kent_luwi([]))
            
