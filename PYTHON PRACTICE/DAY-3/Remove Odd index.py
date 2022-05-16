str1 = input("Enter a string : ")
str2 = ''
for i in range(len(str1)):
    if(i%2==0):
        str2 = str2 + str1[i]
print("After removing the odd index: ", str2)