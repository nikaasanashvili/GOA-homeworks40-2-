# 3)ფუნქციამ მიიღოს სტრინგი და სია აკონტროლოს: დაუბრუნოს მხოლოდ ის სიტყვები, რომლებიც მეტია 3 სიმბოლოზე.
# 👉 "I love Python and AI" → ["love", "Python"]

def txt_3(txt):
    final_list=[]
    list = txt.split()
    for i in list:
        if len(i) > 3:
            final_list.append(i)
    return final_list
print(txt_3("I love Python and AI"))
    