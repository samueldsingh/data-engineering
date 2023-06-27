
## Important string functions:
# centre, count, find, index, join, replace, split, strip

## Built in functions string

# 1. center(width, fillchar)
# Returns a space-padded string with the original string centered to a total of width columns.

# text = "Hello"
# centered_text = text.center(10)     # resulting string is padded with spaces on both sides to achieve center alignment of width 10
# print(centered_text)

# text = "Programming"
# centered_text = text.center(20, "-")
# print(centered_text)

# Without using any function

# text = "Hello, World!"
# width = 30  # Width of the output
#
# string = "Hello, World!"
# text_length = 0  # Initialize length to 0
#
# for char in string:  # Iterate over each character in the string
#     text_length += 1  # Increment the length by 1 for each character
#
#
# padding_length = (width - text_length) // 2  # Calculate padding length on each side
#
# padding = " " * padding_length  # Create the padding string
#
# centered_text = padding + text + padding  # Concatenate the padding with the text
#
# print(centered_text)  # Output: "       Hello, World!       "



# 2. Count
# count(str, beg= 0,end=len(string)) *
# Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.

# text = "Hello, how are you?"

# text = "Mississippi"
# count = text.count("ss")
# print(count)

# text = "She sells seashells by the seashore"
# count = text.count("se")
# print(count)

# Count the number of occurrences of 'se' in the sentence starting from index 10
# sentence = "She sells seashells by the seashore"
# count = sentence.count('se', 10)
# print(count)  # Output: 2

# Count the number of occurrences of 's' in the sentence from index 10 to 20
# sentence = "She sells seashells by the seashore"
# count = sentence.count('s', 5, 20)
# print(count)  # Output: 1

# string = "Hello, World!"
# character = 'o'
# count = 0  # Initialize the count to 0
#
# for char in string:  # Iterate over each character in the string
#     if char == character:  # Check if the character matches the target character
#         count += 1  # Increment the count by 1
#
# print(count)  # Output: 2

# 3. Find (str, beg=0 end=len(string))
# Determine if str occurs in string or in a substring of string if starting
# index beg and ending index end are given returns index if found and -1 otherwise.
# The find() method in Python is used to find the first occurrence of a substring within a given string.
#
# sentence = "She sells seashells by the seashore."
#
# # Find the index of the first occurrence of 'se' in the sentence
# index = sentence.find('se')
# print(index)  # Output: 4
#

# # Find the index of the first occurrence of 'sh' starting from index 10
# index = sentence.find('sh', 10)
# print(index)  # Output: 13
#
# # Find the index of the first occurrence of 'e' in the sentence from index 10 to 20
# index = sentence.find('e', 10, 20)
# print(index)  # Output: 11

# Without using function
# sentence = "She sells seashells by the seashore."
# target_char = "S"
#
# # Find the index of the first occurrence of the target character
# index = -1  # Initialize with -1 in case the character is not found
#
# for i in range(len(sentence)):
#     if sentence[i] == target_char:
#         index = i
#         break
#
# # Print the result
# if index != -1:
#     print(f"The index of the first occurrence of '{target_char}' is: {index}")
# else:
#     print(f"'{target_char}' is not found in the sentence.")

# 4. index(str, beg=0, end=len(string))
# Same as find(), but raises an exception if str not found.
# The index() method in Python is used to find the index of the first occurrence of a substring within a given string.

# sentence = "She sells seashells by the seashore."

# Find the index of the first occurrence of 'se' in the sentence
# index = sentence.index('se')
# print(index)  # Output: 7
#
# # Find the index of the first occurrence of 'sh' starting from index 10
# index = sentence.index('sh', 10)
# print(index)  # Output: 13
#
# # Find the index of the first occurrence of 'z' in the sentence from index 10 to 20
# try:
#     index = sentence.index('z', 10, 20)
#     print(index)
# except ValueError:
#     print("Substring not found.")

# string = "Hello, world!"
# character = input("Enter the character: ")
#
# for i in range(len(string)):
#     if string[i] == character:
#         index = i
#         break
# else:
#     index = "Not found"

# print(index)

# 5. join(seq)
# Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.
# The join() method in Python is used to concatenate elements from a sequence into a single string.

# fruits = ['apple', 'banana', 'cherry']
#
# # Join the elements of the fruits list using a comma as the delimiter
# result = ', '.join(fruits)
# print(result)  # Output: "apple, banana, cherry"

# # Join the elements of a tuple using a hyphen as the delimiter
# numbers = ('1','2','3','4','5')
# result = '-'.join(numbers)
# print(result)  # Output: "1-2-3-4-5"

# Without using functions

