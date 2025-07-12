# 25)შექმენი ფუნქცია რომელსაც გადაეცემა რიცხვების სია,შენი დავალებაა გაიგო რიცხვების ჯამი რომლებიც დგანან კენტ ინდექსზე და ასევე არიან 20 ზე ნაკლები
def nambers(list):
    sum=0
    for i in range(0, len(list)):
        if i % 2 != 0 or list[i] < 20:
            sum += list[i]
    return sum
print(nambers([90, 10, 1]))
            