# მომხმარებელს შემოატანინეთ სიტყვა და for / while loop-ების საშუალებით გამოიტანეთ თითოეული ასო

name=input('enter your name: ')
for i in name:
    print(i)


len_nam=0
while len(name) > len_nam:
    print(name[len_nam])
    len_nam += 1