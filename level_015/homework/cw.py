# 1)შექმენი ფუნქცია,რომელსაც გადაეცემა სტრინგი --> aleqsandre , თქვენი დავალებაა დააბრუნოთ კენტ ინდექსზე მდგომი ასოები

def kenti(name):
    final_str=''
    for i in range(len(name)):
        if i % 2 == 0:
            final_str += name[i]
    return final_str
print(kenti('aleqsandre'))