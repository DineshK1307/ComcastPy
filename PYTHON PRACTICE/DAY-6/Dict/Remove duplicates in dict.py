d1 = {'A':20, 'B':33, 'C':20, 'D':20, 'E':55}
temp = []
res = dict()
for key,val in d1.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
print(res)