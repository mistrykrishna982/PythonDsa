'''
H1) An Amazon fulfilment centre has a conveyor belt with exactly 8 slots numbered 0-7. 
Each slot holds one product. The warehouse manager needs to: 
    check what's at a slot, 
    find a product, 
    update a slot, 
    and check if the belt is full.
The conveyor belt - fixed 8 slots
'''
belt=["laptop","phone","smart watch","digital pen","google lens","charger","head phones","fan"]


a=int(input("enter slot no(0-7):"))
print(f"product of that slot:{belt[a]}")

prd=input("enter product:")
print(f"index of that product:{belt.index(prd)}")

slot=int(input("enter slot no(0-7):"))
product=input("enter new product:")
belt[slot]=product
print(f"index of that product:{belt}")

if len(belt)==8:
    print("belt is full")
else:
    print("not full")