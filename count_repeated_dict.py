n=int(input())
l=[int(x) for x in input().split()]
f= {}
for i in l:
    if (i in f):
        f[i] += 1
    else:
        f[i] = 1
for k,v in f.items():
    print(k,"-",v,sep="")
