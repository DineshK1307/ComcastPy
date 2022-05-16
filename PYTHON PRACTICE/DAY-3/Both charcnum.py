str1 = input("Enter a mixed string: ")
res = []
temp = str1.split()
for i in temp:
    if  any (chr.isalpha() for chr in i ) and any  (chr.isdigit() for chr in i):
        res.append(i)
print("Both charcter and number : " + str(res))