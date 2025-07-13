# 4)შექმენი ფუნქცია რომელსაც გადაეცემა სია,შენი დავალებაა შეამოწმო თუ ამ სიაში მყოფი სახელების სიმბოლოები დგანან კენტ 
# ინდექსზე და ასევე არიან lowercase ები,ჩაამატო ერთ მთლიან სიაში ასეთი ასოები

def str_list(list):
    finall_str=[]
    for i in list:
        for j in range(0, len(i)+1):
            if j % 2 != 0 and i[j].lowercase() == i:
                finall_str.append(i[j])
    return finall_str
print(str_list(["Nika", "giorgi", "Ana", "dato"]))