n=int(input("Enter no of digits:"))
c=0
l=[]
for i in range(1,n):
    for j in range(1,i+1):
        if j**2==i:
            l.append(i)
            c+=1
            break
for k in l:
    print(k,end=" ")
print(" ")
print(c)