# sequence = ['Hello', ' ', 'world', '!']
# result = ''  # Initialize an empty string to store the concatenated result
#
# # Concatenate the elements into a single string
# for element in sequence:
#     result += element
#
# # Print the result
# print(result)  # Output: Hello world!

# Example 2:
# string1 = "Hello"
# string2 = "World"
# separator = " "
# result = ""
#
# for char1 in string1:
#     result += char1
#
# result += separator
#
# for char2 in string2:
#     result += char2
#
# print(result)  # Output: Hello World


# 6. replace(old, new [, max])
# Replaces all occurrences of old in string with new or at most max occurrences if max given.
# sentence = "She sells seashells by the seashore."
#
# # Replace all occurrences of 'se' with 'me' in the sentence
# new_sentence = sentence.replace('se', 'me')
# print(new_sentence)  # Output: "She mells meashells by the meashore."
#
# # Replace only the first occurrence of 'se' with 'me' in the sentence
# new_sentence = sentence.replace('se', 'me', 1)
# print(new_sentence)  # Output: "She mells seashells by the seashore."

# Without using functions

# string = "Hello, World!"
# old_char = "o"
# new_char = "x"
# result = ""
#
# for char in string:
#     if char == old_char:
#         result += new_char
#     else:
#         result += char
#
# print(result)  # Output: Hellx, Wxrld!


# 7. split(str="", num=string.count(str))
# Splits string according to delimiter str (space if not provided) and returns
# list of substrings; split into at most num substrings if given.

# sentence = "She sells seashells by the seashore."
#
# # Split the sentence into a list of words using the default delimiter
# words = sentence.split()
# print(words)  # Output: ['She', 'sells', 'seashells', 'by', 'the', 'seashore.']
#
# # Split the sentence into a list of words using the space as the delimiter
# words = sentence.split(' ')
# print(words)  # Output: ['She', 'sells', 'seashells', 'by', 'the', 'seashore.']
#
# # Split the sentence into a list of words using 'se' as the delimiter
# words = sentence.split('se')
# print(words)  # Output: ['She ', 'lls ', 'ash', 'lls by the ', 'ashore.']
#
# # Split the sentence into a list of words using the first 3 occurrences of 's' as the delimiter
# words = sentence.split('s', 3)
# print(words)  # Output: ['', 'he ', 'ell', ' seashells by the seashore.']

# Without using functions

# string = "Hello, World!"
# delimiter = ","
# result = []
# substring = ""
#
# for char in string:
#     if char != delimiter:
#         substring += char
#     else:
#         result.append(substring)
#         substring = ""
#
# result.append(substring)  # Add the last substring after the last delimiter
#
# print(result)  # Output: ['Hello', ' World!']


# 8. strip([chars])
# Performs both lstrip() and rstrip() on string

# text = "   Hello, World!   "
#
# # Remove leading and trailing whitespace characters
# new_text = text.strip()
# print(new_text)  # Output: "Hello, World!"
#
# # Remove leading and trailing specific characters (e.g., 'H', '!', ' ')
# new_text = text.strip('H! ')
# print(new_text)  # Output: "ello, World"

# 9. capitalize()
# Capitalizes first letter of string

# text = "hello, world!"
# capitalized_text = text.capitalize()
# print(capitalized_text)  # Output: "Hello, world!"
#
#
# text = "123abc"
# capitalized_text = text.capitalize()
# print(capitalized_text)  # Output: "123abc"

# 10. len(string)
# Returns the length of the string

# text = "Hello, World!"
# length = len(text)
# print(length)  # Output: 13

# text = "Hello"
# for i in range(len(text)):
#     print(text[i])

# text = "Python"
# if len(text) == 6:
#     print("The string has 6 characters.")
# else:
#     print("The string does not have 6 characters.")

# Without using any function:

# string = "Hello, World!"                      # State
# length = 0  # Initialize length to 0          # Validation
#
# for char in string:  # Iterate over each character in the string      # Behavior
#     length += 1  # Increment the length by 1 for each character
#
# print(length)  # Output: 13

# 10. max(str)
# Returns the max alphabetical character from the string str.
# It will return the digit with the highest Unicode value, not necessarily the largest numeric value
#
# text = "Hello, World!"
# max_length = max(text)
# print(max_length)   # Output: r

# tuple_nums = (3, 8, 1, 6, 4)
# max_val = max(tuple_nums)
# print(max_val)  # Output: 8

# Without using any functions

# string = "hello world!"
# max_character = ""
#
# # Iterate over each character in the string
# for char in string:
#     # Check if the current character is greater than the current maximum character
#     if char > max_character:
#         max_character = char
#
# print(max_character)  # Output: "w"


