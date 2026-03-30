#loops---->loops are used to block of code in multiple times without writing again and again
 #for loop and while loop
'''
for i in range(10):
    print("jai")

for i in range(10):
    print(i)

for i in range(1,12,4):
    print(i)

for i in range(100,120):
    print(i)

i = int(input("enter any number"))
if i==2:
    print("true")
else:
    print("false")

for i in range(1,6):
    if i==3:
        print("true")
    else:
        print("****")

for i in range(1,6):
    if i==3:
        continue
    print(i)

name = "jai"
for i in name:
    print(i)

name = "jai"
for i in name:
    print(i,end="-")

text = input("enter the paragraph:")
vowels = 0
consonants = 0
spaces = 0
vowel = "aeiou"
for par in text.lower():
    if par in vowel:
        vowels += 1
    elif par.isalpha(): 
        consonants += 1
    elif par.isspace(): 
        spaces += 1
print(f"Vowels: {vowels} ")
print(f"Consonants: {consonants}")
print(f"Spaces: {spaces}")

any = input("enter youre lines")
vowels = 0
conso = 0
space = 0
for j in any:
    if j in "AEIOUaeiou":
        vowels += 1
    elif j == " ":
        space +=1
    else:
        conso +=1
print(vowels)
print(conso)
print(space)

any = input("enter youre lines")
vowels = 0
space = 0
for j in any:
    if j in "AEIOUaeiou":
        vowels += 1
    elif j == " ":
        space +=1
print(f"this is count of all vowels in string {vowels}")
print(f"this is count of all spaces in string {space}")
print(f"this is count of all conso in the string {len(any)-(vowels+space)}")

a = 10#normal variable
print(a)
for i in range(1,10):#"i" is a nitial variable also we will not get error in initial variable
    print(i)

for i in range(1,11,2):
    print(i)
'''
# range()---> this is used to generate the numbers
#SYNTX---->range(start,end,step)

for i in range(1,11,4):
    print(i)

for i in range(0,5):
    print(i)

any = "123456"
print(int(any))
print(list(any))
print(tuple(any))

so = 12345
print(str(so))
print(float(12345))

a = [1,2,3]
bn = (str(a))
print(type(bn))
print(bn)
print(tuple(bn))

a = [(1,2),(3,4)]
print(dict(a))

a = "jaisri"
print(a[::-1])
rev = "jaisri"
empty = ""
for j in rev:
    empty += j 
    print(empty)

rev = "jaisri"
empty = ""
for j in rev:
    empty = j + empty
    print(empty)

rev = "madam"
empty = ""
for j in rev:
    empty = j + empty
if empty == rev:
    print(f"this is palin {rev}")
else:
    print(f"this is no palin {rev}")

rev = "*****"
empty = ""
for j in rev:
    empty = j + empty
    print(empty)

rev = "*****"
empty = " "
for j in rev:
    empty += j 
    print(empty)

for num in range(1,10):
    if num % 2 == 0:
        print(f"{num}:is a even number")
    else:
        print(f"{num}:is odd number")
