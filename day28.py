'''
#Regular expression(RegEx):
--->This regular expression or RegEx is a sequence of characters that
    forms a searching patterns.
--->To use this we have to import #(re), which will unlock the package

Functions:
    1.findall
    2.search


#1.findall
-->by using this fuction , it will find all sequence in the string.
#SYNTAX:re.findall("metachar",variable_name)
#EXAMPLE:
import re
any = "python is used as basic for AI"
so = re.findall("o",any)
print(so)

#2.search
-->by using this function , it will only find first sequence in the string.
#SYNTAX:re.search("metachar",variable_name)
#EXAMPLE:
import re
any = "python is used as basic for AI"
so = re.search("o",any)
print(so)

#Metacharacters:
--->Metacharacters are used to form searching pattern.
    1.[]
    2.dot(.)
    3.^
    4.$
    5.*
    6.+

#1.[]
----> in this metacharacters we can searchfor [a-z], [A-z], [0-9]
#EXAMPLE:

import re
any = "hai may name is jaisri from visakhapatnam"
so = re.findall("[a-n]",any)#searching pattern
print(so)

import re
any = "hai may name is jaisri from visakhapatnam"
so = re.findall("[an]",any)#searching pattern
print(so)

import re
any = "hai may name is j9aisri from v6isakhapatnam"
so = re.findall("[69,a]",any)#searching pattern
print(so)

#2.dot(.)
--->This meta character will form a searching pattern as it will take
any single character for(.).

import re
we = "jaisri"
the = re.findall("..i..i",we)
print(the)

import re
we = "jaisri"
the = re.search("..i..i",we)
print(the)

#3.^
---> this is used to find the string is starting with sequence or
#SYNTAX:re.search("^metachar",variable_name)

import re
how = "hai looking gorgeous"
so = re.findall("^hai ",how)
print(so)

import re
how = "hai looking gorgeous"
so = re.search("^hai ",how)
print(so)

#4.$
---> this is used to find the string is ending with the sequence or no.
#SYNTAX:re.search("$",variable_name)
#EXAMPLE:
import re
how = "hai looking gorgeous jai"
so = re.findall(" jai$", how)
print(so)

import re
how = "hai looking gorgeous jai"
so = re.search(" jai$", how)
print(so)

5.*
--->This meta character will form a searching pattern as it will take
any zero or more character for(*).
#SYNTAX:re.search(".*",variable_name)
#EXAMPLE:

import re
how = "hai looking gorgeous jai"
so = re.search("h.*s", how)
print(so)

import re
how = "hai looking gorgeous jai"
so = re.findall("h.*s", how)
print(so)

6.+
--->
This is meta character will form a searching pattern s it will take any
one or more character for(+).
#SYNTAX:re.search(".+",variable_name)
#EXAMPLE:
'''
import re
how = "hai looking gorgeous jai"
so = re.findall("hai.+g", how)
print(so)







