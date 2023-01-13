# # Write a program to find the length of the string without using inbuilt function (len)
#
# string = "hello world"
# count = 0
#
# for char in string:
#     count += 1
#
# print(count)

###############################################################################################################
# # Write a program to reverse a string without using any inbuilt functions.
#
# string = "hello world"
#
# # slicing
# print(string[::-1])
#
# # concatenation
# reversed_string = ""
# for char in string:
#     reversed_string = char + reversed_string
#
# print(reversed_string)
#
# # reversed() class
# rev = reversed(string)      # reversed object --> iterator object
# print(rev)
#
# # traversing through reversed object
# for item in rev:
#     print(item, end="")
#
# print()
# # type casting
# rev = reversed(string)
# rev_1 = tuple(rev)
# print(rev_1)
# print("".join(rev_1))
#
# # reverse() - list
# list_ = list(string)
# list_.reverse()
# rev_2 = "".join(list_)
# print(rev_2)
#
# #############################################################################################################
# # Write a program to replace one string with another. e.g. "Hello World" replaces "World" with "Universe"
#
# string = "hello world world"
# old_word = "world"
# new_word = "universe"
#
# # using replace()
# print(string.replace("world", "universe", 1))
#
# # without inbuilt methods
# words = string.split()      # [hello, world, world]
# rep_str = ""
#
# for word in words:
#     if word == old_word:
#         rep_str += new_word + " "
#     else:
#         rep_str += word + " "
#
# print(rep_str)
#
# # replacing specific number of occurrences
# words = string.split()      # [hello, world, world]
# rep_str = ""
# count = 0
#
# for word in words:
#     if word == old_word and count < 1:
#         rep_str += new_word + " "
#         count += 1
#     else:
#         rep_str += word + " "
#
# print(rep_str)

#############################################################################################################
# # 4. How to convert a string to a list and vice-versa.
#
# string = "hello"
#
# # split()
# list_ = string.split()          # ["hello"]
# print(" ".join(list_))
#
# # list()
# list_ = list(string)            # [h, e, l , l, o]
# print("".join(list_))

# ################################################################################################################
# # 5. Convert the string "Hello welcome to Python" to a comma separated string.
#
# string = "Hello welcome to Python"
#
# # replace()
# print(string.replace(" ", ","))
#
# # without inbuilt()
# res = ""
# for char in string:
#     if char == " ":
#         res += ","
#     else:
#         res += char
# print(res)
#
# # join()
# list_ = string.split()
# print(",".join(list_))
#
# # re
# import re
# print(re.sub(" ", ",", string))
#
# ############################################################################################################
# # 6. Write a program to print alternate characters in a string.
#
# string = "hello"
# print(string[::2])      # even indexed chars
# print(string[1::2])     # odd indexed chars
#
# # range()
# for i in range(len(string)):
#     if i % 2 == 0:          # if i % 2:
#         print(string[i], end=" ")       # even indexed chars
#
# print()
# # enumerate()
# for index, char in enumerate(string):
#     if index % 2 == 0:
#         print(char, end=" ")

# ##########################################################################################################
# # 7. Write a Program to print ascii values of the characters present in a string.
#
# string = "hello"
#
# for char in string:
#     print(ord(char))

# ##############################################################################################################
# # 8. Write a function to convert upper case to lower case and vice-versa without using inbuilt methods.
#
# string = "HElLo WorlD"
#
#
# # using inbuilt methods
# def lower_upper(a: str) -> str:
#     res = ""
#
#     for char in a:
#         if char.islower():
#             res += char.upper()
#
#         elif char.isupper():
#             res += char.lower()
#
#         else:
#             res += char
#     return res
#
#
# print(lower_upper(string))
#
#
# # swapcase()
# def swapping(s: str) -> str:
#     return s.swapcase()
#
#
# print(swapping(string))
#
#
# # without inbuilt methods
# def swap_case(a: str) -> str:
#     res = ""
#
#     for char in a:
#         if ord("a") <= ord(char) <= ord("z"):
#             res += chr(ord(char)-32)
#
#         elif ord("A") <= ord(char) <= ord("Z"):
#             res += chr(ord(char)+32)
#
#         else:
#             res += char
#
#     return res
#
#
# print(swap_case(string))
#
# ###########################################################################################
# # 9. Write a program to swap two numbers without using the 3rd variable.
#
# a = 10
# b = 20
#
# a, b = b, a
#
# # using 3rd variable
# temp = a
# a = b
# b = temp
#
# #########################################################################################
# # 10. Write a program to merge two different lists.
#
# list_1 = [1, 2, 3]
# list_2 = [2, 3, 4, 5]
#
# # packing and unpacking
# print(*list_1, *list_2)
#
# res = [*list_1, *list_2]
# print(res)
#
# # concatenation
# res = list_1 + list_2
# print(res)
#
# # inbuilt methods
# list_1.extend(list_2)
# print(list_1)
#
# ##########################################################################################
# # 11. Write a program to read a random line in a file. (ex. 50, 65, 78th line)
#
# path = r"C:\Users\Vidyashree M C\PycharmProjects\selenium_RMG_09\files\sample.log"
# n = 7
#
# # count variable
# with open(path) as file:        # file --> iterator object
#     count = 0
#
#     for line in file:
#         count += 1
#         if count == n:
#             print(line)
#             break
#
# # enumerate()
# with open(path) as file:
#     for line_no, line in enumerate(file, start=1):
#         if line_no == n:
#             print(line)
#             break
#
# # islice()
# from itertools import islice
#
# with open(path) as file:
#     lines = islice(file, n-1, n)
#
#     for line in lines:
#         print(line)
# ##########################################################################################
# # extract the messages from sample.log
# path = r"C:\Users\Vidyashree M C\PycharmProjects\selenium_RMG_09\files\sample.log"
#
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             words = line.split()
#             print(words[2])
#
# #########################################################################################
# # 12. Write a program to read random lines in a file. (ex. I want read all lines 10th to 15th line)
#
# path = r"C:\Users\Vidyashree M C\PycharmProjects\selenium_RMG_09\files\sample.log"
#
#
# # count variable
# def read_n_lines(start, end):
#     with open(path) as file:
#
#         count = 0
#         for line in file:
#             count += 1
#             if line.strip():
#                 if start <= count <= end:
#                     print(line)
#
#
# # read_n_lines(3, 7)
#
# # enumerate()
# def read_lines(start, end):
#     with open(path) as file:
#         for line_no, line in enumerate(file, start=1):
#
#             if start <= line_no <= end:
#                 if line.strip():
#                     print(line)
#
#
# # read_lines(3, 7)
#
# # islice()
# from itertools import islice
#
# def read_islice(start, end):
#     with open(path) as file:
#
#         lines = islice(file, start-1, end)
#
#         for line in lines:
#             if line.strip():
#                 print(line)
#
# read_islice(3, 7)

