def printHello(): #this function doesn't take any arguments.  We still need the brackets though.  Note the colon and indent
    """Prints the words "Hello World" to standard output"""  #EVERY Python function needs a docstring.  Its a description of what the function does
    #Python will compile without a docstring, but you will fail the course.  Yes, every function
    print("Hello World")
    return True #Every function should send something back.  As there's no useful information to send back here, I'm just sending "True" to say "yes, that
    #function happened"  Again, Python will be happy without a return statement but you won't be because you'll fail

def addTwoNumbers(x, y):#this functoin takes two arguments, that I am calling x and y
    """Prints the sum of two numbers

    Keyword Arguments:
    x - the first number
    y - the second number
    """ #This is a multiine docstring.  It says what the function does and what arguments it takes
    print(str(x+y))
    return x+y #some useful information to send back here

def raiseToPower(base, index=2):#This takes one argument and one optional argument.  If two are provided, that's fine.  If only one, the secodn will default to 2
    """Prints the value of a number raised to a power

    Keyword Arguments:
    base - the base number
    index - the power to raise base to (default 2)
    """
    print (str(base**index))
    return base**index

#I call a function by writing it's name then brackets
printHello()
#I can store the return value of a function in a variable
resultsFromHello = printHello()
print(resultsFromHello)
#If the function takes arguments I provide them inside the brackets
addTwoNumbers(3,5)
#I can also pass it variables
firstNumber = 2
secondNumber = 3
addTwoNumbers(2,3)
#Or even the output of other functions
raiseToPower(2,addTwoNumbers(2,3)) #We start with the innermost pair of brackets.  So do addTwoNumbers(2,3), that returns 5.  Then do raiseToPower(2,5)
#Despite the fact I said compiled earlier, Python is actually an interpreted language.  That means we need to define the functions BEFORE I call them.
#If I shifted raiseToPower down to after this line, my program wouldn't work properly

