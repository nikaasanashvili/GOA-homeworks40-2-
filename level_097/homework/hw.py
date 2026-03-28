# codewavrs

# def get_sum(a, b):
#     sum = 0    
#     if a <= b:
#         while a <= b:
#             sum += a
#             a += 1
#     else:
#         while b <= a:
#             sum += b
#             b += 1           
#     return sum


# def reverse(st):
#     lst = st.split()
#     txt=''
#     for i in range(len(lst)-1, -1, -1):
#         txt += lst[i] + ' '
#     return txt[0:-1]


# def remove(s):
#     if s[-1] == "!":
#         return s[0:-1]
#     else:
#         return s

# def well(x):
#     good=0
#     for i in x:
#         if i == 'good':
#             good += 1

#     if good > 2:
#         return 'I smell a series!'
#     elif good > 0 and good <= 2:
#         return 'Publish!'
#     else:
#         return 'Fail!'