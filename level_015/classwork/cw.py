# 1)შექმენი ფუნქცია,რომელსაც გადაეცემა სტრინგი --> aleqsandre , თქვენი დავალებაა დააბრუნოთ კენტ ინდექსზე მდგომი ასოები


def kenti(user_name):
    final_name=''
    for i in range(0, len(user_name)+1):
        if i % 2 != 0:
            final_name += user_name[i]
    return final_name
print(kenti('aleqsandre'))
        

        