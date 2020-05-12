import re

inp = input("Enter the file name")
fl = open(inp)

lst = []

for i in fl:
    i = i.rstrip()
    cont = re.findall('[0-9]*',i)
    if (len(cont)!=1) : continue
    num = (cont[0])
    lst.append(num)


print(len(lst))

sums = 0
for ele in range(0, len(lst)): 
    sums = sums + lst[ele]
    
print(sums)
print(lst)