# შექმენით ფუნქცია რომელიც მომხმარებელს შემოტანილ სიტყვიდან ლიწ ინდექსზე მდგომ სიმბოლოების გაერთიანებას დაგვიბრუნებს

def luwi_str(name):
    final_str=''
    for i in range(0, len(name)+1):
        if i % 2 == 0:
            final_str += name[i]
    return final_str
print(luwi_str())
