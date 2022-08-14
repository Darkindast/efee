from itertools import *
k1 = 0
k = 0
for s  in product('0123456789A', repeat = 7):
    a =''.join(s)
    if a[0] != '0':
        for i in range(len(a)-2):
            if (a[i] =='6' or a[i] =='A') and (a[i+1]=='3' or a[i+1]=='4' or a[i+1]=='5' or a[i+1]=='7') and (a[i+2] =='6' or a[i+2] =='A'):
                k += 1 
        if k >= 1:
            k1 += 1 
print(k1)
