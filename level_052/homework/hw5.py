# 5)დაწერეთ ფუნქცია concat_strings(words), რომელიც იღებს სტრინგების სიას და აბრუნებს
#  ერთ სტრინგად გაერთიანებულ ყველა სიტყვას.

def concat_strings(words):
    txt=''
    for i in words:
        if i != ' ':
            txt += i
    return txt
print(concat_strings())



























