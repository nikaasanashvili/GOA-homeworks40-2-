# 4)შექმენი ფუნქცია რომელსაც გადაეცემა რაიმე რიცხვი,შენი დავალებაა 0 დან ამ რიცხვამდე დაითვალო 3 ის გამოტოვებით FOR LOOP/WHILE LOOP

def caunt(namber):
    for i in range(0, namber, 3):
        print(i)
    
    j=0
    while j < namber:
        print(j)
        j += 3
print(caunt(40))