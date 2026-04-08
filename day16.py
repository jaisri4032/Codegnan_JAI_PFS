'''
recursive functions
--------------
recursion is a programming technique where a function calls
itself either directly or indirectly to solve problem by
breaking it into smaller , simpler subproblem.
Recursion is especially useful for problems that can be
divide into identical smaller tasks,such as mathematical
calculations, tree traversals or divide -and-conquer algorithms.

def validate_pin(self):
    while self.remaining_attempts > 0:
        user_pin = input("Enter 4 digit pin :")
        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
           print("Welcome to the ATM")
           return True
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts > 0:
                print(f"Invalid pin.Attempts left:{self.remaining_attempts}")
            else:
                print("card blocked.please contact customer service")
                return False

count_vo_con = "python is a programming language"
vowels = 0
consonants = 0
def vow_con(count_vo_con,vowels,consonants):
   for j in count_vo_con:
       if j in "AEIOUaeiou":
           vowels += 1
       else:
            consonants += 1
   print(f"{vowels} these are vowels")
   print(f"{consonants} these are vowels")
vow_con(count_vo_con,consonants,vowels)

count_vo_con = "python is a programming language"
vowels = []
consonants = []
def vow_con(count_vo_con,vowels,consonants):
   for j in count_vo_con:
       if j in "AEIOUaeiou":
           vowels.append(j)
       else:
            consonants.append(j)
   print(f"{vowels} these are vowels")
   print(f"{consonants} these are vowels")
vow_con(count_vo_con,consonants,vowels)

    
prime = int(input("Enter any number :"))
count = 0
def prim_check(prime,count):
    for i in range(1,prime+1):
       if prime % i == 0:
           count += 1
if count == 2:
    print(f"{prime} is a prime number")
else:
    print(f"{prime} is not a prime")     
prim_check(prime,count)
'''
