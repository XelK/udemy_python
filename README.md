Content-Type: text/x-zim-wiki
Wiki-Format: zim 0.4
Creation-Date: 2019-06-16T14:09:48+02:00

# Python

Created Sunday 16 June 2019

contain  notes/examples of Udemy course   "Automate the Boring Stuff with Python Programming"

https://www.udemy.com/automate/

# Python Basics

## Book

Automating the boring stuff with python

Al Sweigard

https://automatetheboringstuff.com.

opensource book/printable/available on amazon

--------------------

## Expressions

*all expressions are just value and operators*
* value: 2 , 5 , 39204
* operators: + , - , *, ...

## Data Types

*all data belong to types*
* integer
* float
* string

## Variables

*box for some values*
*override the variable*

--------------------
comments
 ''# this is a comment''
*functions are kind of miniprogramm into programm*

print() # function to print

input function
''input ()''

len ()  # len of the string

str ( int (myAge)) 

--------------------

# Flow Control

#### boolean values

* have only 2 values:
	* True
	* False

#### comparison operators

* ==
* !=
* <
* >
* <=
* >=
*integers and string are always not equal*
*float values and integer values can be equal*

#### boolean operators

* and
* or
* not

### if,else,elif

#### if block

* determinate where block start/finish in base of iden tation

#### Truthy and Falsey Value

* blank string → **Falsey**
* 0 is **falsey **
* all other values are **Truthy**

### While

> while spam < 5: 
  spam = spam + 1

#### break statements / contonue statements

* break into loop
* continue into loop

### For loops

> for i in range(5):
  	print (' hello' + str (i))

*while loop is equivalent to the fot loop*

#### range function

> range (10) 		→(0,9)
  range(3,20) 		→ (3,19)

* for loop:	
	* for i in range (10)   → (0,9)
	* for i in range (5,20) → (5,19)
	* for i in range (0,10,2)  → increase by 2
	* for i in range (5,1,-1)   → decrease by -1 from 5 to 1
*you can use break/continue into for loops*

# Functions

#### built-in funcionts

* print ()
* input ()
* len ()
*modules contain specific functions : math module / rando module/ ecc*
*to import module:*
> import random
  import random, sys, os , math # importing muliple modules

*to call function from the module:*
	   ''random.randint(1,10)  #function randint from module random''

*bad prcacticse:*
> from random import *
  randint(1,10)

*in this case import all from module, and you can use function without indicate the module name*

**terminate the programm before end of flow**
> import sys
  sys.exit( )

**pyperclip module**

*permit to copy/paste text to/from the keyboard*
> import pyperclip
  pyperclip.copy('Hello world!')
  pyperclip.paste()

*need to have *xsel **installed

*the modules that come with Python are called the standard library, but you can also intall third-party modules using the pip tool.*

#### writing your own function

#### functions

*kind of mini-programm inside your program*
*get rid of duplicate code*

> def hello (): 
  	print ('Hello world!')

*Arguments  → the value passed in the function call*
*Parameter → the variable inside the function*

> def hello (name): 
  	print ('Hello ' + name)

#### return value

def plusOne (number) :
		return number + 1

#### the non-value

*the //**None*** value the none type //
*every function return value, ever the ***print ***function.  If  the function not have the return statement, the returned value is None*

#### keyword arguments

* *the print function terminate with newline. You can change this with:*
''print('Hello',  end='')''
* *separation of the strings*
print ('cat', 'dog', 'mouse', sep= 'ABC')

*keyword arguments are optional*

#### global and local scopes

*variables into function and out of function can have the same name:*
* *into function → local scope*
* *out of function → global scope*

#### to assign global variable into function

> def spam ():
  	global eggs
  	eggs = 'Hello'

# Handling Errors with try/except

*it's possible to handle errors and permit terminate the program if some operation failes and not crash the entire program*

> try:
  	operation
  except: 
  	error_handler

*except block is executed when the try block failed*

## First complete program: "Guess the Number "

see guess.py

# Lists

* a value that contain multiple values
* values in a list also called items
* begins and ends with []
* the indexes start at 0
* values are separated with commas

''['cat', 'dog', 'rat']''

### list of list

spam = [''['cat', 'dog', 'rat'],[10,20,30,50]] ''
spam [1,3]  → 50

