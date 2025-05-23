# 4) შექმენით ფუნქცია რომელიც მომხმარებელს შემოატანინებს სიტყვას მანამ სანამ არ შემოიტანს 'საკმარისია'ს. ეს შემოტანილი სიტყვები დაამატეთ სიაში
#  და გაფილტრეთ. სიაში უნდა იყოს ისეთი სიტყვები რომლის სიგრძეც არ აღემატება 5-ს და ურევია რიცხვები.

def sakmarisia():
    list=[]
    while True:
        user_txt=input("enter txt: ")
        if user_txt == 'sakmarisia':
            break
        else:
            list.append(user_txt)
    
    final_list=[]
    for i in list:
        if len(i) < 5:
            for j in i:
                if j in '0123456789':
                    final_list.append(i)
    return final_list
print(sakmarisia())