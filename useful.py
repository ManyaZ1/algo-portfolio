####strings,LISTS
#"string to letters"
string = "Geeksforgeeks"
letter = [x for x in string] 

def split(word):
    return list(word)
         
string = "geeks"
print([*string])

#"length of string"
a=len(nums) #nums is a List

a.sort()#sorts list a the object itself is changed
b=sorted(a)#b=a.sort(), a remains unsorted


#####DICTIONARIES
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

#sort dictionary by values
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2}

# Sort the dictionary by values in ascending order
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

##Appending to List in Python Dictionary
dict[sortedStr].append(string)
#Default Dic
from collections import defaultdict
  
  
# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"
      
# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
  
print(d["a"])
print(d["b"])#oytput 2
print(d["c"]) #output : nor present
#with defaultdict
"""def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        
        return list(anagram_map.values())"""

#leetcode problem
class Solution:
    def pancakeSort(self, arr):
        arr_sorted = sorted(arr, reverse = True)

        k_list = []
        for maxi in arr_sorted:
            k = arr.index(maxi) + 1 #max index+1
            k_list.append(k)

            arr = arr[:k][::-1] + arr[k:] #Αντιστροφή από 0 έως k(άρα, το max είναι στο index 0!)
            arr = arr[::-1] #Ολικό reverse(άρα κάναμε flip με k = lenght(arr). ΠΡΟΣΟΧΗ, όχι του αρχηκού arr, αλλά αυτού στο οποιό δουλεύουμε τώρα). Το max είναι στο index = -1.
            k_list.append(len(arr))
            arr.pop(-1) #Δεν μας νοιάζει πια αυτό το max, άρα δουλεύουμε σε υπολίστα!

        return k_list;
        