# 11. min(str)
# Returns the min alphabetical character from the string str.
# It finds and returns the character with the lowest Unicode value
#
# text = "Hello,World!"
# min_length = min(text)
# print(min_length)   # Output: !
#
# Without using any function
# string = "openai"
# min_char = chr(127)  # Initialize with a high ASCII value
#
# for char in string:
#     if ord(char) < ord(min_char):
#         min_char = char
#
# print("Minimum character:", min_char)


# 12. rstrip()
# Removes all trailing whitespace of string.
# It can be handy when working with input data or when dealing with strings that have inconsistent spacing.
# The rstrip() method only removes whitespace characters from the right end of the string.

# text = "   Hello, World!    "
# trimmed_text = text.rstrip()
# print(trimmed_text)  # Output: "   Hello, World!"
#
# text_with_spaces = "   Hello,   World!    "
# trimmed_text_with_spaces = text_with_spaces.rstrip()
# print(trimmed_text_with_spaces)  # Output: "   Hello,   World!"

# # Without using function:
# string = "  Hello World!   "
# length = len(string)
# i = length - 1
#
# while i >= 0 and string[i].isspace():       # while loop starts from the rightmost character
#                                             # of the string and checks if it is a whitespace character.
#     i -= 1                                  # the loop continues to the previous character
#                                             # Once a non-whitespace character is encountered, the loop stops
# result = string[:i+1]
# print(result)


# 13. startswith(str, beg=0,end=len(string))
# Determines if string or a substring of string (if starting index beg and
# ending index end are given) starts with substring str; returns true if so and false otherwise.
#
# text = "Hello, World!"
# starts_with_hello = text.startswith("Hello")
# print(starts_with_hello)  # Output: True
#
# starts_with_hi = text.startswith("Hi")
# print(starts_with_hi)  # Output: False


# Without using any function

def starts_with(string, substring):
    if len(substring) > len(string):
        return False

    for i in range(len(substring)):
        if string[i] != substring[i]:
            return False

    return True

# Example usage
string = "Hello, world!"
substring = "Hello"

if starts_with(string, substring):
    print("The string starts with the substring.")
else:
    print("The string does not start with the substring.")



# 14. upper()
#
# text = "hello, world!"
# upper = text.upper()
# print(upper)

# 15. capitalize()
# Capitalizes first letter of string

# text = "hello, world!"
# capital = text.capitalize()
# print(capital)
#
# 16. decode(encoding='UTF-8',errors='strict')
# Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.

# byte_string = b'Hello, World!'
# decoded_string = byte_string.decode('UTF-8')
# print(decoded_string)  # Output: "Hello, World!"
#
# 17. encode(encoding='UTF-8',errors='strict')
# Returns encoded string version of string; on error, default is to raise a ValueError
# unless errors is given with 'ignore' or 'replace'.
#
# string = "Hello, World!"
# encoded_bytes = string.encode('UTF-8')
# print(encoded_bytes)  # Output: b'Hello, World!'


# 18. endswith(suffix, beg=0, end=len(string))
# Determines if string or a substring of string (if starting index beg and ending
# index end are given) ends with suffix; returns true if so and false otherwise.
#
# string = "Hello, World!"
# suffix = "World!"
#
# result = string.endswith(suffix, 7)  # Search from index 7 onwards
#
# print(result)  # Output: False


# 19. expandtabs(tabsize=8)
# Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.
#
# string = "Hello\tWorld!"
# tabsize = 4
#
# expanded_string = string.expandtabs(tabsize)
#
# print(expanded_string)  # Output: Hello   World!

# 20. isalnum()
# Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.
#
# string = "Hello123"
#
# result = string.isalnum()
#
# print(result)  # Output: True


# 21. isalpha()
# Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.
#
# string = "Hello"
#
# result = string.isalpha()
#
# print(result)  # Output: True

# 22. isdigit()
# Returns true if string contains only digits and false otherwise.
#
# string = "12345"
#
# result = string.isdigit()
#
# print(result)  # Output: True

# 23. islower()
# Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.
#
# string = "Hello"
#
# result = string.islower()
#
# print(result)  # Output: False

# 24. isnumeric()
# Returns true if a unicode string contains only numeric characters and false otherwise.
#
# string = "12345a"
#
# result = string.isnumeric()
#
# print(result)  # Output: False

# 25. isspace()
# Returns true if string contains only whitespace characters and false otherwise.
#
# string = "    "
#
# result = string.isspace()
#
# print(result)  # Output: True
#
# string = "   Hello   "

# result = string.isspace()
#
# print(result)  # Output: False

# 26. istitle()
# Returns true if string is properly "titlecased" and false otherwise.
#
# string = "This Is Title Case"
#
# result = string.istitle()
#
# print(result)  # Output: True
#
#
# string = "This is not Title Case"
#
# result = string.istitle()
#
# print(result)  # Output: False
#

