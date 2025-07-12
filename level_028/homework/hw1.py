# codewars

def square_sum(numbers):
    sum=0
    for i in numbers:
          sum += i * i
    return sum





def find_average(numbers):
    sum=0
    if numbers == []:
        return 0
    for i in numbers:
            sum += i           
    return sum / len(numbers)



def abbrev_name(name):
    name_1 = name.split(" ")
    return name_1[0][0].upper() +'.'+ name_1[1][0].upper()



def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"