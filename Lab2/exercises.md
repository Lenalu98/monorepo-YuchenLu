# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping)
   and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL.
   Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

_I think the name of the member functions correlate to what they do. The pop() method is currently used in Stack object and it means this method will pop the top item(which is added in the last as first-in-last-out stack strcuture) and also return this item, this method is correlate to its function. And when we use stack and it to return the top item of stack, the name of pop() is a good 'verbs'_

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

A dictionary is a collection of key-value pairs, where each key is unique and associated with a value. It is implemented as a hash table for efficient key-based lookups.
A list is an ordered collection of elements that allows duplicates. It is implemented as a dynamic array, allowing for efficient indexing and element manipulation.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

_Yes. You can access the any element in the list(the index must be valid)_

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.).
   What do you think are the pros/cons of a library that can work with any data type?

Pros of working with any data type:
Versatility, code reusability, abstraction.
Cons of working with any data type:
Potential for type-related errors, performance overheads, loss of type safety.

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
   Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

_The requests module in the Requests API documentation does follow good naming conventions for its functions. The function names are descriptive and typically use verbs that accurately represent the actions they perform._

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

_Most of funtions have proper number of arguments. But for request() function, it is a more generic function for making an HTTP request, does accept multiple arguments, but these are often necessary for configuring the request (e.g., method, url, params, data, headers, etc.). The argument count seems reasonable and aligns with the complexity of the HTTP request configuration._

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?

_'\*\*kwargs' means optional arguments that json.loads takes. It's useful for handling unexpected or optional arguments. However, overusing '\*\*kwargs' can lead to code complexity, potential confusion, and debugging challenges._

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text.
   Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

_1. Arguments set to None are optional, allowing for default behaviors when not provided. 2. Arguments without default values are mandatory for method calls. 3. Yes, arguments can have default values other than None. 4. Setting default values offers convenience and flexibility for users, enhancing API usability._
