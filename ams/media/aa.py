n=int(input())
a=list(raw_input().split(' '))
b=list()
for i in range(0,n):
    if a[i] not in b:
        b.append(a[i])
print(b[:],b.__len__())