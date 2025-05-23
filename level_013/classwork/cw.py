# 1) შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი სიტყვა და დაითვლის სიგრძეს  len() ფუნქციის გარეშე.

unser=input('enter txt: ')

def LEN(user_txt):
    txt_len=0
    for i in user_txt:
        txt_len += 1
    return txt_len
print(LEN(unser))

