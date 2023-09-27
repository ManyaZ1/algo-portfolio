#"string to letters"
string = "Geeksforgeeks"
letter = [x for x in string] 

def split(word):
    return list(word)
         
string = "geeks"
print([*string])

#"length of string"
a=len(nums) #nums is a List

#Check whether given Key already exists in a Python Dictionary
#if key in dic.keys():
#if key in dic:

#FROM LIST TO DICTIONARY
    keys = ['apple', 'banana', 'orange']
values = [3, 6, 4]

# zip the two lists together to create a list of key-value pairs
key_value_pairs = zip(keys, values)

# convert the list of key-value pairs to a dictionary
my_dict = dict(key_value_pairs)
