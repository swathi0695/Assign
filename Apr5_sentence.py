letter=0
digit=0
p=input("Enter a sentence : ")
#words=p.split()
for i in range(len(p)):
    if p[i].isalpha():
        letter=letter+1
    elif p[i].isdigit():
        digit=digit+1
print("Letter: %s, Digits: %s"%(letter,digit))