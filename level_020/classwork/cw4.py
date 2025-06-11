# 5)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგებით სავსე სია,თქვენი დავალებაა ახალ სიაში დაამატოთ მხოლოდ ის სტრინგები რომლებიც
#  იწყებიან დიდ ასოზე და ასევე მათ სიგრძე არის 5 ზე ნაკლები და ასევე ამ სტრინგში არის ერთი ასო მაინც ხმოვანი

def str_list(name):
    final_list=[]
    for i in name:
        if i == i.capitalize() or len(i) < 5 or i in 'aeiou':
            final_list.append(i)
    return final_list
print(str_list([]))