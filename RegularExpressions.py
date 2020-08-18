#Regular expression module re , used to search , validate , match strings etc uses are in email , password or sub-string searching

'''      
            sequence chracters     (start with backslash)

\d : find a single chracter in a string which is a digit
\D : find a single chracter in a string which is a non-digit

\s : matches a white space in string
\S : matches a non white space in string

\w : any alphanumeric value
\W : non alpha numeric chracter

\b : space around words

\A : matchs only start of string
\Z : matches ony at the end of string

'''

import re                       #regulare expression module

#search
string = 'Big quick brown quack quakur fox jumps over the lazy dog'
result = re.search(r'l\w\w\w',string)                                     #here we're searching for lazy , so we use l as first and use regular expresssion to find words starts with f and have 4 chracters in total (alphanumeric), regular expression is as follows
print(result.group())                                                  #group() funtion for the result that comes from search/match method

#findall
res = re.findall(r'q\w\w\w\w', string)                      #findall finds all the sequennce we give here we're trying to find all sub-strings starting with q and have 5 chracters in total
print(res)

#match
mat = re.match(r'B\w\w', string)                             #match method only matches at the start of string , it wont work when we find inside the string and returns a None
print(mat.group())

#split                                                    #splits a string into list of strings on the basis of regular expression which we pass as delimiter
ourSTR = 'the string 1122 is made of 22 multiple 44 pieces 88 broken 99 now'
result = re.split(r'\d+',ourSTR)                           #\d digit used to split and + sing means one or more digits(quantifiers we discuss them next)
print(result)                      

#substitute
sample = 'a simple , we say very simple string , on we perform simple substitution'
result = re.sub(r'simple', 'complex', sample)
print(result)

#Quantifiers

'''
+ : one or more Repetition of expressions e.g \d+
* : zero or more Repetition 
? : zero or 1 Repetition 
{m} :exactly m Repetition
{m,n}  : m = minimum occurence n = maximum occurence (Default m = 0 , n = infinity)
'''

#using Quantifiers
str = 'One two One On and On owl at night clear text to test quantifiers Come on'
result = re.findall(r'O\w*', str)
print(result)

#Fidning date in given string
str = '22-05-2011 is a day , 09-11-1999 was a day ,,,try matching date like 05-10-1998'
result = re.findall(r'\d{1,2}-\d{1,2}-\d{2,4}',str)               #using {m,n} quantifier as we discussed earlier (it will give us date in the given string)
print(result)