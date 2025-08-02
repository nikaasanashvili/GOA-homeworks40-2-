# 1)შექემენით ფუნქცია რომელსაც გადაეცემა რიცხვებიტ სავსე სია,თქვენი დავალებაა ამ სიიდან ამოშალოთ ლუწი რიცხვები
def luwi(list):
    for i in list:
        if i % 2 != 0:
            list.remove(i)
    return list
print(luwi([]))