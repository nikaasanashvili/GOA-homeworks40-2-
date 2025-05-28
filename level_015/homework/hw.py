# 1)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი,შენი დავალებაა ამ სტრინგიდან ამოშალო კენტ იდექსზე მდგომი ასოები და დააბრუნო სტრინგი მათ გარეშე

def kenti(name):
    final_str=''
    for i in range(len(name)):
        if i % 2 == 1:
            final_str += name[i]
    return final_str
print(kenti('aleqsandre'))