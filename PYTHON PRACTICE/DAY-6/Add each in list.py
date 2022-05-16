l1 = ["MATT ","MURDOCK "]
l2 = ["KAREN","FOGGY"]
l3 = [x+y for x in l1 for y in l2]
print(f"Adding each element in both lists : {l3}")