# 12) მომხმარებელს შემოატანინეთ სტრინგი და for loop-ის საშუალებით შეაბრუნეთ ეს სტრინგი. შემდეგ გაარკვიეთ არის თუ არა პალინდრომე. 
# (for loop-ით შემოატრიალეთ  და პალინდრომე არის ისეთი სიტყვა რომლის საწყისი ვერსიაც ემთვევა შებრუნებულს 

name=input("enter your name: ")
palindrom=""
for i in name:
    palindrom += i
    if palindrom == palindrom [::-1]:
        print(True)

