'''
prim = int(input("enter number"))
count = 0
for j in range(1,prim+1):
    print(j)
    if prim % j == 0:
       count += 1
       print(count)
if count == 2:
    print(f"{prim} is a prime number")
else:
    print(f"{prim} is not a prime number")

for an in range(2,100):
    count = 0
    for j in range(1,an+1):
       if an % j==0:
           count += 1
    if count == 2:
        print(f"{an}is a prime")
    else:
        print(f"{an} not prime

list = [1052,197,9,86,17673]
for an in list:
    count = 0
    for j in range(1,an+1):
       if an % j==0:
           count += 1
    if count == 2:
        print(f"{an}is a prime")
    else:
        print(f"{an} not prime")

any = [2,356,8,6,3,2,8]
empty = []
for j in any:
    if j not in empty:
       empty.append(j)
       print(empty)
'''
#amstrong number
so = 153
len = len(str(so))
amstr = 0
for j in str(so):
    amstr += int(j)**len
if amstr == so:
    print(f"{so} is amstrong number")
else:
    print(f"{so} is not a amstrong number")
    
   
   
