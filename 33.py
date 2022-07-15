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

def partition(l, r, nums):
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 
def quicksort(l, r, nums):
    if len(nums) == 1:  
        return nums
    if l < r:
        pi = partition(l, r, nums)
        print (d)
        quicksort(l, pi-1, nums)  
        quicksort(pi+1, r, nums)
    return nums