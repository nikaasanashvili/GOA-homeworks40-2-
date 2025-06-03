# 4)შექმენით ფუნქცია რომესლაც გადაეცემათ სტრინგი,თქვენი დავალებაა შეამოწმოთ თუ ამ სტრინგის პირველი ასო იქნება
# uppercase ანუ დიდი მაგ შემთხვევაში დააბრუნეთ True სხვა შემთხვევეაში დააბრუნეთ False

def uper(name):
    if name[0] != name[0].upper():
        return False
    else:
        return True
print(uper('Nika'))