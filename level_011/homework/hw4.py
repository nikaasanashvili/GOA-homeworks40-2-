# 4) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა რიცხვი შემდეგ კი მან უნდა დაგვიბრუნოს ეს რიცხვი დადებითია თუ უარყოფითი
nam=int(input("enter num: "))
 
def shedareba(nam):
    if nam > 0:
        return 'dadebitia'
    else:
        return 'uaryofitia'
print(shedareba(nam))
