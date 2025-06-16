# შექმენით ფუნქცია რომელიც შეამოწმებს არის თუ არა არგუმენტად გადაცემულ სტრინგში ერთი დიდი ასო მაინც

def big_leter(name):
    for i in name:
        if i == i.upper():
            return True
print(big_leter())