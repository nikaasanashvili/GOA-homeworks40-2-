# 2)ფუნქცია, რომელიც მიიღებს რიცხვს და დააბრუნებს "ლუწია" თუ ყველა ციფრი ლუწია, "კენტია"
#  თუ ყველა კენტია, ხოლო "შერეულია" თუ ორივე გვხვდება.


def luwi_kenti(nam):
    even = 0
    odd = 0
    for i in str(nam):
        if int(i) % 2 == 0:
            even += 1
        else:
            odd += 1
    
    if even > 0 and odd > 0:
        return 'mixed'
    elif even > 0 and odd == 0:
        return 'even'
    else:
        return 'odd'
print(luwi_kenti())