########################################################################################################
"""
1. Printing the line with line numbers
2. Reading the file in reversed order
3. Finding the length of each line in the text file
4. Extracting IP addresses from log file.
5. Counting number of occurrences of ip addresses in the log file.
6. Extracting Messages from sample.log
7. Counting Number of INFO, WARN, TRACE Messages.
8. Reading Countries from football.txt
9. Least and Most occurrences of the word
10. Counting total number of words present in a file
11. Finding the line no of a particular word in a file.
12. Printing 4 to 7th lines
13. Printing nth line in a file
14. Printing last n lines in a file
15. WAP to check if the file has even number of lines
16. WAP to print only the lines which are starting with vowels
17. WAP to count all the lowercase and uppercase letters in the file
18. WAP to create a dictionary with vowels and their count pair.
# """
# ###########################################################################################
# # 28 Find the longest word in the sentence**
#
# sentence = "Hello world. Welcome to Python"
#
# # sorted()
# words = sentence.split()
# res = sorted(words, key=len)
# print(res[-1])
#
# # max()
# words = sentence.split()
# res = max(words, key=len)
# print(res)
#
# # without inbuilt methods/functions
# words = sentence.split()
# res = ""
#
# for word in words:
#     if len(res) < len(word):
#         res = word
# print(res)
#
# # bubble sort
# sentence = "Hello world. Welcome to Python"
# """
# i = 0,  [world. , Hello, Welcome, to, Python]
# i = 1,  [world., Welcome, Hello, to, Python]
# i = 2,  [world., Welcome, Hello, to, Python]
# i = 3,  [world., Welcome, Hello, Python, to]
# """
# words = sentence.split()
#
# for _ in range(len(words)-1):
#     for i in range(len(words)-1):
#         if len(words[i]) > len(words[i+1]):
#             words[i], words[i+1] = words[i+1], words[i]
#
# print(words[0], words[-1])

############################################################################################
# 29 write a program to reverse the values in the dictionary if the value is of type String**
# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'world'}

# # traversing through keys
# for key in d:
#     value = d[key]
#     if isinstance(value, str):
#         d[key] = value[::-1]           # d[key] = value
#
# print(d)

# # traversing through items
#
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
#
# print(d)

# #######################################################################################
# # 30 write a program to get 1234 from the below tuple
#
# t = ('1', '2', '3', '4')
#
# # join()
#
# res = "".join(t)
# print(res)
#
# # concatenation
# res = ""
# for item in t:
#     res += item
#
# print(res)
#
# ######################################################################################
# # 31 How to get the elements that are in list b but not in list a**
# a = [1, 2, 3]
# b = [1, 2, 3, 4]
#
# # set.difference()
#
# print(set(b).difference(set(a)))
#
# # for loop
#
# for item in b:
#     if item not in a:
#         print(item)
#
#
# # finding the longest list
#
# if len(a) > len(b):
#     longest, smallest = a, b
# else:
#     longest, smallest = b, a
#
# for item in longest:
#     if item not in smallest:
#         print(item)
#
# #########################################################################################
# # 32 A function takes variable number of positional arguments as input. How to check if the arguments that are passed are more than 5
# def spam(*args):
#     return len(args) > 5
#
#
# print(spam(1, 2, 3, 4, 5))
#
# ##########################################################################################
# # 33 Count the number of occurrences of "CRITICAL", "INFO" and "ERROR" lines in a log file.**
#
# # Assume Below is the contents of the log file
#
# lines = """CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical
# CRITICAL:Hello world
# INFO: This is an info
# ERROR: This is an error
# CRITICAL: This is critical"""
#
# # count variable
# file = lines.split("\n")
# critical_count = 0
# info_count = 0
# error_count = 0
#
# for line in file:
#     words = line.split(":")
#     if words[0] == "CRITICAL":
#         critical_count += 1
#
#     elif words[0] == "INFO":
#         info_count += 1
#
#     elif words[0] == "ERROR":
#         error_count += 1
#
# print(critical_count, info_count, error_count)
#
# # dictionary
# file = lines.split("\n")
# d = {}         # {"CRITICAL" : 2}
#
# for line in file:
#     words = line.split(":")
#
#     if words[0] not in d:
#         d[words[0]] = 1
#     else:
#         d[words[0]] += 1
#
# print(d)
#
# # default dictionary
# from collections import defaultdict
#
# d = defaultdict(int)
# file = lines.split("\n")
#
# for line in file:
#     words = line.split(":")
#     d[words[0]] += 1        # d[words[0]] = d[words[0]] + 1
#
# # Counter
# from collections import Counter
# msgs = []
#
# for line in file:
#     words = line.split(":")
#     msgs.append(words[0])
#
# c = Counter(msgs)           # counter object
# print(c)
# print(c.most_common())      # list of tuples
# print(c.most_common(n))     # n number of most common elements
#
# ##########################################################################################
# # 13 Program to print the last "N" lines of a file.
# from itertools import islice
#
# path = r"C:\Users\Vidyashree M C\PycharmProjects\selenium_RMG_09\files\sample.log"
# n = 3
#
# # islice()
# with open(path) as file:
#     len_file = 0
#
#     for _ in file:
#         len_file += 1
#     print(len_file)
#
#     print(file.tell())
#     file.seek(0)
#     print(file.tell())
#
#     lines = islice(file, len_file-n, len_file)
#
#     for line in lines:
#         print(line)
#
# # deque()
# from collections import deque
#
# with open(path) as file:
#     lines = deque(file, n)
#
#     for line in lines:
#         print(line)
import re

"""
from collections import deque
l = [12, 3, 5, 6, 19, 87, 100]

l1 =  deque(l)
l1
deque([12, 3, 5, 6, 19, 87, 100])

l1.append(10)
l1
deque([12, 3, 5, 6, 19, 87, 100, 10])

l1.appendleft(16)
l1
deque([16, 12, 3, 5, 6, 19, 87, 100, 10])

l1.pop()
10
l1.popleft()
16
l1
deque([12, 3, 5, 6, 19, 87, 100])

l1.rotate()
l1
deque([100, 12, 3, 5, 6, 19, 87])

l1.rotate(2)
l1
deque([19, 87, 100, 12, 3, 5, 6])

l = [12, 3, 5, 6, 19, 87, 100]

l1 = deque(l)
l1
deque([12, 3, 5, 6, 19, 87, 100])

l1 = deque(l, 3)
l1
deque([19, 87, 100], maxlen=3)
"""
#
# ###########################################################################################
# # 15 Write a program to search for a character in a given string and return the corresponding index.
#
# s = "hello world"
#
# # index() or find()
# def linear_search(string: str, char: str):
#
#     for ch in string:
#         if ch == char:
#             print(f"the index of {char} is: {string.index(char)}")
#             break
#
#     else:
#         print("character is not present in the string")
#
#
# # linear_search(s, "o")
#
# # method 2 - try and except with index()
# char = "e"
#
# try:
#     print(s.index(char))
#
# except ValueError as message:
#     print(message)
#
#
# # find()
#
# char = "e"
#
# index = s.find(char)
#
# if index != -1:
#     print(f"the index of {char} is: {index}")
#
# else:
#     print("char is not present")
#
# # range()
#
# string = "hello"
# char = "l"
#
# for i in range(len(string)):
#     if char == string[i]:
#         print(f"the index of {char} is: {i}")
#         break
#
# else:
#     print("character is not present")
#
# # enumerate()
#
# string = "hello"
# char = "x"
#
# for index, ch in enumerate(string):
#     if char == ch:
#         print(f"the index of {char} is: {index}")
#         break
#
# else:
#     print("character is not present in the string")
#
# # re
# import re
#
# string = "hello world"
#
# # findall()
# print(re.findall("o", string))
# print()
#
# # finditer()
# res = re.finditer("o", string)
# # print(res)
#
# for match in res:
#     print(match)
#     print(match.start(), match.end())
#     print(match.group())
# print()
#
# # search()
# res = re.search("o", string)
# print(res.start(), res.end(), res.group())
#
# # match()
# string = "hello world"
#
# res = re.match("ll", string)
# print(res)

