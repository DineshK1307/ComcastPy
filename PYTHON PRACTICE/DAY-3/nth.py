n = int(input("Enter the Index number :"))
str = input("Enter the String :")
mod_str = ''
for char in range(0, len(str)):

	if(char != n):
		mod_str += str[char]

print(f"mod_str : {mod_str}")