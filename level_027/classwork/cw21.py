# 21)დაწერეთ ფუნქცია, რომელიც for ციკლის გამოყენებით ითვლის მასივში რამდენი ელემენტია 10-ზე მეტი.

def mor_then_10(list):
    caunt=0
    for i in list:
        if i > 10:
            caunt += 1
    return caunt
print(mor_then_10([]))