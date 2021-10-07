#https://www.youtube.com/watch?v=MzC1eYxOYk8

from collections import Counter

n=int(input())
fl=[]
for i in range(n):
    s=input()
    s=s.replace("-"," ")
    l=s.split()
    fl.append(l)

d={}

for i in fl:
    
    if int(i[2])>int(i[3]):
        if i[0] in d.keys():
            d[i[0]]=d[i[0]]+3
        else:
            d[i[0]]=3
    
    elif int(i[3])>int(i[2]):
        if i[1] in d.keys():
            d[i[1]]=d[i[1]]+3
        else:
            d[i[1]]=3

    elif int(i[3])==int(i[2]):
        if i[1] in d.keys():
            d[i[1]]=d[i[1]]+1
        if i[0] in d.keys():
            d[i[0]]=d[i[0]]+1
        if i[0] not in d.keys():
            d[i[0]]=1
        if i[1] not in d.keys():
            d[i[1]]=1

d=Counter(d)
f=d.most_common()
print(f[0][0])
print(f[0][1])    








