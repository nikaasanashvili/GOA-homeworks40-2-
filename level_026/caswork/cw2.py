# 2)შექმენი ფუნქცია რომელსაც გადაეცემა სია სადაც მოთავსებული იქნება სხვადასხვა მონაცემთა ტიპები,შენი დავალებაა რომ ამ სიიდან ამოიღო ინტეჯერებიდ
#  ა მოათავსო ცალკე ახალ სიაში,ასევე უნდა მაოიღო სტრინგებიც და ცალკე სიაში,შენი დავალებააა ეს ორი სია დაასორტირო,სტრინგების სია დაასორტირე
#  ანბანის მიხედვით და შემოატრიალე,და რიცხვების სია დაასორტირე ზრდადობის მიხედვით

def int_str(list):
    int_list=[]
    str_list=[]
    for i in list:
        if type(i) == int:
            int_list.append(i)
        elif type(i) == str:
            str_list.append(i)

    return sorted(int_list, key=len(int_list), reverse=False), sorted(str_list, key=)
