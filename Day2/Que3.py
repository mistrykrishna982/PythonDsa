l=['hvb','hdgf','bjd','bjd','riya','om','diya']
f=0
for i in range(len(l)):
    if l[i]=="riya":
        f=1
        break
if f:
    print("present at ,",i+1,"position")
else:
    print("not present")