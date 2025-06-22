# 7)შექმენით ფუნქცია რომელიც ამოშლის სიიდან ლუწ ინდექსზე მდგომ ელემენტებს , და კენტ ინდექსზე მდგომ ელემენტებს ჩაამატებს ახალ სიაში

def kent_luwi(list):
    kenti=[]
    for i in range(0, len(list)):
        if i % 2 == 0:
            kenti.append(i)
        elif i % 2 != 0:
            list.remove(i)
    return kenti
print(kent_luwi([]))