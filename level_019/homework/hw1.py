# შექმენით ფუნქცია რომელსაც გადაეცემა სტრინგად დიდი წინადადება. თქვენი მიზანია ეს წინადადება გახლიჩოთ და შეაერთოთ ისევ, ოღონდ ისე
#  რომ თითოეული სიტყვის პირველი ასო იყოს დიდად

    


def split_str(name):
    list=[]
    splited_name = name.split()
    for i in splited_name:
        list.append(i.capitalize())
    return " ".join(list)
print(split_str('nika saba'))