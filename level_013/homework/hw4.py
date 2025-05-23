# BONUS: შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილ რიცხვის ჩათვლით გამოგვიტანს ყველა მარტივი რიცხვის ნამრავლს.
number=int(input('enter nuber: '))
def numbers(user):
    my_arr=[]
    for i in range(1, user+1):
        for a in range(2, i):
            if i % a == 0:
                break
            else:
                my_arr.append(i)
    sum=1
    for i in my_arr:
        sum *= i
    return sum
print(numbers(number))