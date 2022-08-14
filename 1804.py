f = open('1804.txt')
a = f.readline()
n = int(input())
k = 0
s =''
d = []
for i in range(len(a)):
    if a[i] != ' ':
        k += 1
        s += a[i]
        if i+1==len(a):
            if k >= n:
                d.append(s) 
    else:
      
        if k >= n:
            d.append(s)
        k = 0
        s = ''
print(*d)
    
    
