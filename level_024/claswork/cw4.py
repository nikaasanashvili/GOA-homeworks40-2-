# 4) შექმენით ფუნქცია რომელსაც გადაეცემა წინადადება,თქვენი დავალებაა ამ წინადადებაში მყოფი სიტყვები წარმოაგგინოთ სიის სახით
# (გამოიყენეთ შესაბამისი ფუნქცია),შემდეგ ამ სიას გადაუარეთ და შეამოწმეთ,თუ ამ სიაშიმოცემულუ სიტყვის სიგრძე ნაკლებიაა 5 ზე,დაპრინტეთ ნაკლებია 5 ზე,
# სხვა შემთხვევაში დაპრინტეთ მეტია 5 ზე


def str_list(txt):
    list=txt.split()
    for i in list:
        if len(i) < 5:
            return 'naklebia 5ze'
        else:
            return 'metia 5ze'
print(str_list())