### negative index

-1 → last value into the list
-2 → second to last item 

### slice

* spam[1:3]  → values from index 1 to index 3 of list 
* spam[:2]  → from 0  to 2 index value
* spam[1:]  → from 1 to end index value

#### operation with list

* assignment
* delete:
	* del statement
* len
* concatenation
* multiplication 
* list ()  → convert to list
* find if element is into the list:
	* 'aaa' **in** ['bbb', 'awd', 'aaa']  → True
	* 'aaa' **not in** ['bbb', 'awd', 'aaa']  → False

## for loops with lists, multiple assignment, and augmented assignment operators

### for

> for i in [0,1,2,3]
  	print (i)

*this is the sequencies in python*

### list function

list(range(4)) → [0,1,2,3]

//usefull to populate the big list //

### len

len(myList) 

### multiple assignment

> cat = ['fat', 'orange', 'loud']
  size, color, disposition = cat
  color → orange

or
''size, color, disposition = 'skinny', black, 'quiet'''

### swap:

> a = 1
  b = 2
  a,b=b,a→ a=2, b = 1

### augmented assignment

> spam += 1
  spam -= 1
  ...

## List Methods

*the method is the same thing as a function but it's attached on a certain value*

#### index

> spam = ['hello','hi','howdy','heyas']
  spam.index('hello')→ 0

*if not find return error message*
*if multiple value present return the first one index*

#### append

> spam = ['hello','hi','howdy','heyas']
  spam.append = ('ciao')
  spam → ['hello','hi','howdy','heyas', 'ciao']

#### insert

> spam.insert(1,'hola')
  spam → ['hello','hola','hi','howdy','heyas', 'ciao']

#### remove

> spam.remove('hola')
  spam → ['hello','hi','howdy','heyas', 'ciao']

*only the first one is removed*

#### sort

> spam = [2,1,5,4]
  spam.sort() → [1,2,4,5]

*also working with strings*
*also in reverse order:*
  ''spam.sort(reverse=True)''
*sort method not work with numbers and string into list*
*N.B: ascii-betical order of sort → Uppercase come before lowercase*
  ''spam.sort(key=str.lower) → sort in true alphabetical order''

## Similarities Between Lists and Strings

*many operations/methods of list are valid to strings too: index,slice, in, for ...*
*lists are mutable → value can be change*
*string are immutable → the value can NOT be changed*
* *you can't reassign a value to some character of the string*
*the correct way to change the string is create a new string from the slices*
> name = 'Zophie a cat' 
  newName = name[0:7] + 'the' + name[8:12]
  newName → 'Zophie the cat'

* *list despite integers are referenced, so when you create new list ad assign the value of the old list. The new and the old one are the same list with the same reference to a memory  and when one of two lists change the other one change too, because is the same computer memory* 
* *for this list is a mutable value because it's not stored into variable*
* *change maded to the list in the local scope are also propogate to the global scope → function receive the copy of the reference and not the copy of the value*

#### copy module

*the copy module permit to copy the list into the new separate list*
> import copy
  spam = ['A','B','C']
  chesse = copy.deepcopy(spam)

*lists can be write on multiple lines:*
> spam = [ 'apples'
  	 'oranges',
  	 'bananas']

*the long line of code can be written on multiple line with '\' :*
> print('This is the long line of code ...' + \
        'here is the another piece of code ...')

# Dictionaries

*collection of many values but unlike list indexes, indexes for dictionaries can use many different data types not just integers*
*indexes for the dictionaries are called keys*
*keys with its associated value is called a key value pair*