############################################################################################
# 21 Write a class named Simple and it should have iteration capability.


# class Simple:
#
#     def __init__(self, iterable):
#         self.iterable = iterable
#
#     def __iter__(self):     # --> iterator object
#         return iter(self.iterable)
#
#
# s = Simple("hello")
#
# for i in s:     # iter
#     print(i)

"""
# iterator protocol
s = "hello"

for i in s:
    print(i)
    
    
x = iter(s)     # s.__iter__()
while True:
    try:
        i = next(x)     # x.__next__()
    
    except StopIteration:
        break
    
    else:
        print(i)
"""
#######################################################################################
# 22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a

# points = dict({"a": 1, "b": 2})        # class dict
#
# # print(d["a"])      # 1 --> getitem
# # print(d.a)         # 1
#
#
# class Demo:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __getitem__(self, item):
#         return self.__dict__[item]
#
#
# d = Demo(1, 2)
# print(d.a)      # __getattribute__ --> searches for the attribute in the instance dictionary
# print(d.__getattribute__("a"))
# print(d.__dict__)
# print(d["a"])
#
# # method 2
#
# class Demo:
#
#     def __init__(self, dict_):
#         self.d = dict_
#
#     def __getitem__(self, item):
#         return self.d[item]
#
#     def __getattribute__(self, item):
#         return super().__getattribute__(item)
#
#     def __getattr__(self, item):
#         return self.d[item]
#
#
# points = dict({"a": 1, "b": 2})
# d1 = Demo(points)
# print(d1.__dict__)      # {'d': {'a': 1, 'b': 2}}
# print(d1.a)             # __getattribute__
# print(d1["a"])          # __getitem__

######################################################################################################
# __getattr__, __getattribute__

# class Spam:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __getattribute__(self, item):
#         return super().__getattribute__(item)
#
#     def __getattr__(self, item):
#         return "value is not present"
#
#
# s = Spam("vidya")
# print(s.salary)

#############################################################################################################
# 35 Write a function to print the below output.**
# func("TRACXN", 0)  # Should print RCN
# func("TRACXN", 1)  # Should print TAX

#
# def func(string, num):
#     if num == 0:
#         return string[1::2]
#     elif num == 1:
#         return string[::2]
#     else:
#         return "invalid option"
#
#
# print(func("TRACXN", 0))
# print(func("TRACXN", 1))

#######################################################################################
# # 36 Sum all the numbers in the below string.**
#
# s = "Sony12India567Pvt2ltd" # eg.1+2+5+6+7+2
#
# # using isdigit(), sum()
# nums = []
# for char in s:
#     if char.isdigit():
#         nums.append(int(char))
#
# print(sum(nums))
#
# # without inbuilt functions
# total = 0
# for char in s:
#     if ord("0") <= ord(char) <= ord("9"):
#         total += int(char)
#
# print(total)
#
# # using re
# import re
#
# s = "Sony12India567Pvt2ltd"
#
# pattern = r"\d"
# nums = re.findall(pattern, s)
# print(nums)
#
# total = 0
# for num in nums:
#     total += int(num)
#
# print(total)

#####################################################################################
# # 37 Write a program to sum all the numbers in below string.**
# s = "Sony12India567Pvt2ltd"     # eg.12 + 567 + 2
#
# import re
#
# pattern = r"\d+"        # r"[0-9]+"
# nums = re.findall(pattern, s)
# print(nums)
#
# total = 0
# for num in nums:
#     total += int(num)
#
# print(total)

######################################################################################
# 38 Print all the numbers in the below list**

# a = ['abc', '123', 'hello', '23']
#
# # using isdigit() or isalnum()
# for item in a:
#     if item.isdigit():      # if item.isalnum():
#         print(item)

########################################################################################
# # 39 Program to print the number of occurrences of characters in a String without using inbuilt functions.**
# s = 'helloworld'
#
# # normal dictionary
# d = {}
#
# for char in s:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
#
# print(d)
#
# # default dictionary
# from collections import defaultdict
#
# dd = defaultdict(int)
#
# for char in s:                  # "h"
#     dd[char] = dd[char] + 1     # dd["h"] = dd["h"] + 1
#                                 # dd["h"] = 0 + 1
# print(dd)
#
# # count()
# s = 'helloworld'
# set_ = set(s)
# print(set_)
#
#
# d = {}
#
# for char in set_:                               # no of iterations = 7
#     d[char] = s.count(char)
#
# # comprehension
# d = {char: s.count(char) for char in s}         # no of iterations = 10
#
# """
# s = 'helloworld'
#
# char                        d
# --------------------------------
# h                           {h: 1}
# e                           {h: 1, e: 1}
# l                           {h: 1, e: 1, l: 3}
# l                           {h: 1, e: 1, l: 3}
#
# """
#
# # Counter()
# from collections import Counter
#
# res = Counter(s)
# print(dict(res))

#########################################################################################
# 40 Program to print only the repeated characters and count of the same.**
# s = 'helloworld'
#
# d = {}
#
# for char in s:
#     if s.count(char) > 1:
#         if char not in d:
#             d[char] = 1
#         else:
#             d[char] += 1

# print(d)

############################################################################################
# 41 Write a program to get alternate characters of a string in list format.**
# s = 'helloworld'
#
# # slicing
# res = s[::2]
# print(list(res))
#
# # concatenation
# res = []
# for index, char in enumerate(s):
#     if index % 2 == 0:
#         res.append(char)
# print(res)

#########################################################################################
# 42 Write a program to get square of list of number's using lambda function .**
# a = [1, 2, 3, 4, 5]
#
# squares = lambda num: num ** 2
#
# # for loop
# res = []
# for item in a:
#     res.append(squares(item))
#
# print(res)
#
# # comprehension
# res = [squares(item) for item in a]
# print(res)
#
# # map()
# res = list(map(squares, a))
# print(res)

###########################################################################################
# 43 Write a function that accepts two strings and returns True if the two strings are anagrams of each other.

