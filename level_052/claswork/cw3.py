# 1)ფუნქციამ მიიღოს სტრინგი და შეამოწმოს არის თუ არა ის პალინდრომი (წინიდან და უკნიდან ერთნაირად იკითხება).
# # 👉 მაგალითი: "level" → True, "hello" → False

def palindrom(txt):
    return txt == txt[::-1]
print(palindrom("level"))