# 16)შექმენი ფუნქცია რომელსაც გადაეცემა რიცხვებით სავსე სია,შენი დავალებაა ახალ სიაში ჩაამატო კენტი რიცხვები,შემდეგ 
# ამ ახალ სიაში მყოფი რიცხვების საშუალო არითმეტიკული გიაგეთ

def kenti(list):
    kenti_list=[]
    sum=0
    for i in list:
        if i % 2 != 0:
            kenti_list.append(i)
            sum += i
    return sum / len(kenti_list)
print(kenti([1,2,3,4,5]))