# def check_anagram(string1, string2):
#     return sorted(string1) == sorted(string2)
#
#
# print(check_anagram("fare", "fear"))
# print(check_anagram("faree", "fear"))
# print(check_anagram("faar", "fear"))

#############################################################################################
# 44 Write a program to iterate through list and build a new list, only if the items of the list has even number of characters.**
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
#
# # method 1
#
# res = [name for name in names if len(name) % 2 == 0]
# print(res)
#
# # method 2 - filter()
#
# def even_len(string):
#     return len(string) % 2 == 0
#
#
# print(list(map(even_len, names)))
# print(list(filter(even_len, names)))

##########################################################################################
# 45 Write a program to iterate through list and build a new dictionary, only if the items of the list has even number of characters.**
# names = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
#
# # normal method
# d = {}
#
# for name in names:
#     if len(name) % 2 == 0:
#         d[name] = len(name)
#
# print(d)
#
# # comprehension
# d = {name: len(name) for name in names if len(name) % 2 == 0}
# print(d)
#
# # len: word pair
# d = {}
#
# for name in names:
#     if len(name) not in d:
#         d[len(name)] = [name]
#     else:
#         d[len(name)] += [name]
#
# print(d)
#
# # default dict
# from collections import defaultdict
#
# dd = defaultdict(list)
#
# for name in names:
#     dd[len(name)] += [name]
#
# print(dd)

#############################################################################################
# 47 Count number of lines in a file without loading the file to the memory

# path = r"./files/example.txt"
#
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
# print(count)

##########################################################################################
# # 48 Printing line and line no's in a file
# path = r"./files/example.txt"
#
# with open(path) as file:
#
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, line, sep=" - ")

##############################################################################################
# 49 Write a Program to print the sum of entire list and sum of only internal list**

# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# # without in built functions
# total_sum = 0
#
# for item in l:      # [1, 2, 3]
#     internal_sum = 0
#
#     for ele in item:    # 1
#         internal_sum += ele
#
#     print(internal_sum)
#     total_sum += internal_sum
#
# print(total_sum)
#
# # sum()
# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# internal_sum = []
#
# for item in l:
#     internal_sum.append(sum(item))
#
# print(internal_sum)
# print(sum(internal_sum))

###################################################################################
# 50 Write a program to reverse the list as below**
# >>> res = ["python", "hello", "hi"]

# words = ["hi", "hello", "python"]
#
# # slicing
# res = words[::-1]
# print(res)
#
# # reversed class
# res = list(reversed(words))
# print(res)
#
# # concatenation
# res = []
# for word in words:
#     res = [word] + res
#
# print(res)

#########################################################################################
# 51 Write a program to update the tuple
# o/p (1, 2, 3, 4, 100, 200, 300)

"""
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [*l1, *l2]
l3
[1, 2, 3, 4, 5, 6]
l1 = [1, 2, 3]l2 = [4, 5, 6]
SyntaxError: invalid syntax
l1 = [1, 2, 3]
l2 = (4, 5, 6)
l1 = (1, 2, 3)
l3 = (*l1, *l2)
l3
(1, 2, 3, 4, 5, 6)
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {*s1, *s2}
s3
{1, 2, 3, 4}
s3 = [*s1, *s2]
s3
[1, 2, 3, 2, 3, 4]

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "e": 4}

d3 = {*d1, *d2}
d3
{'a', 'b', 'c', 'e'}
d3 = {**d1, **d2}
d3
{'a': 1, 'b': 2, 'c': 3, 'e': 4}
d3 = [**d1, **d2]
SyntaxError: invalid syntax
"""

# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
#
# # concatenation
# print(t1 + t2)
#
# # unpacking
# t3 = (*t1, *t2)
# print(t3)

#########################################################################################
# 52 Write a program to replace value present in nested dictionary.**
# # Replace "nose" with "net"

# dict_ = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
#
#
# def replace(d: dict, old: str, new: str) -> dict:
#     for key, value in d.items():
#         if isinstance(value, dict):
#             for key_n, value_n in value.items():
#                 if value_n == old:
#                     value[key_n] = new
#
#         if value == old:
#             d[key] = new
#
#     return d
#
#
# print(replace(dict_, "nose", "net"))
# print(replace(dict_, 100, "hello"))

###########################################################################################
# 53 Write a program to count the number of white spaces in a file.

# path = "./files/example.txt"
#
# # method 1 - count()
# with open(path) as file:
#     space_count = 0
#     for line in file:
#         space_count += line.count(" ")
#
#     print(space_count)
#
# # without inbuilt methods
# with open(path) as file:
#     space_count = 0
#     for line in file:
#         for char in line:
#             if char == " ":
#                 space_count += 1
#
#     print(space_count)
#
# # method 2 - split()
# with open(path) as file:
#     space_count = 0
#     for line in file:
#         words = line.split()
#         space_count += len(words) - 1
#     print(space_count)
#
# # reg ex
# with open(path) as file:
#     space_count = 0
#
#     for line in file:
#         space_count += len(re.findall(r" ", line))
#
#     print(space_count)

############################################################################################
# 54 Grouping anagrams.**
# l = ["listen", "hello", "eat", "desserts", "silent", "peek", "ate", "keep", "tea", "stressed"]
#
# """
# listen - sorted(listen) -->  [e, i, l, n, s, t] --> "eilnst"
# silent - sorted(silent) -->  [e, i, l, n, s, t] --> "eilnst"
# """
#
# anagrams = {}
# for item in l:
#     key = "".join(sorted(item))
#
#     if key not in anagrams:
#         anagrams[key] = [item]
#     else:
#         anagrams[key] += [item]
#
# print(anagrams)
#
# # default dict()
# from collections import defaultdict
#
# anagrams = defaultdict(list)
#
# for item in l:
#     key = "".join(sorted(item))
#     anagrams[key] += [item]
#
# print(anagrams)
#
# # printing only anagram groups from the dictionary
# for value in anagrams.values():
#     if len(value) > 1:
#         print(value)

###########################################################################################
# 56 Explain property decorator in python.

# property(getter, setter, deleter)

# class Employee:
#
#     def __init__(self, name, salary):
#         self._name = name
#         self._salary = salary
#
#     def get_name(self):
#         return self._name
#
#     def get_salary(self):
#         return self._salary
#
#     def change_name(self, new_name):
#         self._name = new_name
#
#     def change_salary(self, new_salary):
#         raise TypeError("salary cannot be modified")
#
#     def delete_name(self):
#         del self._name
#
#     def delete_salary(self):
#         del self._salary
#
#     name = property(get_name, change_name, delete_name)
#     salary = property(get_salary, change_salary, delete_salary)
#
#
# # e = Employee("John", 2000)
# # print(e.name)
# # e.name = "Dave"
# #
# # print(e.salary)
# # e.salary = 3000
# # del e.salary
#
# # property decorators
# class Employee:
#
#     def __init__(self, emp_name):
#         self._name = emp_name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, new_name):
#         self._name = new_name
#
#     @name.deleter
#     def name(self):
#         del self._name
#
#
# e = Employee("Steve")
# print(e.name)
# e.name = "John"
# del e.name

