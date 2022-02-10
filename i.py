nm = "@gmail.com"
for i in range(int(input())):
    k = str(input())
    m=k.find(nm,0,len(k))
    if m == len(k)-10 and len(k) > 10:
        print(k[0 : m])

