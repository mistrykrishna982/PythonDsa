a=[87,95,65,54,97,65,108,76,975,654,987]
a.sort()
print(a)
left=0
f=0
right=len(a)-1
s=int(input("enter data for search:"))
while(left<=right):
    mid=(left+right)//2
    if(a[mid]==s):
        print("\n found at ,",mid+1,", position")
        f=1
        break
    elif(s>a[mid]):
        left=mid+1
    elif(s<a[mid]):
        right=mid-1
if(f==0):
    print("\nnot found")