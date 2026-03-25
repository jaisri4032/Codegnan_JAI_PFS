'''
vowel_con = input("enter any letter")
if vowel_con in "AEIOUaeiou":
    print("vowel")
else:
    print("consonant")
'''
#converting 24hrs time to 12hrs time usecase
'''
time_aday = input("Enter 24hrs time:")
parts_ = time_aday.split(":")
hours_ = int(parts_[0])
Min_ = int(parts_[1])
if hours_>=13 and Min_ < 60:
    print(f"{time_aday} is converted into {hours_ - 12}:{Min_}pm")
else:
    print("you have entered nrml or min incorrect")
'''
#list---> different types inside the [],which are separated by ,
#eg---> [1,"name",[1,2,"jai"]]
'''
list_1 = [1,2,3,"python",[1,2,["python", "java"],"language"]]
print(list_1[4][0])
'''
#Methods of list
#<-------------->
#append)--->this method is used to add new items into list,it will only go for the index of the list
#Syntax---> variable_name.append[item]
#extend()
#remove()
#pop()

#append()ex
'''
list_2 = [1,2,3,4,5]
print(list_2)
list_2.append("jai")#Mutable---> i can directly modify on that paticular variable.
print(list_2)
list_2.append([45,46])
print(list_2)
#Immutable----> i can't modify directly on the particular variable.
'''
#extend()--->this method is used to add items to list in the last index,
           #where each item or substring is each index in the list.
#Syntax---> variable_name.extend(item)
#extend()ex.1
'''
list_3 = [25,6,7,]
list_3.extend("jai")
print(list_3 )
'''
#extend()ex.2
'''
list_3.extend("jai")
list_3 = [25,6,7,]
list_3.extend("jai")
list_3.append("sri")
print(list_3 )
'''
#remove()----> this method will delete the item or a value directly.
#Syntax--->variable_name.remove(item)
#remove()ex.1
'''
list_4 = ["jai","sri"]
list_4.remove("sri")
print(list_4)
'''
#remove()ex.2
'''
list_4 = [1,5,6,78,60]
list_4.remove(5)
print(list_4)
'''
#pop()---> this method will delete the item or value based on index position
#syntax--->variable_name.pop(index)
#pox()ex.1
list_5 = [90,55,"java",7,9]
list_5.pop(2)
print(list_5)
