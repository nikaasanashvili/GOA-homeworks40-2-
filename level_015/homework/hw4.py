# 5)შექმენი ფუნქცია რომელსაც გადაეცემა სია,თქვენი დავალებაა სიიდან ამოშალოთ მხოლოდ ის სიტყვები რომლის სიგრძეც ნაკლებია 5 ზე

def name_len(name):
    final_list=[]
    for i in name:
        if len(i) > 5:
            final_list.append(i)
    return final_list
print(name_len(['nika','saba','daviti','dachi']))