l1 = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]

flat_list = []
for sublist in l1:
    for num in sublist:
        flat_list.append(num)

print(f"Flattend List : {flat_list}")