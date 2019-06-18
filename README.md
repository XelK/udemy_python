Content-Type: text/x-zim-wiki
Wiki-Format: zim 0.4
Creation-Date: 2019-06-16T14:09:48+02:00

# Python

Created Sunday 16 June 2019

contain  notes/examples of Udemy course   "Automate the Boring Stuff with Python Programming"

https://www.udemy.com/automate/

# Book

Automating the boring stuff with python

Al Sweigard

https://automatetheboringstuff.com.

opensource book/printable/available on amazon

--------------------

# Expressions

*all expressions are just value and operators*
* value: 2 , 5 , 39204
* operators: + , - , *, ...

# Data Types

*all data belong to types*
* integer
* float
* string

# Variables

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

# Flow Charts

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

//need to have //**xsel **installed

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

'''
	def plusOne (number) :
	    return number + 1
	'''

#### the non-value

*the //**None*** value the none type //
*every function return value, ever the //**print ***function.  If  the function not have the return statement, the returned value is None//

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

# Try and Except Statements

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
