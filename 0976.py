f = open('0976.txt (3).TXT')
a = f.readline()
k = 0
maxx = 0
for i in range(len(a)):
    if k < 9:
        if (a[i] == 'B' and k % 5 == 0) or  (a[i] == 'E' and k % 5 == 1) or (a[i] == 'B' and k % 5 == 2) or (a[i] == 'R' and k % 5 == 3) or (a[i] == 'A' and k % 5 == 4):
            k += 1
            maxx = max(maxx, k)
            
        elif a[i] == 'E' or a[i] == "C" or a[i] == "D"  or a[i] == "F" or a[i] == "G":
            maxx = maxx -1
            k = 0
        else:
            k = 0
    else:
    
        maxx = max(maxx, k)
   
print(maxx)
    
