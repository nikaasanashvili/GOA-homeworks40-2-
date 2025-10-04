# 2)ფუნქციამ მიიღოს წინადადება (სტრინგი) და დააბრუნოს რამდენი სიტყვაა მასში.
# # 👉 "I love Python programming" → 4

def caunt_txt(txt):
    list = txt.split()
    return len(list)
print(caunt_txt("I love Python programming"))