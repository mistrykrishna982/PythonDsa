a=[7,9,4,5,6,2,3,1,67,87,45,342,3]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            t=a[i]
            a[i]=a[j]
            a[j]=t
print(a)