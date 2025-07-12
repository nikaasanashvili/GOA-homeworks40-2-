# 11)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგები,შეამოწმე თუ სტრინგის პირველი ასო არის დიდი და მისი სიგრძე ნაკლებია 5 
# ზე ეს სტრინგები ჩაამატრ ახალ სიაში,შემდეგ ამ ახალ სიაში ჩამატებული ელემენტები გაფილტრეთ(sorted) მათი სიგრძის მიხედვით 
# და ეს სია შემოატრიალეთ

def str_len(list):
    final_list=[]
    for i in list:
        if i[0] == i.capitalize() or len(i) < 5:
            final_list.append(i)
    
    return sorted(final_list, key=len, reverse=False)
print(str_len([]))