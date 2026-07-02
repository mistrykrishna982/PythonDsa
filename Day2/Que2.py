a=[7,9,4,5,6,2,3,1,67,87,45,342,3,100]
for i in range(len(a)):
    max=i
    for j in range(i+1,len(a)):
        if a[max]>a[j]:
            max=j
    t=a[max]
    a[max]=a[i]
    a[i]=t
print(a)