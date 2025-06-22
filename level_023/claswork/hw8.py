# 8)შექმენი ფუნქცია რომელსაც გადაეცემა სია,შენი დავალებაა იპოვო ამ სიიდან ლუწი რიცხვები და ჩაამატო ახალ
#  სიაში,შემდეგ ამ სიიდან უნდა გაიგოთ კენტ ინდექსზე მდგომი რიცხვების კვადრატების ჯამი

def kvadratebi(nambers):
    luwi=[]
    for i in nambers:
        if i % 2 == 0:
            luwi.append(i)
    
    sum=0
    for j in range(0, len(luwi)):
        if j % 2 != 0:
            sum += luwi[j] * luwi[j]
    return sum
print(kvadratebi([]))
