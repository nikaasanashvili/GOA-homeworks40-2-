# 2. for loop & while loop - ის გამოყენებით მომხმარებლის შემოტანილ სიტყვას გადაუარეთ და გამოიტანეთ თითოეული ასო.


def leters(name):
    name_1=''
    for i in name:
        print(i)

    index=0
    while index <= len(name):
        print(name[index])
        index += 1
print(leters('nika'))
    


