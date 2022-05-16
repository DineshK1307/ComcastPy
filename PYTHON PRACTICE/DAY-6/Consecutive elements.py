l1 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
prev = None
new = []

for ele in l1:
    if ele!=prev:
        new.append(ele)
        prev=ele
print(f"After removing consecutive : {new}")