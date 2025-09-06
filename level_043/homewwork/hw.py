# codewars

# def solution(number):
#     sum=0
#     if number < 0:
#         return 0
#     else:
#         for i in range(number):
#             if i % 3 == 0 or i % 5 == 0:
#                 sum += i
#     return sum
  
# def is_uppercase(inp):
#     if inp.upper() == inp:
#         return True
#     elif inp.upper() != inp:
#         return False

# def multiply(a, b):
#     return a * b


# def even_or_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     elif number % 2 != 0:
#         return "Odd"




txt='Nia_kaKus_h-Ka'
if '-' in txt or '_':
    list= txt.split('-')
    final_txt = list[0].lower()
    for i in range(1, len(list)):
        final_txt += list[i].capitalize()


print(final_txt)
    