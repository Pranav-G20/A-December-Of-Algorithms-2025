n=int(input("Enter a number"))
w=len(bin(n)) - 2
for i in range(n+1):
    d=str(i)
    o=oct(i)[2:]
    h=hex(i)[2:].upper()
    b=bin(i)[2:]
    print(d,o.rjust(w),h.rjust(w),b.rjust(w))