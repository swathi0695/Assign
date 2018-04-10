import numpy as np
m1=[]
m2=[]
m3=[]
m4=[]
t1=0
t2=0
t3=0
t4=0
total=[]

print("Enter Roll.No. 1 marks : ")
for i in range(4):
    m1.append(int(input(" Sub%d : " %(i+1))))
    t1 += m1[i]

print("Enter Roll.No. 2 marks : ")
for i in range(4):
    m2.append(int(input("Sub%d :" %(i+1))))
    t2 += m2[i]
    
print("Enter Roll.No. 3 marks : ")
for i in range(4):
    m3.append(int(input("Sub%d :" %(i+1))))
    t3 += m3[i]

print("Enter Roll.No. 4 marks : ")
for i in range(4):
    m4.append(int(input("Sub%d :" %(i+1))))
    t4 += m4[i]
print("******")
print("Highest marks :")
print("Roll No. 1 : %d " %max(m1))
print("Roll No. 2 : %d " %max(m2))
print("Roll No. 3 : %d " %max(m3))
print("Roll No. 4 : %d " %max(m4))

#for i in range(4):
#total.append('t1'))#,t2,t3,t3)
print("******")

print("Ascending order :")
print("Roll No. 1 : ",sorted(m1)) 
print("Roll No. 2 : ",sorted(m2)) 
print("Roll No. 3 : ",sorted(m3)) 
print("Roll No. 4 : ",sorted(m4)) 

print("******")

#print(len(m1))
for i in range(4,6):
    m1.insert(int(input("%d :" % (m1[i]))))
    m2.append(int(input("%d :" % (m2[i]))))
    m3.append(int(input("%d :" % (m3[i]))))
    m4.append(int(input("%d :" % (m4[i]))))







    
    
    
    