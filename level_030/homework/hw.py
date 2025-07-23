# codewars

def logical_calc(array, op):
    arr=array[0]
    for i in array[1:]:
        if op == 'AND':
            arr = arr and i
        elif op == "OR":
            arr = arr or i
        elif op == "XOR":
            arr = arr != i
    return arr

def correct(s):
    final_txt=''
    for i in s:
        if i not in '501':
            final_txt += i
        elif i == '5':
            final_txt += 'S'
        elif i == '0':
            final_txt += 'O'
        elif i == '1':
            final_txt += 'I'
    return final_txt


def count_sheep(n):
    final_txt=''
    for i in range(1, n+1):
        final_txt += str(i) + ' sheep...'
    return final_txt


def reverse_seq(n):
    list=[]
    for i in range(n, 0, -1):
        list.append(i)
    return list
print(reverse_seq(6))


def two_highest(arg1):
      return sorted(set(arg1), reverse=True) [0:2]