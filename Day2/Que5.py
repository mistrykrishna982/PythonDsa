'''
h1)-The Spam Detector (Search in Stream) -linear search
A cybersecurity intern at a startup is building a basic spam filter. Incoming emails are checked against a blacklist of known spam sender IDs. The blacklist has no order.
'''

s=["a101","a102","a193","a654","a225","a906"]
f=0
e=input("enter ids:")
for i in range(len(s)):
    if s[i]==e:
        print("found at ,",i+1,",position")
        f=1
        break
else:
    print("not found")
    