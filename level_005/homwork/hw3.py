# 4)მომხმარებელს შემოატანინე მისი საყვარელი ფერი,თუ საყვარელი ფერი ემთხვევა წითელს ტერმინალში გამოუტანე
#  red is favorite color,თუ შემოტანილი ფერი ემთხვევა ყვითელს დაუპტინტე favorite color is yellow,თუ შემოტანილი ფერი ემთხვევა ლურჯს 
# დაუპრინტე favorite color is blue,ყველა სხვა დანარჩენ შემთხვევაში დაუპტინტე other color

fav_color=input("enter your fav color: ")

if fav_color == "red":
    print("red is favotit colore")
elif fav_color == "yellow":
    print("favorit colore is yellow ")
elif fav_color == "blue":
    print("favorit colore is blue")
else:
    print("other color")
