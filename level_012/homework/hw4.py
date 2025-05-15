# 4) შექმენით ფუნქცია, სადაც მომხმარებლის შემოტანილ ტექსტს შეაბრუნებთ ისე რომ თითოეულ ასოს შორის - (ტირე) იყოს. (სლაისინგის გარეშე სცადეთ) 
# მაგ: თუ მომხმარებელმა შემოიტანა Goa შედეგი უნდა იყოს a-o-G
name=(input("enter your name: "))

def tire(name1):
    final_name=""
    for i in name1:
        final_name += i
        final_name += "-"
    return final_name
print(tire(name))

