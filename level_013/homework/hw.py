# 1) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა მომხმარებლის შემოტანილი სიტყვა. ხმოვნები სადაც იქნება ! 
# ნიშნით ჩაინაცვლოს და თანხმოვნები *-ით სხვა დანარჩენი სიმბოლო იყოს ისე როგორ იქნება. 

user=input("enter txt:")


def xmovnebi_tanxmovnebi(txt):
    xmovnebi="aeiou"
    tanxmovnebi='bsdfghjklmnpqrstwxvz'
    filtre_txt=''
    for i in txt:
        if i.lower() in xmovnebi:
            filtre_txt += '!'
        elif i.lower() in tanxmovnebi:
            filtre_txt += '*'
        else:
            filtre_txt += i
    return filtre_txt
print(xmovnebi_tanxmovnebi(user))
