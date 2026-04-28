'''
continuation for day28.py
Regular expresions:
    7.?
    8.{}
    9.|

#7.?
-->this is metacharacter will form a searching pattern as it will make
   any zero or one character for (?)
#SYNTAX:re.findall(".?",variable_name)

import re
any = "hai my name is jaisri"
an = re.search("ja....?",any)
print(an)

import re
any = "hai my name is jaisri"
an = re.findall("jai...?",any)
print(an)

8.{}
-->this is metacharacter will form a searching pattern as we can mention the size in the {}
#SYNTAX:re.findall(".{size}",variable_name)   

import re
any = "hai my name is jaisri"
an = re.findall("ha.{10}",any)
print(an)

import re
any = "hai my name is jaisri"
an = re.findall(".{10}ri",any)
print(an)

import re
any = "hai my name is jaisri"
an = re.findall(".{5}",any)
print(an)

9.|
-->this is metacharacter will form a searching pattern as it consider right or left any string is present or not for(|).

import re
any = "hai my name is jaisri"
an = re.findall("my|is",any)
print(an)

-----------------------------
#SPECIAL SEQUENCE:
Return a match if the specified characters are at the beginning of the string
    1.\A
    2:\b
    3.\d
    4:\D
    5:\s
    6:\S
        

1.\A:Returns a match if the specified characters are at the beginning of the string.
eg:"\ATHE"



import re
txt = "The rain in Spain"
#Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)
if x:
     print("Yes, there is a match!")
else:
    print("No match")

2:\b- Returns a match where the specified characters are at the beginning or at  
 end of a word
 Eg: r"\bain"
 
import re
txt = "The rain in Spain"
 #Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\bSpain", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


3:\d- Returns a match where the string contains digits (numbers
Eg: "\d"

import re
txt = "The rain in 556 Spain"
#Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


4:\D- Returns a match where the string DOES NOT contain digits
Eg: "\D"

import re
txt = "The rain in 67 Spain"
#Return a match at every no-digit character:
x = re.findall("\D", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")





5:\s- Returns a match where the string contains a white space
character
Eg: "\s"

import re
txt = "The rain in Spain"
#Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


6:\S- Returns a match where the string DOES NOT contain a white space character
Eg: "\S"

import re
txt = "The rain in Spain"
#Return a match at every NON white-space character:
x = re.findall("\S", txt)
print(x)
if x:
    print("Yes, there is at least one match!")
else:
    print("No match")


-----------------------------
#Time and Date:
    %d--->day
    %m--->month
    %Y--->year
    %H--->Hours
    %M--->Minutes
    %S--->Seconds
    %p--->AM/PM
    %A--->Day names
    %B--->Month name
'''
import datetime
now = datetime.datetime.now()
print(now)

import datetime
today = datetime.date.today()
print(today.strftime("%d/%m/%Y"))
print(today.strftime("%A"))
print(today.strftime("%B"))




