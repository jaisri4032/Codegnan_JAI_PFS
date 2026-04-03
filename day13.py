num = 5
for j in range(num):
    for i in range(j):       
        print("*", end = "")
    print()

num = 5
for j in range(num):
    for i in range(num):
        print("*", end = "")
    print()
    

num = 5
for j in range(num):
    for i in range(j):
        print(j, end = "")
    print()

num = 5
for j in range(num):
    for i in range(num):
        print(i, end = "")
    print()

num = 5
for j in range(num):
    for i in range(j):
        print(i, end = "")
    print()

num = 5
for j in range(num):
    print(" " * (num-j),end = "")
    for i in range(j+1):  
        print("*",end = " ")
    print()

num = 5
for j in range(num):
    print(" " * (num-j),end = "")
    for i in range(j+1):  
        print("*",end = "")
    print()
