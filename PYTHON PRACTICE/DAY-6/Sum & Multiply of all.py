l1 = [66,4,333,545,1001]
l2 = sum(l1)
print(f"Sum of all elements in l1 : {l2}")

def multplyall(l):
    res = 1
    for i in l:
        res = res*i
    return res
l1 = [66,4,333,545,1001]
print(multplyall(l1))