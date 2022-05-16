def di(d1):
    res = {}
    for val in d1.values():
        res[val] = len(val)
    return res

d1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
print(f"length of values form dict : {di(d1)}")
d1 = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
print(f"Length of values from dict : {di(d1)}")

