# 7)მომხმარებელს შემოაყვანინე პაროლი,ასევე შექმენი ცვლადი სადაც შეინახავ შენს პაროლს,შენი დავალებაა გააარკვიო,თუ მომხმარებლის 
# შემოყვანილი პაროლი არ ემთხვევა შენს პატოლს მაშნ თავიდან გუამეორე რომ შემოიყვანოს პაროლი ხელახლა,შემდეგ თუ მომხმარებლის 
# შემოტანილი პაროლი დაემთხვა შენს პაროლს დაუპრინტე რომ CORRECT 

my_paword='nika'
user_pasword=input("enter pasword: ")

while user_pasword != my_paword:
    user_pasword=input("enter pasword: ")
    if user_pasword ==  my_paword:
        print('correct')
        