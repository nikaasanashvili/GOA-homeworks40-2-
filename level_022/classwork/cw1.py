# 1)შექმენით ფუნქცია რომელიც შეამოწმებს არის თუ არა გადმოცემულ სტრინგში ხმოვნები,თუ არის დააბრუნე ეს ხმოვნები ასევე  დაითვალე 
# რამდენი ხმოვანი იყო მოცემულ სტრინგში

def xmovnebi(txt):
    raodenoba=0
    txt_xmovnebi=''
    for i in txt:
        if i in 'aeiou':
            txt_xmovnebi += i
            raodenoba += 1 
    return raodenoba, txt_xmovnebi
print(xmovnebi())
    