########################################################################################
# 58 Explain get() method in dictionaries.
"""
d = {"a": 1, "b": 2}

d["a"]
1
d["c"]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d["c"]
KeyError: 'c'

d.get("c")
d.get("a")
1
d.get("a", 0)
1
d.get("c", 0)
0
"""
########################################################################################
# 59 Write a list comprehension to get a list of even numbers from 1-50

# evens = [num for num in range(1, 51) if num % 2 == 0]
# print(evens)

########################################################################################
# 60 Find the longest non-repeated substring in the below string**

# s = "This is a Programming language and Programming is fun"
#
# # sorted()
# words = s.split()
# non_rep_words = []
#
# for word in words:
#     if words.count(word) == 1:
#         non_rep_words.append(word)
#
# res = sorted(non_rep_words, key=len)
# print(res[-1])
#
# # method 2
# s = "This is a Programming language and Programming is fun"
#
# words = s.split()
# longest = ""
#
# for word in words:
#     if words.count(word) == 1 and len(longest) < len(word):
#         longest = word      # This --> language
#
# print(longest)
#
# # max()
# s = "This is a Programming language and Programming is fun"
#
# words = s.split()
# non_rep_words = []
#
# for word in words:
#     if words.count(word) == 1:
#         non_rep_words.append(word)
#
# # print(max(non_rep_words, key=len))
#
# # dictionary
# s = "This is a Programming language and Programming is fun"
#
# words = s.split()
#
# d = {word: len(word) for word in words if words.count(word) == 1}
#
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])

######################################################################################
# 61 Write a program to find the duplicate elements in the list without using inbuilt functions**

# names = ['apple', 'google', 'apple', 'yahoo', 'google']
#
# # list
#
# non_duplicates = []
# duplicates = []
#
# for name in names:
#     if name not in non_duplicates:
#         non_duplicates.append(name)
#     else:
#         duplicates.append(name)
#
# print(non_duplicates)
# print(duplicates)
#
# # dictionary
#
# d = {}
#
# for name in names:
#     if name not in d:
#         d[name] = 1
#     else:
#         d[name] += 1
#
# print(d)
#
# for key, value in d.items():
#     if value > 1:
#         print(key)

##########################################################################################
# 62 Write a program to count the number occurrences of each item in the list without using any inbuilt functions**
# names = ['apple', 'google', 'apple', 'yahoo', 'google', 'facebook', 'gmail', 'yahoo']
#
# # list of tuples
# ele_count = []
#
# for name in set(names):     # ['apple', 'google', 'yahoo', 'facebook', 'gmail']
#     element = (name, names.count(name))
#     ele_count.append(element)
#
# print(ele_count)
#
# # without inbuilt methods
# count_ = {}
#
# for name in names:
#     if name not in count_:
#         count_[name] = 1
#     else:
#         count_[name] += 1
#
# print(count_)
#
# # default dictionary
# from collections import defaultdict
#
# count_ele = defaultdict(int)
#
# for name in names:
#     count_ele[name] += 1
#
# print(count_ele)

############################################################################################
# 63 Write a function to check if the number is Prime
"""
i = 2, 5 % 2 == 0
i = 3, 5 % 3 == 0
i = 4, 5 % 4 == 0
i = 5

num = 9
i = 2, 9 % 2 == 0
i = 3, 9 % 3 == 0
"""

# def is_prime(num):
#     if num > 1:
#         for i in range(2, num//2):
#             if num % i == 0:
#                 print("not a prime")
#                 break
#
#         else:
#             print("It is a prime")
#     else:
#         print("number should be greater than 1")
#
#
# is_prime(9)         # "not a prime"
# is_prime(5)         # It is a prime
# is_prime(2)
# is_prime(1)
#
# ###########################################################################################
# # prime number series 1 - 50
#
# for num in range(1, 51):
#     if num > 1:
#         for i in range(2, int(num**0.5)):
#             if num % i == 0:
#                 break
#
#         else:
#             print(num, end=" ")

###########################################################################################
# 64 How to create a tuple of numbers from 0 to 10 using range function

# tuple()
# print(tuple(range(0, 11)))

# concatenation
# t = ()
#
# for num in range(11):
#     t += (num,)
#
# print(t)

##########################################################################################
# 65 Write a program to find the largest number in the list without using any inbuilt functions**
# numbers = [10, 20, 30, 40, 50]
#
# # max()
# max_ = max(numbers)
# print(max_)
#
# # list.sort(key, reverse)
# numbers.sort()      # ascii value - ascending order
# print(numbers[-1])
#
# numbers.sort(reverse=True)      # ascii value - descending order
# print(numbers[0])
#
# # sorted(key, reverse) --> LIST
# numbers = [10, 20, 30, 40, 50]
#
# res = sorted(numbers)     # ascii value - ascending order
# print(res[-1])
#
# # without inbuilt method
# numbers = [10, 20, 30, 40, 50]
#
# max_num = 0
#
# for num in numbers:
#     if num > max_num:
#         max_num = num
#
# print(max_num)

# bubble sort

"""
numbers = [40, 20, 30, 10, 50]

iteration - 1
i = 0,  num = 40, 40 > 20 --> [20, 40, 30, 10, 50]
i = 1,  num = 40, 40 > 30 --> [20, 30, 40, 10, 50]
i = 2,  num = 40, 40 > 10 --> [20, 30, 10, 40, 50]
i = 3,  num = 40, 40 > 50 --> [20, 30, 10, 40, 50]
i = 4, 

iteration - 2
l = [20, 30, 10, 40, 50]

i = 0, num = 20, 20 > 30 --> [20, 30, 10, 40, 50]
i = 1, num = 30, 30 > 10 --> [20, 10, 30, 40, 50]
"""

# numbers = [40, 20, 30, 10, 50]
#
# for _ in range(len(numbers)-1):
#     for i in range(len(numbers)-1):
#         if numbers[i] > numbers[i + 1]:
#             numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#
# print(numbers[-1])

########################################################################################
# 66 Write a method that returns the last digit of an integer. For example, the call of get_last_digit(3572) should return 2.

# def last_digit(num: int):
#     return int(str(num)[-1])
#
#
# print(last_digit(1234))
#
#
# def last_digit(num):
#     return num % 10
#
#
# print(last_digit(1234))

###########################################################################################
# 67 Write a program to find most common words in a given list.**
# words = [
# 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
# 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
# 'eyes', 'look', 'into','my', 'eyes', "you're", 'under'
# ]
#
# # count()
# d = {word: words.count(word) for word in set(words)}
# l = sorted(d.items(), key=lambda item: item[-1])
# print(l[-1])
#
# # without inbuilt method
# d = {}
#
# for word in words:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
#
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])
#
# # default dict()
# from collections import  defaultdict
#
# d = defaultdict(int)
#
# for word in words:
#     d[word] += 1
#
# res = sorted(d.items(), key=lambda item: item[-1])
# print(res[-1])
#
# # Counter class
# from collections import Counter
#
# c = Counter(words)
# print(c)            # counter_object --> dict
# print(c.most_common())      # list of tuples
# print(c.most_common(1))
# print(c.most_common(2))

