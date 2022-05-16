str1 = input("Enter mixed string : ")
alph = 0
dig = 0
special = 0
for i in range(len(str1)):
    if(str1[i].isalpha()):
        alph = alph+1
    elif(str1[i].isdigit()):
        dig = dig+1
    else:
        special = special+1
print("Alphabets in string : ",alph)
print("Digits in string : ",dig)
print("Special in string : ",special)

