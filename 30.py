# HW 5lab 
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
l = a
for value in b:
    if value not in a:
        l.append(value)

d = l
for value in c:
    if value not in l:
        d.append(value)

print ("First array is:", d)

def bubbleSort(arr):
    n = len(arr)
   
    swapped = False
    
    for i in range(n-1):
        
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print (arr)
         
        if not swapped:
            
            return
 

bubbleSort(d)
 
print("Sorted array is:")
for i in range(len(d)):
    print("% d" % d[i], end=" ")