##########################################################################################
# 68 Make a function named tail that takes a sequence (like a list, string, or tuple) and a number n and returns the last n elements from the given sequence, as a list.**

# slicing
# def tail(sequence, n):
#     return sequence[-n:]
#
# print(tail("hello", 3))
#
#
# # islice()
# from itertools import islice
#
# def tail(sequence, n):
#     obj = islice(sequence, len(sequence)-n, len(sequence))      # islice object
#     list_ = list(obj)       # list
#     return "".join(list_)
#
# print(tail("hello", 3))
#
# # deque()
#
# from collections import deque
#
# def tail(seq, n):
#     res = list(deque(seq, n))
#     return "".join(res)
#
# print(tail("hello", 3))

##########################################################################################
# **69 Write function named is_perfect_square that accepts a number and returns True if it's a perfect square and False if it's not.**

# sqrt()

# from math import sqrt
#
# def is_perfect_square(num):
#     res = int(sqrt(num)) ** 2          # res = int(num ** 0.5) ** 2
#     return res == num
#
# print(is_perfect_square(4))
# print(is_perfect_square(27))
#
# # without inbuilt functions
#
# def is_perfect_square(num):
#
#     for i in range(num):
#         if i * i == num:
#             print(True)
#             break
#     else:
#         print(False)
#
#
# def is_perfect_square(num):
#     for i in range(num//2):
#         if i * i == num:
#             return True
#
#     return False

###########################################################################################
# **70 Write a program to get all the duplicate items and the number of times the item is repeated in the list.**
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'facebook', 'apple', 'gmail', 'gmail', 'gmail', 'gmail']
#
# # count()
# d = {}
# for name in set(names):
#     if names.count(name) > 1:
#         d[name] = names.count(name)
#
# print(d)
#
#
# d = {name: names.count(name) for name in set(names) if names.count(name) > 1}
# print(d)
#
# # without inbuilt functions
#
# d = {}
# for name in names:
#     if name not in d:
#         d[name] = 1
#     else:
#         d[name] += 1
#
# for key, value in d.items():
#     if value > 1:
#         print((key, value))

# Counter()

##########################################################################################
# **71 Write a program to count the number of occurrences of each word in a file.**

# path = "./files/example.txt"
#
# with open(path) as file:
#     d = {}
#     for line in file:
#         if line.strip():
#             words = line.split()
#
#             for word in words:
#                 if word not in d:
#                     d[word] = 1
#                 else:
#                     d[word] += 1
#
# print(d)

# Counter()

##########################################################################################
# 72 Write a program to count the number of occurrences of vowels in a file.

# path = "./files/example.txt"
#
# # using re
# import re
#
# with open(path) as file:
#     d = {}
#
#     for line in file:
#         if line.strip():
#             vowels = re.findall("[aeiou]", line, re.IGNORECASE)
#
#             for vowel in vowels:
#                 if vowel not in d:
#                     d[vowel] = 1
#                 else:
#                     d[vowel] += 1
#
# print(d)
#
# # without re
# with open(path) as file:
#     d = {}
#
#     for line in file:
#         if line.strip():
#
#             for char in line:
#                 if char.lower() in "aeiou":
#                     if char not in d:
#                         d[char] = 1
#                     else:
#                         d[char] += 1
# print(d)

#########################################################################################
# 73 Write a program to print all numeric values in a list**

items = ['apple', 1.2, 'google', '12.6', 26, '100']


#########################################################################################
"""
*         
* *       
* * *     
* * * *   
* * * * * 
"""
# n = 5
#
# for row in range(1, n+1):
#     print("* " * row)


# for row in range(n):
#     for col in range(n):
#         if row >= col:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 

"""
# n = 5
#
# for row in range(1, n+1):
#     print(f'{"* " * row:>{n * 2}}')

"""
    *     
   * *    
  * * *   
 * * * *  
* * * * * 
"""
# n = 5
#
# for row in range(1, n+1):
#     print(f'{"* " * row:^{n * 2}}')

"""
* * * * * * 
* * * * * 
* * * * 
* * * 
* *   
* 
"""

# n = 6
#
# for row in range(n, 0, -1):
#     print("* " * row)

"""
* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
"""
# n = 6
#
# for row in range(n, 0, -1):
#     print(f'{"* " * row:>{n * 2}}')

"""
 * * * * * *
  * * * * * 
   * * * *  
    * * *   
     * *    
      * 
"""
# n = 6
#
# for row in range(n, 0, -1):
#     print(f'{"* " * row:^{n * 2}}')

"""
1    
12   
123  
1234 
12345
"""

# n = 5
# pattern = ""
#
# for row in range(1, n+1):
#     pattern = pattern + str(row) + " "      # "1", "12", "123", "1234", "12345"
#     print(pattern)

"""
row = 1, pattern = "1"
row = 2, pattern = "1 2"
row = 3, pattern = "1 2 3"
row = 4, pattern = "1 2 3 4"
row = 5, pattern = "1 2 3 4 5"
"""
###########################################################################################
# 75 Write a program to count the occurrence of a particular word in the file

# path = "./files/example.txt"
#
#
# def word_occurrence(pattern):
#     count = 0
#     with open(path) as file:
#         for line in file:
#             words = line.split()
#             for word in words:
#                 if word == pattern:
#                     count += 1
#     return count
#
# print(word_occurrence("Today"))
#
# # count()
# def word_occurrence(pattern):
#     count = 0
#     with open(path) as file:
#         for line in file:
#             words = line.split()
#             count += words.count(pattern)
#
#     return count
#
# print(word_occurrence("Today"))

######################################################################################
# 76 Write a program to map a product to a company and build a dictionary with company and list of products pair**
# from collections import defaultdict
#
# all_products = ['iPhone', 'Mac', 'Gmail', 'Maps', 'iWatch', 'Windows', 'iOS', 'Google Drive', 'One Drive']
#
# # Pre-defined products for different companies
# apple_products = {'iPhone', 'Mac', 'iWatch'}
# google_products = {'Gmail', 'Maps', 'Google Drive'}
# msft_products = {'Windows', 'One Drive'}
#
# d = defaultdict(list)
#
# for product in all_products:
#
#     if product in apple_products:
#         d["apple_products"] += [product]
#
#     elif product in google_products:
#         d["google_products"] += [product]
#
#     elif product in msft_products:
#         d["msft_products"] += [product]
#
# print(d)

###########################################################################################
# 77 Write a program to rotate items of the list**
# from collections import deque
#
# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
#
# n = 3
# # deque()
# d_names = deque(names)
# d_names.rotate(n)
# # print(list(d_names))
#
# # without inbuilt methods
# for i in range(n):
#     item = names.pop()      # item -> amazon
#     names.insert(0, item)
#
# # print(names)
#
# """
# n = 1 >> ["amazon", "apple", "google", "yahoo", "gmail", "facebook", "flipkart"]
# n = 2 >> ["flipkart", "amazon", "apple", "google", "yahoo", "gmail", "facebook"]
# n = 3 >> ["facebook", "flipkart", "amazon", "apple", "google", "yahoo", "gmail"]
# """
#
# # slicing
# names = ["apple", "google", "yahoo", "gmail", "facebook", "flipkart", "amazon"]
# n = 3
#
# n_rotation = n % len(names)
#
# res = names[-n_rotation:] + names[:-n_rotation]
# # print(res)
#
# # function
# n = 4
#
# def rotate(iterable):
#     res = iterable[-1:] + iterable[:-1]
#     return res
#
# for i in range(n % len(names)):
#     names = rotate(names)
#     print(names)

