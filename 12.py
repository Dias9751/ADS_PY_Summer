#Selection sort
import sys
from random import randint
A = []
for i in range(500):
    A.append(randint(0, 500))

print ("First array:\n")
print (A, "\n\n\n")
 

for i in range(len(A)):
 min_idx = i
 for j in range(i+1, len(A)):
  if A[min_idx] > A[j]:
   min_idx = j
    
 A[i], A[min_idx] = A[min_idx], A[i]
 

print ("Sorted array")
for i in range(len(A)):
 #print("%d" %A[i]),
 print(A[i], end = " ")