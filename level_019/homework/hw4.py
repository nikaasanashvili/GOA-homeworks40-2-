# შექმენით ფუნქცია რომელიც მომხმარებლის შემოტანილი რიცხვის ჩათვლით გამოგვიტანს ყველა კენტი რიცხვის კვადრატის ჯამს

def kenti(namber):
    sum=0
    for i in range(0, namber+1):
        if i % 2 != 0:
            sum += i * i
    return sum
print(kenti(10))