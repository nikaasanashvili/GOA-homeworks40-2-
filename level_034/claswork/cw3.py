# 4)შექმენით ფუნქცია რომელსაც გადაეცემა სია სადაც მოთავსებული იქნება როგორც სტრინგები ასევე ინტეჯერები,თქვენი დავალებაა
#  სტრინგ ტიპის მონაცემები ჩაამატო ახალ შექმნილ სიაში და დაასორტირო ანბანის მიხედვით,ხოლო ინტეჯერებიც ჩაამატე სხვა 
# ახალ სიაში და ეს საბოლოო სიაც დაასორტირე თან შემოატრიალე

def sorted_list(list):
    str_list=[]
    int_list=[]
    for i in list:
        if type(i) == int:
            int_list.append(i)
        elif type(i) == str:
            str_list.append(i)
    return sorted(str_list, reverse=True), sorted(int_list, reverse=True)
print(sorted([]))