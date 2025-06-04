# 1. შექმენით ფუნქცია, რომელიც მომხმარებლის შემოტანილ სიტყვაში დაითვლის რამდენი განსხვავებული ასოსგან შედგება ეს სიტყვა.

def count(name):
    list_1=''
    Quantity=0
    for i in name:
        list_1.append(i)
        if i not in list_1:
            Quantity += i
    return len(list_1)
print(count('nika'))