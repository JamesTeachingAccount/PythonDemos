
import random

#Imagine I wanted to print out 'Hello' five times
#print ("Hello")
#print ("Hello")
#print ("Hello")
#print ("Hello")
#print ("Hello")
#Not TOO bad, I suppose, especially with copy and paste.  But now imagine I wanted to print it out a billion times
#Even with Copy and paste that would be a bit of a pain
#Or, even worse, imagine I wanted the user to type in a number and print 'hello' that many times
#I could try that with an elif
#if(numberTheUserEntered==1):
#    print('hello')
#elif(numberTheUserEntered==2:
#    print('hello')
#    print('hello')
#elif(...etc
#But that would be a pain
#Do I really want to type out a billion elif blocks?")
#Iteration is about doing the same thing multiple times.  We're going to look at three (or maybe 2, depends on how you count them) ways of doing it")
#First, the For loop repeats its tasks a certain number of time")
#for x in range([start], stop, [step]):  Start and step are optional.  So we could just print something five times with 'for x in range(5):'")
for x in range(5): #colon, indent
    print ("hello")
#That loop starts a counter at zero and does the instructions then incremements the counter until it reaches five - it doesn't do it the fifth time")
#Before you run the code, how many times do you think 'for x in range(3,5):' will print 'hello'?
for x in range(3,5):
    print ("hello")
print ("did you get it right?")
print ("the counter starts at 3, does the instructions.  It then goes to four, which is below five so it does the instructions.  It then goes to five"
       "which isn't below five, so it stops.")
#what about 'for x in range (0,10,2):'?  Again, try to work it out before you run the code")
input()
for x in range (0,10,2):
    print ("hello")
#get it?  The counter starts at zero, but this time it goes up in 2s.  So 0,2,4,6,8 - five times.  We can see that more clearly if we print the counter")
for x in range(0,10,2):
    print ("The counter is: " + str(x))
#The next type of iteration is iterating through a list.  This is a type of for loop (which is why I said 2 and a half before) but a special type")
#Quite often we want to do something to every item in a list.  I'm just going to set one up")
parts=["heads", "shoulders", "knees", "toes"]
#we can print out every item in the list like this:")
for x in parts: #colon, indent
    print(x)
#we can even indent things in other things:")
for x in parts:
    print(x)
    if (x=="knees"):#colon, indent
        print ("and")#which means we're now indented two steps
    #this comment is inside the for loop but not inside the if
#this comment is in neither
loopCounter = 0;
#Finally there's the while loop.  A for loop does something a certain number of times, a while loop does something so long as a condition is met")
#It works well with a Sheffield accent - 'Do this while the bus comes'")
#as you might be able to guess, there's colons and indenting.  It looks like this:")
while loopCounter<5:
    print ("I'm in a while loop")
    loopCounter+=1 #this means increment the loopCounter variable
#some other programming languages have other iteration operators - do/while, repeat/until, etc and JavaScript has a bunch of specialist ones")
#but those two/three are common to most languages and are all you actually need, if you learn how 'break' and 'continue' work")



