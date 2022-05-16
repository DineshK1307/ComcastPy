l1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
l2 = ["A","B","C"]
print(l1[2])
print(l1[2][1])
print(l1[2][1][3])
l1[2][1][2].extend(l2)
print(f"After extending the sublist : {l1}")