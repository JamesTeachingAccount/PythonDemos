import random

print("I am an example of selection")
print("The program will choose which statements to execute based on conditions")
print ("A simple 'if' statement will do an instruction if a condition is met")
firstRan = random.randint(1,10)
if (firstRan==10): #notice the colon at the end of this line and the indentation (one tab or four space, use the same each time) at the start of the next
    print("I just picked a random number.  You'll only see this line if it was a ten.  If it wasn't, this line doesn't appear")
print ("Adding an 'else' clause tot he 'if' statement will allow us to one thing if the condition is met and a different thing if it isn't")
secondRan = random.randint(1,10)
if (secondRan>5):
    print("I picked another random number.  You'l only see this message if it's above 5")
else: #again, colon, indentation.  Else doesn't need a condition though - it's condition is basically "the first one isn't met"
    print("I picked another random number.  You'l only see this message if it's 5 or below")
print("If we have many options, we can add 'elif' blocks.  These function the same as if blocks")
thirdRan=random.randint(1,10)
if (thirdRan==1):
    print("I picked yet another number.  You'll see this line if it was one")
elif (thirdRan==2):#colon, indentation
    print("I picked yet another number.  You'll see this line if it was two")
else:
    print("I picked yet another number.  You'll see this line if it neither one nor two")
    #the line below is too long for my screen so I've split it into two.  Each individual part is surrounded by "s but there's only one set of brackets
    print ("We can also have multiple lines inside an 'if', 'elif' or 'else'.  This line is in the else block so "#why is there a space after so?
           "will only appear if the number was neither one nor two, like the one above")
print ("So the order of instructions remains the same, like in sequence, but the computer makes a decision as to which line to use")
        
