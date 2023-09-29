# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!

## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
   - _It's an concrete class. Since class MObject does not involve the use of the abc module to define abstract methods that must be implemented by subclasses. Class MObject does not have any abstract methods, nor does it inherit from an abstract base class._
1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
   - _The commented-out **del** method is a destructor in Python, executed when an object is about to be garbage collected._
1. What class does Texture inherit from?
   - _Texture inherit from class Image._
1. What methods and attributes does the Texture class inherit from 'Image'?

   - _Method: **init**(self, w, h): Constructor method to initialize a Texture object with width w and height h.
     getWidth(self): Returns the width of the texture.
     getHeight(self): Returns the height of the texture.
     getPixelColorR(self, x, y): Returns the red color value of the pixel at coordinates (x, y).
     getPixels(self): Returns the pixel values of the texture.
     setPixelsToRandomValue(self): Sets all pixel values to a random color._
     Attributes: m_width: Attribute to store the width of the texture.
     m_height: Attribute to store the height of the texture.
     m_colorChannels: Attribute to store the number of color channels (assumed to be 3 for RGB).
     m_Pixels: Attribute to store the pixel values of the texture.

1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
   - _I think texture should have a 'has_a' relationship with 'Image'. A Texture is not fundamentally a type of Image, but it can contain an Image or be derived from it. _
1. I did not declare a constructor for Texture. Does Python automatically create constructors for us?
   - _Yes, Python generates a default constructor, known as the **init** method, for a class when it's not defined explicitly. This default constructor requires no arguments and performs a basic task of initializing the object instance._

## Task 2 - Singleton

1. Refactor the singleton.py file such that:

- The first time the logger is constructed, it will print out:
  - `Logger created exactly once`
- If the logger is already initialized, it will print: - `logger already created`
  Note: You do not 'have' a constructor, but you construct the object in the _instance_ member function where you will create an object.  
  Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

_Singletons in Python do not come with built-in thread safety. Common implementations of the singleton pattern in Python do not naturally manage concurrent access by multiple threads. This can result in the creation of multiple instances when accessed concurrently in a multi-threaded environment._
