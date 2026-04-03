#break--> This is used to exit from the loop, when we found the required element or value...
'''
for j in range(1,10):
    print(j)
    if j==1:
        break

for j in range(1,10):
    print(j)
    if j==1:
        print("hai")
    break

for j in range(1,10):
    print(j)
    if j==1:
        break
    print("hai")
'''

'''
lis=[1,2,3,4]
for i in lis:
    print(i)
    #if n==1: #NameError: name 'n' is not defined
    if i==1:
        break
'''

#continue --> this is used to skip that particular loop
'''
for j in range(1,10):
    if j==5:
    #if j==5 and j==10:
        break
    print(j)

lis=[1,2,3,4]
for n in lis:
    if n==3:
        continue
    print(n)
'''
'''
#pass-- this is called as space holder
incase any statement like(for,if,else,elif ....) this should be complete,if not we will get indentation
error to avoid this we are using pass 

for j in range(1,100):
    pass
'''

#else -- for : it will fall back to else block,when all loops are completed
'''
for m in range(1,10):
    print(m)
else:
    print("else block")

for m in range(1,10):
    if m==10:
        print(m)
    break
else:
    print("else block")
'''
#while --> this is combination for and if stmts, if we did not end the loop in proper it way it will
#run upto the memory space in the becomes empty
'''
num = 1
while num<5:
    print(num)
    num+=1

#fibonacci series

user_input=int(input("enter the numbers:"))
num_1=0
num_2=1
print(num_1,num_2,end=" ")
#for n in range(user_input): #range start with 0, we want excluded ending number e.g:9 (0,1,2,3,4,5,6,7,8)
for n in range(user_input+1): #range start with 0, we want included ending number added it to 1 e.g:9 (0,1,2,3,4,5,6,7,8,9)
    num_3=num_1+num_2
    num_1=num_2
    num_2=num_3
    print(num_3,end=" ")
    '''
