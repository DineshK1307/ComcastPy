def di(d1):
    for key in d1:
        d1[key].clear()
    return d1
d1 = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
print(f"after clear values in dict : {di(d1)}")
