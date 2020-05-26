# Program for Linear Search
pos = -1
def search(num,t):
    for i in range(len(num)):
        if num[i] == t:
            globals()['pos'] = i
            return True
    return False
num = [1,5,4,14,5,69,7]
t = 44
if search(num,t):
    print('found @ ', pos)
else:
    print('Not Found!!')
