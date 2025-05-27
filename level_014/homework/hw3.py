# 4) შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ სტრინგს დაფარავს *-ით

user=input('emter txt: ')

def fifqi(user_txt):
    filter_txt=''
    for i in user_txt:
        filter_txt += '*'
    return filter_txt
print(fifqi(user))
