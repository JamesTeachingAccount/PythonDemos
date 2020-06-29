def functionOne():
    print(globaVariable)#This variable is global (or will be when I declare it in a bit)
    localVariable="hello" #This variable is local to functionOne.  I can use it within the function
    print (localVariable)

def functionTwo(parameter): #The passed argument is local to the function
    print (parameter) #So I can use it here

def functionThree():
    globalNumericVariable = globalNumericVariable + 2 #ERROR!  I can access the global variable, but I can't modify it
    #Specifically what has happened is that a new variable called globalNumericVariable has been created that is, despite the name, local to the function
    #I then tried to add two to it, which caused an error as Python didn't know what's value was.
    global globalNumericValue #now I've given myself access to the global variable and the lines:
    globalNumericVariable = globalNumericVariable + 2
    print(globalNumericVariable)
    #will work as expected
    #I NEVER want to see you use global.  It's on the spec, you need to know about it, but its bad practice.  Don't do it.  LEarn it for the exam then
    #immediately forget about it.  NEVER use it

globalVariable = 2 # This variable is declared outside any functions or loops - it can be used anywhere in the program
print (globalVariable) # So I can use it here.
print (localVariable) # However, localVariable is local to functionOne.  I can't use it outside functionOne
functionOne()
print (localVariable) # This still won't work.  Even though functionOne has been run, the variable doesn't exist outside of the function
functionTwo("function two variable")
globalNumericVariable = 2 #Again, global because it's referenced outside of a function
functionThree()
