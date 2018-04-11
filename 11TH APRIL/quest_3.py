n=0
sum=0
s=[]
n=int(input("Enter n: "))
for i in range(1,n+1):
    sum=sum+i
print("Sum of %d terms : %d \n" %(n,sum))

#n=int(input("Enter n: "))
print("All no.s divisible by %d in range (1-500)" %n)
for i in range(1,501):
    if i % n==0:
        s.append(i)
print(s)        
print("******")
#Pascal's tringle
print("Pascal's tringle :")
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()
 
print("******")
#n to sum into-- n + nn + nnn: "))
print("\n n + nn + nnn:")
n1=n
n2=n*10+n
n3=n*100+n*10+n
print("%d + %d + %d : %d" %(n1,n2,n3,(n1+n2+n3)))

 
print("******")
#1 + 1/2 + 1/3 + ... 1/n 
print("1 + 1/2 + ... 1/%d " %n)
for i in range(1,n+1):
    sum=sum+(1/i)
print("\n",sum)



