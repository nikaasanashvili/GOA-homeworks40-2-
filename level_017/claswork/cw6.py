# 7)შექმენით ფუნქცია რომელსაც გადაეცემა შემდეგი სია["kaxi" , 5 ,"Aleqsandre", 10, "Giorgi" ,20 , "beqa"]
#  თვენი დავალებაა ამ სიიდან ამოშალოთ მხოლოდ integer ები და დააბრუნოთ სია მათ გარეშე

def Only_int(list):
    final_list=[]
    for i in list:
        if type(i) != int:
            final_list.append(i)
    return final_list
print(Only_int(["kaxi" , 5 ,"Aleqsandre", 10, "Giorgi" ,20 , "beqa"]))
