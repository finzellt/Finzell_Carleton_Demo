# Lists

In a previous assignment we looked at how to store and manipulate singular values as variables. The power of computers comes from being able to work with many (*many*) values. 

**Lists** are data structures[^1] that allow us to store multiple values in a single variable. To create an empty list, we use the syntax:

### Defining a List
```
my_list = []
```

We'll see plenty of those square brackets. 

We can store values in a list using code like the following:

```
my_list = [6,"pencil","t-shirt"]
```

Note that we can store multiple data types[^2] in a single list. 

### Accessing Elements in a List

To access **elements**--individual values--stored in the list we once again use the square brackets. Try running the following code:

```
my_list = [6,"pencil","t-shirt"]
print(my_list[1])
```

The number within the square brackets is called the **index**, and it's what allows us to fetch specific values in the list. 
*Note* that Python lists use *zero-indexing*, meaning that the first element in the list has the index 0. 


### Adding to a List

If we already have a list that's been defined and we want to add another value to it we can use the **`append`** function. For instance, if we wanted to add the value 17.282 to our list, it would look like the following (try running this code on your own):

```
my_list = [6,"pencil","t-shirt"]
my_list.append(17.282)
print(my_list)
```

### Additional List Functionality
For most of our class it will be sufficient to just define and `append` elements to a List. However, there are lots of other tools built into Lists that you *may* find useful. [This website](https://www.w3schools.com/python/python_lists.asp) gives a rundown of the different tools used in a list.


### Questions

1. What's an example of a list from everyday life?
2. Run the following bit of code:
```
my_list = [6,"pencil","t-shirt"]
print(my_list[5])
```
What error does this throw? What is the error code trying to tell you? What caused the error? How could you modify the code so that it no longer throws an error (without deleting or commenting any lines of code)?

### REMEMBER TO FILL OUT THE [PRE-CLASS SURVEY](https://forms.gle/wueUAtxJwUAZJXAfA)


[^1]: *Data structures are different kinds of containers that we use to store data. Lists are just one type of data structure, others include Dictionaries, Stacks, Queues, etc. You'll learn more about these in CS 201!*
[^2]: *See day 1 pre-class for more information on data types.*





