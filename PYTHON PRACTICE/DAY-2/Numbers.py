a=10
print(type(a)) #RTTI - Run Time Type Identification
b=-10
print(f"b : {b}")
print(type(b))
c=-10.00
print(type(c))

e= +2e3
f= -2e3
print(type(e))
print(e)
print(f)

g= 2+4j
print(type(g))
print(f"g : {g}")

print(max(100, 566, 676))
print(min(1111111111111, 11111111111111, 1111111111))

x= 2+3.6
print(type(x))

x=1
y=2.5
z=x+y
print(type(x))
print(type(y))
print(type(z))

print("DINESH".center(20,"-"))

a=-10
print(type(a))
print(type(float(a)))
print(complex(a))
print(type(complex(a)))


print("NUMBER SYSTEMS".center(20,"-"))

print(11)   #decimal
print(0b11) #binary
print(0b101)
print(0o111) #octal
print(0xe)   #hexa
print(0xa)

print("CONVERSION OD NUMBER SYSTEMS".center(20,"-"))

a=1000
print(bin(a))
print(hex(a))
print(oct(a))