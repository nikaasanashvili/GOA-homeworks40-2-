# 6)შექმენით ფუნქცია რომელსაც გადაეცემა სია -- >["kaxi" , "ana" ,"Aleqsandre", "ia" , "Giorgi" , "Iamze" , "beqa"],თქვენი დავალებაა შეამოწმოთ 
# თუ ამ სიიდან თითოეული ელემენტი იწყება დიდ ასოზე ანუ არის capitalize() ეს ელემენტები ადაამატოთ ახალ სიაში და დააბრუნოთ ეს ახალი სია
#  სადაც მოთავსებული გვექნება დიდი ასოთი დაწყებული სიტყბვები

def cap(name):
    list=[]
    for i in name:
        if i[0] == i[0].capitalize():
            list.append(i)
    return list
print(cap(["kaxi" , "ana" ,"Aleqsandre", "ia" , "Giorgi" , "Iamze" , "beqa"]))