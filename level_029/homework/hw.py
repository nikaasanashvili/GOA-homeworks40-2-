#codewars


def positive_sum(arr):
    sum = 0
    for element in arr:
        if element > 0:
            sum += element
    return sum


def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    total_blank_pages = 0
    for i in range(n): 
        total_blank_pages += m
    return total_blank_pages


def count_by(x, n):
    nam= x * n
    list=[]
    for i in range(x, nam+1, x):
        list.append(i)
    return list


    