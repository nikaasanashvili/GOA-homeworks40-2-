# 3)შექმენი ფუნქცია რომელსაც გადაეცემა სტრინგი --> "hidroeleqtrosadguri" ,თქვენი დავალებაა ამოშალოთ ამ სტრინგიდან მხოლოდ ხმოვნები და დააბრუნოთ ეს სტრინგი ხმოვნების გარეშე

def tanxmovnebi(name):
    findal_name=''
    for i in name:
        if i in 'qwrtypsdfghjklzxcvbnm':
            findal_name += i
    return findal_name
print(tanxmovnebi('hidroeleqtrosadguri'))