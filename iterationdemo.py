
import random

print("I am an example of iteration")
print("Imagine I wanted to print out 'Hello' five times")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Not TOO bad, I suppose, especially with copy and paste.  But now imagine I wanted to print it out a billion times")
print ("Even with Copy and paste that would be a bit of a pain")
print("Or, even worse, imagine I wanted the user to type in a number and print 'hello' that many times")
print("I could try that with an elif")
print ("if(numberTheUserEntered==1):print('hello')elif(numberTheUserEntered==2:print('hello')print('hello')elif:...etc")
print("But that would be a pain")
print("Do I really want to type out a billion elif blocks?")
print("Iteration is about doing the same thing multiple times.  We're going to look at three (or maybe 2, depends on how you count them) ways of doing it")
print("First, the For loop repeats its tasks a certain number of time")
print("for x in range([start], stop, [step]):  Start and step are optional.  So we could just print something five times with 'for x in range(5):'")
for x in range(5): #colon, indent
    print("hello")
print("That loop starts a counter at zero and does the instructions then incremements the counter until it reaches five - it doesn't do it the fifth time")
print("Before you run the code, how many times do you think 'for x in range(3,5):' will print 'hello'? (Press any key to continue)")
input()
for x in range(3,5):
    print("hello")
print ("did you get it right?")
print ("the counter starts at 3, does the instructions.  It then goes to four, which is below five so it does the instructions.  It then goes to five"
       "which isn't below five, so it stops.")
print("what about 'for x in range (0,10,2):'?  Again, try to work it out before you run the code")
input()
for x in range (0,10,2):
    print("hello")
print("get it?  The counter starts at zero, but this time it goes up in 2s.  So 0,2,4,6,8 - five times.  We can see that more clearly if we print the counter")
for x in range(0,10,2):
    print("The counter is: " + str(x))
#to do While, For x in list
