'''
h3) Merge Sort - The IRCTC Waitlist Merger
IRCTC has two separately sorted waitlists one from its mobile app, one from railway counters. To produce a final unified waitlist, they don't re-sort from scratch. They merge both sorted lists in one pass compare the front of each list, pick the smaller token, advance. This is exactly merge sort's merge step.
'''

a1 = [1,4,5,7,8]
a2 = [2,3,6,9]
merge=[]

i=0
j=0

while i<len(a1) and j<len(a2):
    if a1[i]<a2[j]:
        merge.append(a1[i])
        i+=1
    else:
        merge.append(a2[j])
        j+=1
while i<len(a1):
    merge.append(a1[i])
    i+=1
while j<len(a2):
    merge.append(a2[j])
    j+=1
print(merge)
