import math #Libraries are collections of extra commands in Python that do a specific job.  "Math", unsurprisingly, does a bunch of maths-type jobs
print(math.pi) #to access a command from a libray we can use libraryname.thingname - math.pi
import matplotlib as mpl#matplotlib is used fro drawing graphs and charts  Here we've used the "as" keyword which temporarily renames "matplotlib" to "mpl"
mpl.rcParams['lines.linewidth'] = 2 #I can now set the line width of my graphs to two, or do other matplotlib stuff, without typing out matplotlib every time
from PIL import Image #PIL is the Python Image Library.  It has a bunch of stuff to do with manipulatig images (there are also other image manipulation
#libraries such as pillow that many people think are better).  Here I've just imported a specific class, Image, from the library
im = Image.open("demo.jpg") #I can then use that class without referencing it - I don't need to write PIL.Image
from numpy import arange as rng #I can combine these things if I want.  Numpy has a lot of high level maths techniques - far beyond anything we'll do
#on this course! - here I'm importing the arange class from numpy and renaming it ar, which means I can go:
a = rng(15) # which means I can write this instead of a = numpy.arange(15)
#I can also do this:
from numpy import * # star means everything.  Never do this though, it "pollutes the global namespace".  There's a mars bar in it if you can explain to
#me what that means
