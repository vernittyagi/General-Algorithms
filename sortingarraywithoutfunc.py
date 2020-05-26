# Program to sort an array

def sort(num):
    new_num = []
    while num:
        minimum = num[0]
        for x in num:
            if x<minimum:
                minimum = x
        new_num.append(minimum)
        num.remove(minimum)
    print(new_num)
num = [55,66,44,8,96,5]
sort(num)
