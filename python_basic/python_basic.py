def function():
    print("hello world")


function()

message = "hahahh"
print(message)

if 5 > 2:
    print("5 is larger than 2")
else:
    print("error")


"""
multi line comments 
written more than one line
"""

"""
variable
"""
x = 5
y = "Robin"
print(x)
print(y)

"""
python string, you could visit character directly
"""
print(y[1])

"""
loop the string
"""
for c in "banana":
    print(c)

"""
len() is used to get the length of string
"""
print(len(y))

"""
in & not in 
"""
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("correct")

"""
slicing string
"""
string = "hello test"
sliced_string = string[2: 3]
print(sliced_string)

"""
remove whitespace
"""
a = " hello world, xxx "
print(a.strip())

"""
replace() method a string with another string, you need one variable to get it
split() -> return type is a list
"""
b = a.replace("h", "H")
print(b)

"""
bool, True, False
"""

"""
order will not change in a list, allow duplicates
append(), insert()
pop(): if not specified, remove last element
del list[0]: delete specific element in list


loop list through index :
for i in range(len(list)):
    print(list[i])
"""

this_list = ["apple", "banana", "cherry"]
print(this_list)
print(len(this_list))


"""
sort(), list.sort() by default, it will sort by alphanumerically 
sort(reverse = True) 
list.reverse() means reverse the order 
"""

"""
copy a list
.copy(), list() : two ways to copy 
"""


"""
tuple -> unchangable 
('a', 'b', 'c')
"""

"""
set
myset = {"apple", "banana", "cherry"}
set is also unchangeable
to add one item in set, using add() method 
"""

"""
dictionaries: {"key": "value"}
keys() will return a list of keys 
values() method will return a list of all values in the dictionary
items() will return each item in a dictionary in a tuple value
"""

my_dictionaries = {"name":"robin", "age": 23, "happy": False}
for key, val in my_dictionaries.items():
    print(key + " is and value is " + str(val))


"""
if 
elif
else

print(a) if a > b else print(b)

and , or, not 

pass, continue 
"""

"""
def: a python function is defined by a def keyword 
"""

def iterate_list(my_list):
    for x in my_list:
        print(x)
    return 0
my_list = ['a', 'b', 'c']
result = iterate_list(my_list)
print(result)

"""
sorted(data, key = lambda x: (x[1], -x[0]))
"""