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