##########################################################################################
# 83 Write a program to count the number of commented lines in a text file

# with open(path) as file:
#     count = 0
#     for line in file:
#         if line.startswith("#"):        # if line[0] == "#":
#             count += 1

##########################################################################################
# 84 Write a program to check if the year is leap year or not

# year = 2020
#
# import calendar
#
# print(calendar.isleap(year))
# print(calendar.isleap(1100))

#########################################################################################
"""
*
*
* 
* * 
* 
* * * 
* 
* * * * 
* 
* * * * * 
"""

# n = 5
#
# for row in range(1, n+1):
#     print("*")
#     print("* " * row)

###########################################################################################
# 89 Write a program to get the below output**
# ```python
# o/p:
# >>> [1, 2]
#     [3, 4]
#     [5, 6]
#     [7, 8]
#     [9]

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in range(0, len(a), 2):
#     print(a[i:i+2])

"""
i 
0       -->  a[0: 2]        --> [1, 2]
2       -->  a[2: 4]        --> [3, 4]
4       -->  a[4: 6]        --> [5, 6]
6       -->  a[6: 8]        --> [7, 8]
8       -->  a[8: 10]       --> [9]
"""

###########################################################################################
# 90 Write a program to check if the elements in the second list is series of continuation of the items in the first list**

# a = [10, 12, 14, 16, 18]
# b = [20, 22, 24, 26, 28]
#
# a = [0, 5, 10, 15]
# b = [20, 25, 30, 35, 40]
# #
# x = [10, 20, 30, 40]
# y = [50, 40, 60, 70]
#
# difference = x[1] - x[0]
# res = x + y         # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
#
# for i in range(len(res)-1):
#     if res[i+1] - res[i] != difference:
#         print("the lists are not a series")
#         break
#
# else:
#     print("lists are a series")

#############################################################################################
# 92 Write a program to find the first repeating character in a string

# string = "hello world"
#
# # count()
# for char in string:
#     if string.count(char) > 1:
#         print(char)
#         break
#
# # without using inbuilt methods
# res = []
# string = "hello world"
#
# for char in string:
#     if char not in res:
#         res += [char]
#     else:
#         print(char)
#         break

#########################################################################################
# 93 Write a program to find the index of nth occurrence of a sub-string in a string
# string = "hello world hello hai hello"
# n = 2
# char = "hello"
# count = 0
#
# for index, item in enumerate(string):
#     if item == char:
#         count += 1
#         if count == n:
#             print(index)
import re

# s = "hello world hello hai hello"
# nth_occ = 1
# pattern = "lo"
#
# def nth_occ_index(string, n, substring):
#     matches = re.finditer(substring, string)        # [obj1, obj2, obj3]
#
#     for index, match in enumerate(matches, start=1):
#         if n == index:
#             print(match.start(), match.end())
#
#
# nth_occ_index(s, nth_occ, pattern)

###########################################################################################
# 97 Write a program to count the number of occurrences of non-special characters in a given string**
# s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
#
# count = 0
#
# for char in s:
#     if ord("a") <= ord(char) <= ord("z") or ord("A") <= ord(char) <= ord("Z") or ord("0") <= ord(char) <= ord("9"):
#         count += 1
#
# # dictionary
#
# d = {}
# for char in s:
#     if ord("a") <= ord(char) <= ord("z") or ord("A") <= ord(char) <= ord("Z") or ord("0") <= ord(char) <= ord("9"):
#         if char not in d:
#             d[char] = 1
#         else:
#             d[char] += 1
#
# # using re
# import re
#
# s = 'hello@world! welcome!!! Python$ hi how are you & where are you?'
#
# res = re.findall(r'[a-zA-Z0-9]', s)
# print(len(res))
#
# d = {}
# for char in res:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
#
# print(d)

############################################################################################
# 98 Grouping Flowers and Animals in the below list**

# items = ['lotus-flower', 'lilly-flower', 'cat-animal', 'sunflower-flower', 'dog-animal']
# d = {}
#
# for item in items:
#     name, type = item.split("-")     # [lotus, flower]
#
#     if type not in d:
#         d[type] = [name]
#     else:
#         d[type].append(name)
#
# print(d)

#########################################################################################
# 100 Filter only those characters except digits**
# s = '@hello12world34welcome!123'
#
# # method 1
#
# for char in s:
#     if char not in "0123456789":    #if not (ord("0") <= ord(char) <= ord("9")):
#         print(char, end=" ")
#
# print()
# # method 2 - re
# import re
#
# print(re.findall(r"[^0-9]", s))
# print(re.findall(r"\D", s))

##########################################################################################
# 101 Count number of letters in a word in the sentence. ignore special characters.**
# sentence = "Hi there! How are you:) How are you doing today!"
#
# words = sentence.split()
# d = {}
#
# for word in words:      # there!
#     count = 0
#     res = ""
#
#     for char in word:   # t, h, e, r, e, !
#         if char.isalpha():
#             count += 1      # 1, 2, 3, 4, 5
#             res += char     # "there"
#
#     d[res] = count
# print(d)
#
# # reg ex
# import re
# sentence = "Hi there! How are you:) How are you doing today!"
#
# res = re.findall(r"[a-zA-Z0-9]+", sentence)
# print(res)

###########################################################################################
# 104 Find all max length words from the below sentence**
# sentence = "hello world hi apple you yahoo to you"
# words = sentence.split()
#
# longest = max(words, key=len)
# print(longest)
#
# for word in words:
#     if len(word) == len(longest):
#         print(word)

##########################################################################################
# 105 Find the range from the following string**
# Output Should be [0, 4, 5, 6, 7, 8, 20, 43, 44, 45, 46]

# sentence = '0-0, 4-8, 20-20, 43-46'
#
# range_ = sentence.split(",")
# print(range_)               # ['0-0', ' 4-8', ' 20-20', ' 43-46']
#
# output = []
# for item in range_:
#     start, end = item.split("-")
#
#     res = list(range(int(start), int(end)+1))
#     output.extend(res)
#
# print(output)

########################################################################################
# 106 Can we override a static method in python?

