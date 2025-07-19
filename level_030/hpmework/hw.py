# codewars

# def correct(s):
#     final_txt=''
#     for i in s:
#         if i not in '501':
#             final_txt += i
#         elif i == '5':
#             final_txt += 'S'
#         elif i == '0':
#             final_txt += 'O'
#         elif i == '1':
#             final_txt += 'I'
#     return final_txt


# def count_sheep(n):
#     final_txt=''
#     for i in range(1, n+1):
#         final_txt += str(i) + ' sheep...'
#     return final_txt


# def reverse_seq(n):
#     list=[]
#     for i in range(n, 0, -1):
#         list.append(i)
#     return list
# print(reverse_seq(6))


def two_highest(arg1):
    nam=arg1[0]
    list=[]
    list_1=[]
    for i in arg1:
        if i > nam:
            nam = i
    list.append(nam)
    for j in arg1:
        if j != nam:
            list_1.append(j)
    nam_1=list_1[0]
    for x in list_1:
        if x > nam_1:
            nam_1 = x
    list.append(nam_1)
    return list
print(two_highest([4,6,10,5,13]))