str1 = "MaTtMuRdOcK"
lower = []
upper = []
for char in str1:
    if char.isupper():
        upper.append(char)
    else:
        lower.append(char)
sorted = "".join(lower + upper)
print(f"Sorted list : {sorted}")