#HW lab5 ex5
import random
a, b, c = [], [], []
for i in range(15):
    x = random.randint(1,99)
    y = random.randint(1,99)
    z = random.randint(1,99)
    a.append(x)
    b.append(y)
    c.append(z)
print(a,"\n",b,"\n",c)
l = []
for value in b:
    if value not in c:
        l.append(value)

d = l
for value in a:
    if value not in c and value not in l:
        d.append(value)

print ("First array is:", d)

for i in range(len(d)):
    min_idx = i
    for j in range(i+1, len(d)):
        if d[min_idx] > d[j]: min_idx = j
    
    d[i], d[min_idx] = d[min_idx], d[i]
    print (d)

print("Sorted array is:")
for i in range(len(d)):
    print("% d" % d[i], end=" ")