# 27. isupper()
# Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.

# string = "HELLO"
#
# result = string.isupper()
#
# print(result)  # Output: True
#
#
# string = "Hello"
#
# result = string.isupper()
#
# print(result)  # Output: False

# 28. ljust(width[, fillchar])
# Returns a space-padded string with the original string left-justified to a total of width columns.

# string = "Hello"
#
# width = 10
#
# new_string = string.ljust(width)
#
# print(new_string)
#
#
# string = "Hello"
# width = 10
# fillchar = '-'
#
# new_string = string.ljust(width, fillchar)
#
# print(new_string)  # Output: "Hello-----"


# # 29. lower()
# # Converts all uppercase letters in string to lowercase.
#
# string = "Hello"
#
# new_string = string.lower()
#
# print(new_string)


# 30. lstrip()
# Removes all leading whitespace in string.

# string = "Hello"
#
# new_string = string.lstrip()
#
# print(new_string)

# 31. maketrans()
# Returns a translation table to be used in translate function.

# original_string = "Hello, world!"
# translation_table = str.maketrans("lo", "xy")
# new_string = original_string.translate(translation_table)
# print(new_string)       # Output: Hexxy, wyrxd!

# 32. rfind(str, beg=0,end=len(string))
# Same as find(), but search backwards in string.
# The rfind() method in Python is used to find the last occurrence of a substring within a string.
# It returns the index of the last occurrence of the substring if found, or -1 if the substring is not present.

# string = "Hello, Hello, Hello"
# substring = "Hello"
# index = string.rfind(substring)
# print(index)        # Output: 14

# string = "Hello, world!"
# substring = "Python"
# index = string.rfind(substring)
# print(index)          # Output: -1

# 33. rindex( str, beg=0, end=len(string))
# Same as index(), but search backwards in string.
# The difference from rfind() is that rindex() raises a ValueError if the substring is not found, instead of returning -1.

# string = "Hello, Hello, Hello"
# substring = "Hello"
# index = string.rindex(substring)
# print(index)            # Output: 14

# string = "Hello, world!"
# substring = "Python"
# index = string.rindex(substring)
# print(index)              # Output: Value Error

# 34. rjust(width,[, fillchar])
# Returns a space-padded string with the original string right-justified to a total of width columns.
# It returns a new string with the specified width.
# If fillchar is not provided, it defaults to whitespace.

# string = "Hello"
# new_string = string.rjust(10)
# print(new_string)           # Output:      Hello

# string = "Hello"
# new_string = string.rjust(10, "*")
# print(new_string)             # Output: *****Hello

# 35. splitlines( num=string.count('\n'))
# Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.
# If num is not provided, it defaults to string.count('\n'), which means it splits the string at every line break.
# The splitlines() method is particularly useful when dealing with multi-line strings or text files, as it
# allows you to extract individual lines for further processing.

# string = "Hello\nWorld\nPython"
# lines = string.splitlines()
# print(lines)                # Output: ['Hello', 'World', 'Python']

# You can also specify the maximum number of splits using the num parameter. For example:
# string = "Hello\nWorld\nPython"
# lines = string.splitlines(1)
# print(lines)                # Output: ['Hello\n', 'World\n', 'Python']


# string = "Hello\nWorld\nPython"
# lines = string.splitlines()
# print(lines)                   # Output: ['Hello\n', 'World\n', 'Python']

# The resulting list contains the lines of the original string,
# including the line break character ('\n') at the end of each line.

# 36. swapcase()
# Inverts case for all letters in string.


# The swapcase() method is useful when you need to convert the case of characters
# in a string without altering the original string. It can be handy for tasks such
# as case-insensitive comparisons or for modifying the appearance of text.

# string = "Hello World"
# new_string = string.swapcase()
# print(new_string)           # Output: hELLO wORLD

# 37. title()
# Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.

# string = "hello world"
# new_string = string.title()
# print(new_string)             # Output: Hello World

# 38. translate(table, deletechars="")
# Translates string according to translation table str(256 chars), removing those in the del string.

# string = "Hello, World!"
# table = str.maketrans("o", "e")
# new_string = string.translate(table)
# print(new_string)           # Output: Helle, Werld!


# 39. zfill (width)
# Returns original string leftpadded with zeros to a total of width characters; intended
# for numbers, zfill() retains any sign given (less one zero).

# string = "42"
# new_string = string.zfill(5)
# print(new_string)           # Output: 00042

# 40. isdecimal()
# Returns true if a unicode string contains only decimal characters and false otherwise.

# string1 = "12345"
# string2 = "12.34"
# string3 = "abc123"
#
# print(string1.isdecimal())  # Output: True
# print(string2.isdecimal())  # Output: False
# print(string3.isdecimal())  # Output: False