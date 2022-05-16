l1 = [1,1,1,1,1,1,1,4,4,4,4,4]
val = 1
l1.remove(val)
print(f"After removing single occurence : {l1}")

#To remove all occurences

l1 = [1,1,1,1,1,1,1,4,4,4,4,4]
val = 1
l1 = [i for i in l1 if i!=val]
print(f"After removing multiple 1's: {l1}")