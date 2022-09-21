#!/usr/bin/env python
# coding: utf-8
1. Square brackets are lists while parentheses are tuples.
2. Generator - A process that is repeated more than one time by applying the same logic is called an Iteration.  In programming languages like python, a loop is created with few conditions to perform iteration till it exceeds the limit. If the loop is executed 6 times continuously, then we could say the particular block has iterated 6 times. 
Iterator - An iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, tuples, sets, etc. Iterators are implemented using a class and a local variable for iterating is not required here, It follows lazy evaluation where the evaluation of the expression will be on hold and stored in the memory until the item is called specifically which helps us to avoid repeated evaluation. As lazy evaluation is implemented, it requires only 1 memory location to process the value and when we are using a large dataset then, wastage of RAM space will be reduced the need to load the entire dataset at the same time will not be there.

Using an iterator-

iter() keyword is used to create an iterator containing an iterable object.
next() keyword is used to call the next element in the iterable object.
After the iterable object is completed, to use them again reassign them to the same object.
3. If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. Both yield and return will return some value from a function.

4. The yield statement returns a generator object to the one who calls the function which contains yield, instead of simply returning a value.
5. List comprehension is more concise and easier to read as compared to map. List comprehension are used when a list of results is required as map only returns a map object and does not return any list. Map is faster in case of calling an already defined function (as no lambda is required).