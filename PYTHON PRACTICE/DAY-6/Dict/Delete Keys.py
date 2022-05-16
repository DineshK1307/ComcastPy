d1 =  {1: 'CSK', 2: 'RCB', 3: 'MI', 4: 'RR'}
d1.pop(1)
print(f"After deleting key : {d1}")
# d1.pop(5) # key error

d1.pop(5,None)
print(f"After deleting key : {d1}")
