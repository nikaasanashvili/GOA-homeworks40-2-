# 1) შექმენით ფუნქცია რომელსაც გადაეცემა მომხმარებლის შემოტანილი რიცხვი. დააბრუნეთ ამ რიცხვის ჩათვლით ყველა ლუწი რიცხვის საშუალო არითმეტიკული


def sashvalo(namber):
    sum=0
    index=0
    for i in range(0, namber+1):
        if i % 2 == 0:
            sum += i
            index += 1
    return sum // index         
print(sashvalo(int(input("enter your namber: "))))



