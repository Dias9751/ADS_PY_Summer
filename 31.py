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

def insertionSort(arr):
    for i in range(1, len(arr)):
 
        key = arr[i]

        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
        print (arr)
 
insertionSort(d)
 
print("Sorted array is:")
for i in range(len(d)):
    print("% d" % d[i], end=" ")