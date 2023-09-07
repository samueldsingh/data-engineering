
## 1. What is the difference between python 2 and python 3?

**division `/`** operator: It preferred to use the floating value (like 7.0/5 or 7/5.0) to get the expected result in Python 2.

Example:
```
print(7 / 5 )
print(-7 / 5)    

'''
Output in Python 2.x
1
-2
 
Output in Python 3.x :
1.4
-1.4
'''
```

**`print`**: In Python 3, the print statement from Python 2 is converted to Python function. However, parentheses work in Python 2 if space 
is added after the print keyword because the interpreter evaluates it as an expression.

```
print 'Hello, Geeks'	 # Python 3.x doesn't support
print('Hope You like these facts')
'''
Output in Python 2.x :
Hello, Geeks
Hope You like these facts

Output in Python 3.x :
File "a.py", line 1
	print 'Hello, Geeks'
					^
SyntaxError: invalid syntax
'''
```

**Unicode in Python 3**: 

In Python 2, an implicit str type is ASCII. But in Python 3.x implicit str type is Unicode. In this example, difference is shown between both 
the version of Python with the help of code and also the output in Python comments.

```
print(type('default string '))
print(type(b'string with b '))

'''
Output in Python 2.x (Bytes is same as str)
<type 'str'>
<type 'str'>

Output in Python 3.x (Bytes and str are different)
<class 'str'>
<class 'bytes'>
'''
```

In Python 2, unicode is supported as:

```
print(type('default string '))
print(type(u'string with b '))
'''
Output in Python 2.x (Unicode and str are different)
<type 'str'>
<type 'unicode'>
   
Output in Python 3.x (Unicode and str are same)
<class 'str'>
<class 'str'>
'''
```

**`xrange()` vs `range()` in both versions**:

- In Python 2, `range()` returns a list `[0,1,2], whereas `xrange()` returns an iterator object which works similar to
  Java iterator and generates number when needed.
- If we need to iterate over the same sequence multiple times, we prefer `range()` as range provides a static list.
- `xrange()` doesn’t support slices and other list methods.
- The advantage of `xrange()` is it acts as a generator and saves memory when the task is to iterate over a large range.
- In Python 3.x, the `range` function now does what `xrange` does in Python 2.x, so to keep our code portable, we might want to stick to using a range instead.
- [range vs xrange](https://www.geeksforgeeks.org/range-vs-xrange-in-python/)

**Error Handling**
There is a small change in error handling in both versions. In latest version of Python, ‘as’ keyword is optional. 

```
try:
	trying_to_check_error
except NameError, err:
# Would not work in Python 3.x
	print err, 'Error Caused'

'''
Output in Python 2.x:
name 'trying_to_check_error' is not defined Error Caused

Output in Python 3.x :
File "a.py", line 3
	except NameError, err:
					^
SyntaxError: invalid syntax
'''
```

```
try:
	trying_to_check_error
except NameError as err:
	print(err, 'Error Caused')

# code without using as keyword
try:
	trying_to_check_error
	
# 'as' is optional in Python 3.10
except NameError:
	print('Error Caused')
	
'''
Output in Python 2.x:
(NameError("name 'trying_to_check_error' is not defined",), 'Error Caused')

Output in Python 3.x :
name 'trying_to_check_error' is not defined Error Caused
'''
```

## 2. What is regular expression?

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search 
pattern. 

```
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

# Output:
YES! We have a match!

# Explanation:
^ represents startswith
. represents anycharacter except newline character
$	represents Ends with
```

[Regular Expression](https://www.w3schools.com/python/python_regex.asp)

## API call

An API call, or API request, allows one application to request data or services from another application. Most web applications regularly make API calls. [API](https://www.cloudflare.com/learning/security/api/what-is-api-call/#:~:text=Application%20programming%20interfaces%20(APIs)%20are,provide%20a%20service%20or%20information.)

An API consists of three parts:
- Request URL: A request URL consists of an HTTP method, a base URL, and a resource URI. The request header also includes parameters such as the content type and authorization information. The following format to construct a request URL: `<HTTP method> http(s)://<host>:<port>/api/public/<resource URI>`. The following example shows a URL for a request that returns a list of all projects: `GET http://<host name>:<port number>/api/public/tdm/v1/projects`.
- Request Method: The message that is sent by a client to a server is what is known as an HTTP request. An HTTP request is an action to be performed on a resource identified by a given Request-URL. [HTTP requests](https://rapidapi.com/blog/api-glossary/http-request-methods/#:~:text=An%20HTTP%20request%20is%20an,is%20assigned%20a%20specific%20purpose.)
- Payload: When each unit of data is transmitted, it boasts two essential parts: the header/overhead identifier and the actual information dubbed payload. A payload in API is the actual data pack that is sent with the GET method in HTTP. It is the crucial information that you submit to the server when you are making an API request. The payload can be sent or received in various formats, including JSON. Usually, the payload is denoted using the `“{}”` in a query string. [Payload](https://rapidapi.com/blog/api-glossary/payload/#:~:text=A%20payload%20in%20API%20is,%7B%7D%E2%80%9D%20in%20a%20query%20string.)

Let's consider the JSON web service response:

```
{
    "status":"OK",
    "data":
        {
            "message": "Welcome, world!"
        }
}
```

In the above example, the payload is the Welcome, World! Since it is the part of the query string that the user is interested in. The rest of the information is referred to as the overhead data. This is because it is only used to show the source or destination and display authenticity.

[Making HTTPS requests in Python](https://www.datacamp.com/tutorial/making-http-requests-in-python)
