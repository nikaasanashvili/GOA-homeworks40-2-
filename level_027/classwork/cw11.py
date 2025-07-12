# 12)შექმენი სია სადაც გექნება სტრინგები და რიცხვები,რიცხვებიგადაიტანე ახალ სიაში და დაალაგე ზრდის მიხევდით
#  სტრინგებიც ჩაამატე სხვა ახალ სიაში და ეს სტრინგების სია დააალაგეთ ანბანის მიხევდით

list=[10 ,20, 11,'nika', 'saba', 'daviti']
int_list=[]
str_list=[]

for i in list:
    if type(i) == int:
        int_list.append(i)
    elif type(i) == str:
        str_list.append(i)

print(sorted(int_list, reverse= False))
print(sorted(str_list, reverse=True))