# class Base:
#
#     @staticmethod
#     def display():
#         print("hello")
#
#     @classmethod
#     def name(cls):
#         print("in name method")
#
#
# class Derived(Base):
#
#     @staticmethod
#     def display():
#         print("hai")
#
#     @classmethod
#     def name(cls):
#         print("in name method in derived class")
#
#
# d = Derived()
# d.display()
# d.name()            # d.__class__.name(), Derived.name(d)

##########################################################################################
# 107 Write a function which returns the sum of lengths of all the iterables**
# >>> total_length([1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'flipkart'], {1, 2, 3}, {'a': 1, 'b': 2})
# o/p: 15

# input_ = [1, 2, 3], (4, 5), ['apple', 'google', 'yahoo', 'gmail', 'flipkart'], {1, 2, 3}, {'a': 1, 'b': 2}


# def total_length(*args):
#     len_ = 0
#     for element in args:
#         if isinstance(element, (str, tuple, list, dict, set)):
#             len_ += len(element)
#     return len_
#
#
# print(total_length(*input_))

############################################################################################
# 108 Replace whitespaces with newline character in the below string**
# sentence = "Hello world welcome to python"
#
# # replace()
# print(sentence.replace(" ", "\n"))
# print()
# # concatenating
# res = ""
#
# for char in sentence:
#     if char == " ":
#         res += "\n"
#     else:
#         res += char
# print(res)
# print()
# # re
# import re
#
# print(re.sub(" ", "\n", sentence))
# print()
# print(re.subn(" ", "\n", sentence))      # tuple(replaced string, number of replacements)

#############################################################################################
# 109 Replace all vowels with "*"
# sentence = "hello world welcome to python"

# # concatenation
# res = ""
#
# for char in sentence:
#     if char.lower() in "aeiou":
#         res += "*"
#     else:
#         res += char
#
# print(res)
#
# # re
# import re
#
# print(re.sub("[aeiou]", "*", sentence))

############################################################################################
# 110 Replace all occurrences of "Java" with "Python" in a file

# path = r"./files/example.txt"
#
# with open(path) as file:
#     with open("./files/demo.txt", "w") as write_file:
#         for line in file:
#             if line.strip():
#                 words = line.split()       # [Java, python]
#
#                 for index, word in enumerate(words):
#                     if word.lower() == "java":
#                         words[index] = "python"
#
#                 new_line = " ".join(words)
#                 write_file.write(new_line+"\n")

#########################################################################################
# 111 sum of first 3 Maximum numbers and sum of first 3 Minimum numbers**
# numbers = [10, 15, 20, 25, 30, 35, 40, 15, 15]
#
# numbers.sort()
# least_sum = sum(numbers[:3])
# max_sum = sum(numbers[-3:])
#
# print(least_sum, max_sum)

###########################################################################################
# 112 Write a program to get the output as below**
# # i/p is "python@#$%pool"
# # o/p should be ['PYTHON', 'POOL']

# string = "python@#$%pool"
#
# # re
#
# import re
# pattern = r"[A-Za-z]+"
# res = re.findall(pattern, string)
#
# op = []
# for word in res:
#     op.append(word.upper())
#
# print(op)

###################################################################################
# 113 Write a program to print all the number which are ending with 5**
# numbers = ['1', '12', '123', '12345', '125', '905', '55', '5', '95655', '55555']
#
# for number in numbers:
#     if number.endswith("5"):        # number[-1] == "5"
#         print(number)
#
# # re
# import re
#
# pattern = r"[0-9]*5$"
#
# for number in numbers:
#     print(re.findall(pattern, number))

############################################################################################
# 114 Write a program to get the indexes of each item in the below list**
# names = ['apple', 'google', 'apple', 'yahoo', 'yahoo', 'google', 'gmail', 'gmail', 'gmail']
# output should be -  {'apple': [0, 2], 'google': [1, 5], 'yahoo': [3, 4], 'gmail': [6, 7, 8]}

# d = {}
# for index, name in enumerate(names):
#     if name not in d:
#         d[name] = [index]
#     else:
#         d[name] += [index]
#
# print(d)

##########################################################################################################
# 115 Write a program to print "Bangalore" 10 times without using "for" loop**

# print("Bangalore\n" * 10)

###########################################################################################
# 118 Write a program to add each number in word1 to number in word2**
# word1 = 'hello 1 2 3 4 5 6'
# word2 = 'world 5 6 7 8 9'
# # # e.g. 1 + 5, 2 + 6, 3 + 7, 4 + 8, 5 + 9
#
# import re
#
# num1 = re.findall("[0-9]", word1)       # [1, 2, 3, 4, 5, 6]
# num2 = re.findall("[0-9]", word2)       # [5, 6, 7, 8, 9]
# method 1

# for i in range(len(num1)):  # i --> 0, 1, 2, 3, 4, 5
#     print(int(num1[i]) + int(num2[i]), end=", ")

# zip()
# for item1, item2 in zip(num1, num2):
#     print(int(item1) + int(item2))

# zip_longest()
# from itertools import zip_longest
#
# res = zip_longest(num1, num2, fillvalue=0)
#
# for item1, item2 in res:
#     print(int(item1) + int(item2))

########################################################################################
# 121 Write a program to remove duplicates from the list without using set or empty list
l1 = [1, 2, 3, 4, 1, 2, 3, 4, 3, 4, 4]

d = {}
for item in l1:
    d[item] = l1.count(item)

print(d.keys())

# for key,  value in d.items():
#     if value == 1:
#         print(key)

############################################################################
# 122 Print all the missing numbers from 1 to 10 in the below list
# l = [3, 4, 7, 9]
#
# for item in range(1, 11):
#     if item not in l:
#         print(item)

#####################################################################################
# 123 Write a python program to get the below output**
# >>> # o/p ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']

# l1 = [1, 2, 3]
# l2 = ['a', 'b', 'c']
#
# res = []
# for item1 in l1:
#     for item2 in l2:
#         op = str(item1) + item2
#         res.append(op)

# print(res)

#########################################################################################
# 124 Write a python program to get the below output
# string = "AAAAaaCCYYYY"
# # op = ["Y4", "C2", "a2", "A4"]
#
# d = {}
# for char in string:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
#
# print(d)
#
# l = []
#
# for key, value in d.items():
#     l.append(key+str(value))
#
# l.reverse()
# print(l)

#########################################################################################
# **125 What is the output of the below function call**

# class Demo:
#     def greet(self):
#         print("hello world")
#
#     def greet(self):
#         print("hello universe")
#
#
# d = Demo()
# d.greet()

#########################################################################################
# 126 In the list below, find all the number pairs which results in 10 either when added or subtracted**

# a = [3, 5, -4, 8, 11, 1, -1, 6]

# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         if a[i] + a[j] == 10 or a[i] - a[j] == 10:
#             print(a[i], a[j])
#
#
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j:
#             if a[i] + a[j] == 10 or a[i] - a[j] == 10:
#                 print(a[i], a[j])

"""
[3, 5, -4, 8, 11, 1, -1, 6]

i           j
3           3
            5
            -4
            8
            11
            
5            -4   
             8
             11
             1
             -1
             6

-4          8
            11
            1
            -1
            6



"""