> In [24]: myCat = {'size':'fat','color':'gray','disposition':'loud'}
In [25]: myCat                                                                
Out[25]: {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
In [26]: myCat['size']                                                        
Out[26]: 'fat'

*indexes not start from  0, but can be any value*
*dictionaries are unordered (comparison of two dictionaries with different order product True)*

"*in" and "not in" operators working with dictionaries*

'''
In [27]: list(myCat.values())                                                    
Out[27]: ['fat', 'gray', 'loud']

In [28]: list(myCat.keys())                      
Out[28]: ['size', 'color', 'disposition']                                                         

In [29]: list(myCat.items())                     
Out[29]: [('size', 'fat'), ('color', 'gray'), ('disposition', 'loud')]                            

In [30]: myCat.items()  
Out[30]: dict_items([('size', 'fat'), ('color', 'gray'), ('disposition', 'loud')])
'''

*use in for loops:*

'''
In [62]: for k in myCat.values(): 
    ...:     print (k) 
    ...:                
fat
gray
loud
1

In [70]: for k,z in myCat.items(): 
    ...:     print (k,'-',z) 
    ...:                
size - fat
color - gray
disposition - loud
age - 1
'''

#### get method

'''
In [73]: myCat          
Out[73]: {'size': 'fat', 'color': 'gray', 'disposition': 'loud', 'age': 1}

In [74]: myCat.get('age',0)                      
Out[74]: 1
'''

*permit to check if some value exist into the dictionary, without causing error if not. If value not exist, return the default value setted into method*

#### setdefault method

*set the dafault value if not exist*

'''
In [75]: myCat          
Out[75]: {'size': 'fat', 'color': 'gray', 'disposition': 'loud', 'age': 1}

In [76]: myCat.setdefault('color',1)             
Out[76]: 'gray'

In [77]: myCat.setdefault('aaa',213)             
Out[77]: 213

In [78]: myCat          
Out[78]: {'size': 'fat', 'color': 'gray', 'disposition': 'loud', 'age': 1, 'aaa': 213}
'''

#### pprint module

'''
pprint.pprint (count)

rjtext = pprint.pformat(count)
print(rjtext)
'''

*pprint()* *permit to display a dictionary value cleanly*
*pformat() function returns a string value of the output*

## Data structures

*list of dictionaries*

> In [83]: cat    
Out[83]: {'size': 'fat', 'color': 'gray', 'disposition': 'loud', 'age': 1}
In [86]: allCats = []
In [88]: allCats.append({'size': 'gray', 'color': 'gray', 'disposition': 'loud', 'age': 7})
In [90]: allCats.append({'size': 'big', 'color': 'red', 'disposition': 'loud', 'age': 7}) 
In [91]: allCats           
Out[91]: 
[{'size': 'gray', 'color': 'gray', 'disposition': 'loud', 'age': 7},
 {'size': 'big', 'color': 'red', 'disposition': 'loud', 'age': 7}]

#### Type function

*return the type of some object*
'''
In [92]: a = 123        

In [93]: a              
Out[93]: 123

In [94]: type(a)        
Out[94]: int
'''

# More about strings

## Advanced string syntax

string can be delimeted with '... ' or " ... " 

| Escape character | Prints as            |
|:-----------------|:---------------------|
| \'               | Single quote         |
| \"               | Double quote         |
| \t               | Tab                  |
| \ n              | Newline (line break) |
| \\               | Backslash            |

#### Raw string

> In [97]: r'That is a Carol\'s cat'             
Out[97]: "That is a Carol\\'s cat"

*print any backslashes in the string and ignore escape characters*

#### Multiline string

> '''jklsdjflkdsf
   sdhkjfhdskj
   werwoiejr'''

#### Similarities between strings and lists

*can perform many operations on the string as on the lists*

## String methods

### upper() lower ()

'''
In [101]: spam = 'Hello world!'                  

In [102]: spam.upper()  
Out[102]: 'HELLO WORLD!'

In [103]: spam.lower()  
Out[103]: 'hello world!'
'''

### isupper(), islower()

'''
In [107]: spam = 'hello world!'                  

In [108]: spam.islower()
Out[108]: True
'''

### other methods

* isalpha()   - letters only
* isalnum()   - letters and number only
* isdecimal() - numbers only
* isspace()   - whitespace only
* istitle()   - titlecase only (all words inside the string begin with uppercase)

### startswith() / endswith()

'''
In [109]: spam   
Out[109]: 'hello world!'

In [110]: spam.startswith('hello') 
Out[110]: True

In [111]: spam.endswith('d!')      
Out[111]: True
'''

### join()

*usefull when you need to join a list of strings into a single string*

> In[112]:','.join(['cats','rats','bats'])                          
Out[112]: 'cats,rats,bats'

### split()

//split string into a list of worlds //

> In [113]: 'My name is Simon'.split()                                
Out[113]: ['My', 'name', 'is', 'Simon']

*split by another character:*
> In [118]: 'My name is Simon'.split('m') 
Out[118]: ['My na', 'e is Si', 'on']

### ljust(), rjust(), center ()

*justify characters (left/right):*

> In [119]: 'Hello'.rjust(10)           
Out[119]: '   Hello'

*make string 10 characters long*

> In [122]: 'Hello'.rjust(15,'*')       
Out[122]: '**********Hello'
'''

In [123]: 'Hello'.center(20)            
Out[123]: '       Hello        '

In [124]: 'Hello'.center(20,'=')        
Out[124]: '=======Hello========'
'''

### strip (), lstrip(), rstrip()

*remove white space before/after the string*

'''
In [129]: aaa='Hello  '.rjust(10)       

In [130]: aaa       
Out[130]: '   Hello  '

In [131]: aaa.strip()                   
Out[131]: 'Hello'
'''

*it possible to remove not only empty space chacarter*
> In [132]: 'aadq324sflkf324kaf324'.strip('324')                                
Out[132]: 'aadq324sflkf324kaf'

### replace()

'''
In [133]: spam = 'Hello there!'         

In [134]: spam.replace('e','AAA')       
Out[134]: 'HAAAllo thAAArAAA!'
'''

## string formatting

*in the string you can use %s for variable and % (var1,var2) out*

'''
In [135]: name = 'Alex'                 

In [136]: age = 26  

In [137]: 'Hello %s, you are %s' % (name,age)                                   
Out[137]: 'Hello Alex, you are 26'
'''

# Running programs from the command line

*shebang line into the script:*
* windows : #! python3
* os x 	  : #! [/usr/bin/env](/usr/bin/env) python3
* linux   : #! /usr/bin/python3

*in windows cmd windows disappear quickly, you have to run pause.exe after the script, it can be done with batch script:*

> @py c:\hello.py %*
@pause

if you don't need a windows to see output:
  ''@pyw c:\hello.py %*''

### read arguments

> import sys
print('Hello %s' % sys.argv[2])
print(sys.argv)

# Regular expressions

* *regular expressions are mini-language for specifying text patterns. Writing code to do pattern matching without regula expression is a huge pain.*
* *regex strings often use \ backslashes (like \d), so they are often raw strings: r'\d'*
* *import the re module*
* *call the re.compile() function to create a regex object*
* *call the regex object's search() method to create a match object*
* *call the match object's group() method to get the matched string*
* *\d is the regex for a numeric digit character*

## regex groups and the pipe character

'''
In [183]: phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')       

In [184]: mo = phoneNumRegex.search('My number is 415-555-4242.')         

In [185]: mo.group()   
Out[185]: '415-555-4242'

In [186]: mo.group(1)  
Out[186]: '415'

In [187]: mo.group(2)  
Out[187]: '555-4242'
'''

## pipe

'''
In [188]: batRegex = re.compile(r'Bat(man|mobile|copter|bat)')            

In [189]: mo = batRegex.search('Batmobile lost a wheel')                  

In [190]: mo.group()                 
Out[190]: 'Batmobile'
'''

* groups are created in regex strings with parentheses
* the first set of parentheses is group 1, the second is 2, ..
* calling group() or group(0) returns the full matching string, group(1) returns group 1's matching string, and so on.
* use \( and \) to match literal parentheses in the regex string
* the | pipe can match one of many possible groups

## Repetition in Regex Patterns and Greedy/Nongreedy Matching

*matching a specific number of repetitions*

#### zero or one match

* (..)? 

'''
In [199]: import re                  

In [200]: batRegex = re.compile(r'Bat(wo)?man')                           

In [201]: mo = batRegex.search('The Adventures of Batman')                

In [202]: mo.group()                 
Out[202]: 'Batman'

In [203]: mo = batRegex.search('The Adventures of Batwoman')              

In [204]: mo.group()                 
Out[204]: 'Batwoman'
'''

#### zero or more match

* (..)*

'''
In [205]: batRegex = re.compile(r'Bat(wo)*man')                         

In [206]: mo = batRegex.search('The Adventures of Batwoman')            

In [207]: mo.group()                
Out[207]: 'Batwoman'

In [208]: mo = batRegex.search('The Adventures of Batwowowowoman')      

In [209]: mo.group()                
Out[209]: 'Batwowowowoman'
'''

### one or more match

* (..)+

### specific number of match

* (..){number}

### range of match

* (..){numberA,numberB}

### non greedy match

* match the shortest string possible - not default
* (..){number1,number2}?

'''
In [217]: digitRegex = re.compile(r'(\d){3,5}')                         

In [218]: digitRegex.search('1234567890')                               
Out[218]: <re.Match object; span=(0, 5), match='12345'>

In [219]: digitRegex = re.compile(r'(\d){3,5}?')                        

In [220]: digitRegex.search('1234567890')                               
Out[220]: <re.Match object; span=(0, 3), match='123'>
'''

## Regex Character Classes and the findall() method

| Shorthand character class | Represents                                                                                               |
|:--------------------------|:---------------------------------------------------------------------------------------------------------|
| \d                        | Any numeric digit from 0 to 9                                                                            |
| \D                        | Any character that is not a numeric digit from 0 to 9                                                    |
| \w                        | Any letter, numeric digit, or the undescore character. \n (Think of this as matching "word" characters.) |
| \W                        | Any character that is not a letter, numeric digit or \n the underscore character.                        |
| \s                        | Any space, tab, or newline character. \n (Think of this as matching "space" characters.)                 |
| \S                        | Any character that is nota a space, tab, or newline.                                                     |
| ^                         | makes a negative character class \n matching anything not in the brackets []                             |
|                           |                                                                                                          |

'''
In [15]: lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies danic
    ...: ng'           

In [16]: xmasRegex = re.compile(r'\d+\s\w+')  

In [17]: xmasRegex.findall(lyrics)            
Out[17]: ['12 drummers', '11 pipers', '10 lords', '9 ladies']
'''

### custom class regex

'''
In [18]: vowelRegex = re.compile(r'[aeiouAEIOU]') #the same of (a|o|i|..)                    

In [19]: vowelRegex.findall('Robocop eats baby food.')                                       
Out[19]: ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']

In [20]: doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')                                   

In [21]: vowelRegex.findall('Robocop eats baby food.')                                       
Out[21]: ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']

In [22]: doubleVowelRegex.findall('Robocop eats baby food.')                                 
Out[22]: ['ea', 'oo']

In [23]: consonantsRegex = re.compile(r'[^aeiouAEIOU]')                                      

In [24]: consonantsRegex.findall('Robocop eats baby food.')                                  
Out[24]: ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.']
'''

## Regex Dot-star and teh Caret/Dollar characters

## begins:

'''
In [1]: import re                                                                            

In [2]: beginsWhithHelloRegex = re.compile(r'^Hello')                                        

In [3]: beginsWhithHelloRegex.search('Hello there!')                                         
Out[3]: <re.Match object; span=(0, 5), match='Hello'>

In [4]: beginsWhithHelloRegex.search('He say: Hello there!')
'''

## ends:

'''
In [5]: endsWithWorld =re.compile(r'world!$')                                                

In [6]: endsWithWorld.search('Hello world!')                                                 
Out[6]: <re.Match object; span=(6, 12), match='world!'>

In [7]: endsWithWorld.search('Hello world again!')
'''

## exact string:

'''
In [8]: allDigits = re.compile(r'^\d+$')                                                     

In [9]: allDigits.search('33498573948534')                                                   
Out[9]: <re.Match object; span=(0, 14), match='33498573948534'>

In [10]: allDigits.search('334985a73948534')
'''

### anything except newline

### wildcard dot character (.)

'''
In [3]: atRegex = re.compile(r'.at')                                   
In [4]: atRegex.findall('The cat in the hat sat on the flat mat.')     
Out[4]: ['cat', 'hat', 'sat', 'lat', 'mat']

In [7]: atRegex = re.compile(r'.{1,2}at')                              

In [8]: atRegex.findall('The cat in the hat sat on the flat mat.')     
Out[8]: [' cat', ' hat', ' sat', 'flat', ' mat']
'''

### use:

'''
In [12]: nameRegex = re.compile(r'First Name (.*) Last Name: (.*)')    

In [13]: nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')   

In [14]: nameRegex.findall('First Name: Alex Last Name: Xelk dd')      
Out[14]: [('Alex', 'Xelk dd')]
'''

### greedy

'''
In [15]: strin = '<ljasdkl >asdkf>'                                    

In [16]: nongreedy = re.compile(r'<(.*?)>')                            

In [17]: nongreedy.findall(strin)                                      
Out[17]: ['ljasdkl ']

In [18]: ngreedy = re.compile(r'<(.*)>')                               

In [19]: ngreedy.findall(strin)                                        
Out[19]: ['ljasdkl >asdkf']
'''

## second argument to compile function

re.DOTALL  — match as match as possible
	''re.compile(r'.*',re.DOTALL)''

re.IGNORECASE  or re.I
   ''re.compile(r'[aeiou]',re.I)''

### recap:

* ^ the string must start with the pattern
* $ the string must end with the pattern
* ^abc$ the string abc match the pattern
* . (dot)  wildcard - matches anything except newlines

## Regex sub () Method and Verbose Mode

'''
In [1]: import re 

In [2]: namesRegex = re.compile(r'Agent \w+')                             

In [3]: namesRegex.findall('Agent Alice gave the secret documents to Agent
   ...:  Bob.')   
Out[3]: ['Agent Alice', 'Agent Bob']

In [4]: namesRegex.sub('REDACTED','Agent Alice gave the secret documents t
   ...: o Agent Bob.')               
Out[4]: 'REDACTED gave the secret documents to REDACTED.'

In [5]: namesRegex = re.compile(r'Agent (\w)\w*')                         

In [6]: namesRegex.findall('Agent Alice gave the secret documents to Agent
   ...:  Bob.')   
Out[6]: ['A', 'B']

In [7]: namesRegex = re.compile(r'Agent ((\w)\w*)')                       

In [8]: namesRegex.findall('Agent Alice gave the secret documents to Agent
   ...:  Bob.')   
Out[8]: [('Alice', 'A'), ('Bob', 'B')]

In [9]: namesRegex.sub(r'Agent \2****','Agent Alice gave the secret docume
   ...: nts to Agent Bob.')          
Out[9]: 'Agent A**** gave the secret documents to Agent B****.'
'''

### verbose

> In [10]: re.compile(r''' 
    ...: \d\d\d #area code 
    ...: -       #sdfsdf 
    ...: \d\d\d\d# last area code''',re.VERBOSE)                      
Out[10]: 
re.compile(r'\n\d\d\d #area code\n-       #sdfsdf\n\d\d\d\d# last area code',
re.UNICODE|re.VERBOSE)

### multiple options

> In [11]: re.compile(r''' 
    ...: \d\d\d #area code 
    ...: -       #sdfsdf 
    ...: \d\d\d\d# last area code''',re.VERBOSE | re.IGNORECASE | re.DOT
    ...: ALL )

*Recap:*
* *the sub() regex method : subsitute matches with some other text*
* *using \1,\2, ... will subsitute group 1,2 etc in the regex pattern*
* *passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile()*
* *if you want to pass multiple arguments, combine them with |*

## Regex Example Program: A phone and Email Scraper

*see phoneAndEmail.py*

# Files

## text file

helloFIle = open('/tmp/ciao')   — read mode

'''
In [1]: helloFile = open('/tmp/ciao')         

In [2]: helloFile.read()                      
Out[2]: 'ciao mondo!\nciao mondo!\nciao mondo!\nciao mondo!\nciao mondo!\n'

In [3]: helloFile.close()
> 

In [6]: helloFile.readlines()                 
Out[6]: 
['ciao mondo!\n',
 'ciao mondo!\n',
 'ciao mondo!\n',
 'ciao mondo!\n',
 'ciao mondo!\n']
'''

*Recap*
* *open () will return a file object which has reading and writing related methods*
* *pass 'r' (or nothing) to open() — read monde*
* *pass 'w' — write mode*
* *pass 'a' — append mode*
* *opening a nonexistant filename in write or append mode will create that file*
* *read () / write ()*
* *readlines() //
* //close() — when you are done with the file*
* *shelve module can store Python values in a binary file*
* *shelve.open()  — return a dictionary-like shelf value*

# Copying and moving files and folders

import shutil 

shutli.copy('aa','bb')
shutil.copytree()
shutil.move()
os.unlink() — will delete a file
os.rmdir() — will delete a folder (only if it empty)
send2trash.send2trash() — will send a file or folder to the recycling bin (import send2trash)

# Debugging

Raise your own excepions with try and except statements so that your program can recover from exceptions that your anticipated, but you can also raise your own exceptions in your code. 

'''
In [2]: import traceback                      

In [3]: try: 
   ...:     raise Exception('This is the error message.') 
   ...: except: 
   ...:     errorFile = open('erroInfo.txt','w') 
   ...:     errorFile.write(traceback.format_exc()) 
   ...:     errorFile.close() 
   ...:     print('The traceback info was written to errorInfo.txt.') 
   ...:                
The traceback info was written to errorInfo.txt.
'''

## Assertions

is a sanity check to make sure your code isn't doing something obviously wrong, these sanity checks are performed by assert statements. If the sanity checks fails, then an AssertionError exception is raised. In code, an assert statement consists of the following:
* the assert keywoard
* a condition
* a comma
* a string to display when the condition is False

An assert statement says, "I assert that this condition holds true and if not, there is a bug somewhere in the program." 
The code should not handle assert statements with try and except; if an assert fails, your progrm should crash. 
Assertations are for programmer errors, not user errors. For errors that can be recovered from (such as a file not being found or the user entering invalid data), raise an exceptio instead of detecting it with an assert statement.

*to run program without assertations "python -O myprogra.py"*

## Logging

**enable logging in your program with:**
> import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -%(message)s')

**print debug message**
> logging.debug('Start of program')

**disabling**
> logging.disable(logging.CRITICAL)--> disable all message of CRITICAL level and below --> disable all messages

**various levels of log**
* debug
* info
* warning
* error
* critical

**logging to a file**

> logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='
%(asctime)s - %(levelname)s - %(message)s')

# Web

*the requests moduile is a third-party module for downloading web pages and files*
*requests.get() returns a Response object*
*the raise_for_status() response method will raise an exception if the download failed*
*you can save a downloaded file to your hard drive with calls to the iter_content() method*

## Parsing HTML with the Beatiful Soup Module

> pip install beautifulsoup4
import bs4

* *web pages are plaintext files formatted as HTML*
* *HTML can be paresed with the BeautifulSoup module*
* *BeatifulSoup is imported with the name bs4*
* *pass teh string with the HTML to the bs4.BeautifulSoup() function to get a Soup object*
* *the soup object has a select() method that can be passed a string og the CSS selector for an HTML tag*
* *you can get a CSS selector string from the browser's developer tools by right-click the element and selecting Copy CSS Path*
* *the select() method will return a list of matching Element objects.*

## Controlling the browser with the Selenium module

*permit to run browser with python → run javascript/authontication/ecc → slow*

''pip install selenium''

'''
In [15]: browser = webdriver.Firefox()                                                                                                                                                      

In [16]: browser.get('https://automatetheboringstuff.com')                                                                                                                                  

In [17]: elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(                                                                                              
    ...: 19) > li:nth-child(1) > a:nth-child(1)')                                                                                                                                           

In [18]: elem.click()     

In [29]: searchElem = browser.find_element_by_class_name('gLFyf')                             

In [30]: searchElem.send_keys('ciao')          

In [31]: searchElem.send_keys('ciao darwin')   

In [32]: searchElem.send_keys('aaa')           

In [33]: searchElem.send_keys('adlajsd')       

In [34]: searchElem.submit()                   

In [35]: browser.back()

In [36]: browser.forward()                     

In [37]: browser.refresh()                     
^[[A
In [38]: browser.quit()
'''

* *to import selenium=, you need to run: from selenium import webdrivers*
* to open the browser, run: browser = webdriver.Firefox()
* to send the browser to a URL, run: beowser.get
* the browser.find_elements_by_css_selector() method will return a list of WebElement objects
* WebElement objects have a text variable that contains the element's HTML in a string
* the clic() method will clock on an element in the browser
* the send_key() method will type into a specific element in the browser
* the submit() method will simulate clicking on the Submit button for a form 
* the browser can also be controlled with these method: back(), forward(), refresh(), quit().

**https://selenium-python.readthedocs.org**
