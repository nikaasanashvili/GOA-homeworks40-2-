# 1)შექმენით ფუნქცია რომელსაც გადაეცემა სახელები,თქვენი დავალებაა ტერმინალში გამოიტანოთ კენტ ინდექსზე მდგომი სახელები და შეინახოთ ახალ სიაში


def kenti_str(name):
    kenti_str=""
    for i in range(0,len(name)+1):
        if i % 2 == 0:
            kenti_str += name[i]
    return kenti_str
print(kenti_str())
