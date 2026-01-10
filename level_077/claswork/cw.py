# codewars

# def disemvowel(string_):
#     final_string=''
#     for i in string_:
#         if i.lower() not in 'aeiou':
#             final_string += i
#     return final_string


# def move_zeros(lst):
#     list=[]
#     list_0=[]
#     for i in lst:
#         if i != 0:
#             list.append(i)
#         elif i == 0:
#             list_0.append(i)
#     return list + list_0


# def spin_words(sentence):
#     words = sentence.split()
#     final_str = []
#     for i in words:
#         if len(i) > 4:
#             final_str.append(i[::-1])
#         else:
#             final_str.append(i)

#     return ' '.join(final_str)

# def twice_as_old(dad_years_old, son_years_old):
#     return abs(dad_years_old - (son_years_old + son_years_old))