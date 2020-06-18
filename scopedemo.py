def functionOne():
    print(globaVariable)#This variable is global (or will be when I declare it in a bit)
    localVariable="hello" #This variable is local to functionOne.  I can use it within the function
    print (localVariable)

def functionTwo(parameter): #The passed argument is local to the function
    print (parameter) #So I can use it here

globalVariable = 2 # This variable is declared outside any functions or loops - it can be used anywhere in the program
print (globalVariable) # So I can use it here.
print (localVariable) # However, localVariable is local to functionOne.  I can't use it outside functionOne
functionOne()
print (localVariable) # This still won't work.  Even though functionOne has been run, the variable doesn't exist outside of the function
functionTwo("function two variable")
