# 17)შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგებით სავსე სია,შენი დავალებაა შეამოწმო თუ რამდენი ცალი დიდი ასო ურევია ყველა სტრინგში მთლიანად

def caunt_str(list):
    txt = "".join(list)
    caunt=0
    for i in txt:
        if i == i.upper():
            caunt += 1
    return caunt
print(caunt_str([]))