
## 1. Controller, Service and DAO

"Controller," "service," and "DAO" stand for specific components of an application's architecture, especially in the context of a design pattern like MVC (Model-View-Controller). Here's an explanation of each term:

**1. Controller:**
- A controller is responsible for handling user input and interaction within an application.
- It acts as an intermediary between the user interface (view) and the application's logic (model).
- The controller receives user requests from the view, processes them, interacts with the model to retrieve or manipulate data, and sends the appropriate response back to the view. It helps separate the concerns of user interaction and application logic.

**2. Service:**
- A service is a component that encapsulates specific business logic or functionality in an application.
- Services are often used to provide a higher-level abstraction over data manipulation or operations.
- They can include complex calculations, data validation, and interactions with multiple data sources or models. Services are designed to be reusable and independent of specific user interface or presentation concerns.

**3. DAO (Data Access Object):**
- DAO is a design pattern that separates the data access logic from the rest of the application.
- The DAO pattern provides an interface to interact with a data source (such as a database) without exposing the underlying implementation details.
- It encapsulates the CRUD (Create, Read, Update, Delete) operations and ensures that data access concerns are isolated. DAOs are often used to abstract the database interactions and make it easier to switch to different data sources or adapt to changes in data storage technologies.

In Python applications, these components can be organized in various ways based on the architectural pattern you're following. For instance, in a web application using a framework like Flask or Django:

- **Controller:** In web frameworks, the controller is often associated with the view functions or methods that handle HTTP requests and map them to appropriate actions or services.

- **Service:** Services can be classes or modules that encapsulate specific business logic. They might handle operations like authentication, payment processing, or user profile management.

- **DAO:** In the context of a web application, the DAO pattern might be implemented using object-relational mappers (ORMs) like SQLAlchemy in Flask or Django's built-in ORM. These ORMs abstract the database operations and provide a consistent way to interact with the database.

Remember that while these terms have specific meanings in the context of certain architectural patterns, their exact usage can vary based on the application's structure and the design decisions made by the development team.

## 2. Importance of file

Files are an essential part of programming and have significant importance in Python for various reasons:

1. **Data Persistence:** Files allow you to store data beyond the runtime of a program. This enables data to be preserved between program executions, providing data persistence.

2. **Input and Output:** Files are used for input and output operations. Programs often need to read data from files (input) or write data to files (output) as part of their functionality.

3. **Data Storage:** Files provide a way to store data in structured formats (e.g., text, JSON, XML, CSV) and unstructured formats (e.g., binary). This is vital for handling different types of data.

4. **Configuration Management:** Configuration files store settings and preferences for applications. Reading and modifying configuration files allow programs to be customized without changing the code.

5. **Logging:** Files are commonly used for logging program activities, errors, and debugging information. This helps in troubleshooting and improving program quality.

6. **Data Analysis:** Files are used to store and manipulate large datasets. Data analysis libraries like pandas enable efficient data processing directly from files.

7. **Collaboration:** Files facilitate data exchange and collaboration among different programs or users. This is particularly important in complex projects involving multiple components.

8. **Resource Storage:** Files store various types of resources, such as images, audio, and video files, used by applications.

9. **Database Backup:** Files are used to back up databases, ensuring data integrity in case of system failures.

10. **Report Generation:** Files are used to generate reports by collecting and formatting data in a presentable manner.

11. **Archiving:** Files can be used to archive data or compress files for storage and sharing.

12. **Web Development:** Files are crucial for web development, including serving static assets (HTML, CSS, JavaScript), uploading and downloading files, and managing user data.

Python provides built-in functions and libraries for efficient file handling, such as `open()`, context managers (`with` statement), and various file modes (read, write, append, binary). Proper file handling enhances program reliability, data integrity, and interaction with external data sources.

## 3. Different files in general

In general, there are various types of files used in computing, each serving a specific purpose and format. Here are some common types of files:

1. **Text Files:** These contain human-readable text and are often used for configuration, code, documentation, and data storage. Examples include `.txt`, `.csv`, `.json`, `.xml`.

2. **Binary Files:** These contain data in a format that is not directly readable by humans. They are used for storing multimedia, executable programs, and other complex data structures. Examples include images (`.jpg`, `.png`), audio (`.mp3`, `.wav`), and executables (`.exe`, `.dll`).

3. **Document Files:** These contain formatted text and graphics and are often used for creating documents, reports, presentations, and spreadsheets. Examples include `.docx`, `.pdf`, `.pptx`, `.xlsx`.

4. **Archive Files:** These store multiple files and directories in a compressed format. They are used for bundling and transferring data efficiently. Examples include `.zip`, `.tar`, `.rar`.

5. **Database Files:** These store structured data in a database format, allowing efficient storage and retrieval of information. Examples include `.sqlite`, `.db`, `.mdb`.

6. **Configuration Files:** These contain settings and preferences for applications. They allow users to customize program behavior without altering the code. Examples include `.ini`, `.cfg`, `.yaml`.

7. **Log Files:** These record events, activities, and errors generated by applications. They are essential for troubleshooting and debugging. Examples include `.log`, `.txt`.

8. **Web Files:** These are used for web development and include HTML files (`.html`), CSS files (`.css`), JavaScript files (`.js`), and more.

9. **Font Files:** These store font data used for displaying text in different styles and sizes. Examples include `.ttf`, `.otf`.

10. **Executable Files:** These are programs that can be run by the operating system. They contain machine code instructions. Examples include `.exe`, `.sh`, `.py`.

11. **Backup Files:** These are copies of original files created for data protection. They ensure data recovery in case of loss or corruption. Examples include `.bak`, `.backup`.

12. **Virtual Disk Images:** These contain the complete contents of a storage device and are used for creating virtual machines. Examples include `.iso`, `.vdi`, `.vmdk`.

13. **Compressed Files:** These are files that have been reduced in size to save storage space and speed up file transfer. Examples include `.gz`, `.bz2`, `.xz`.

14. **Font Files:** These contain fonts that are used for text rendering in documents and applications. Examples include `.ttf`, `.otf`.

15. **Configuration Files:** These store settings and preferences for applications. Examples include `.ini`, `.cfg`, `.yaml`.

These are just a few examples of the many types of files used in computing. Each type serves a specific purpose and is designed to accommodate different kinds of data and information.

## 4. Different file handling operations:

- `r`:	Opens a file for reading. (default)
- `a`:	Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
- `w`:	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
- `r+`: Reads and writes data into file. Previous data will not be deleted.
- `a+`: Appends and reads data of file. If file does not exists,will create new file and writes data
- `w+`: Writes and reads data of file. Previous data in the file will be deleted.
- `x`:	Opens a file for exclusive creation. If the file already exists, the operation fails.
- `t`:	Opens in text mode. (default)
- `b`:	Opens in binary mode.
- `+`:	Opens a file for updating (reading and writing)

[File Handlin](https://ncert.nic.in/textbook/pdf/lecs102.pdf)

## 5. Give example of reading, writing and updating a txt file

**Reading a text file:**

Assume you have a text file named "read_data.txt" with the following content:

```
Hello World. This is a Python test file. Python is amazing.
```

You can read the text file by using the following code:

  ```
  my_file = open("read_data1.txt", 'r')
  f_data = my_file.read()
  print(f_data)

  counter = 0
  for line in f_data.split(" "):
      if "Python" in line:
          counter += 1

  print("Python word repeated times in file:", counter)

  my_file.close()

  # The output will be:
  # Hello World. This is a Python test file. Python is amazing.
  # Python word repeated times in file: 2
  ```

Assume you have a text file named "data.txt" with the following content:

```
Line 1: Hello, world!
Line 2: This is a text file.
```

You can read the text file line by line using the following code:

  ```python
  with open("data.txt", "r") as file:
      lines = file.readlines()
      for line in lines:
          print(line.strip())  # strip() to remove newline characters

  # Output is:
  Line 1: Hello, world!
  Line 2: This is a text file.
  ```

**Writing to a text file**

You can write new content to a text file using the following code:

  ```python
  new_content = [
      "New line 1: Added through Python",
      "New line 2: Writing to text files"
  ]

  with open("data.txt", "w") as file:
      for line in new_content:
          file.write(line + "\n")

  print("Data written to new_data.txt")
 
  Output:
  A "data.txt" file with the following content is created.
  New line 1: Added through Python
  New line 2: Writing to text files
  ```

**Update a text file**

You can read the existing content of a text file, update it, and then write the updated content back to the file:

Consider a `data.txt` file with the following contents:

```
New line 1: Added through Python
New line 2: Writing to text files
New line 3: Hello world!
```

  ```python
  updated_content = []

  with open("data.txt", "r") as file:
      lines = file.readlines()
      for line in lines:
          updated_line = line.replace("world", "Python")
          updated_content.append(updated_line)

  with open("data.txt", "w") as file:
      file.writelines(updated_content)

  print("Text file updated and written back to data.txt")

  # The file after updating is:
  New line 1: Added through Python
  New line 2: Writing to text files
  New line 3: Hello Python!
```

## 6. Give example of reading, writing and updating a csv file

Exchanging information through text files is a common way to share info between programs. One of the most popular formats for exchanging data is the CSV format. 
The Python [csv library](https://docs.python.org/3/library/csv.html) will work for most cases. If your work requires lots of data or numerical analysis, the [pandas library](http://pandas.pydata.org/) has CSV parsing capabilities as well, which should handle the rest.

A CSV file (Comma Separated Values file) is a type of plain text file that uses specific structuring to arrange tabular data. Because it’s a plain text file, it can contain only actual text data—in other words, printable ASCII or Unicode characters.

The structure of a CSV file is given away by its name. Normally, CSV files use a comma to separate each specific data value. Here’s what that structure looks like:

```
column 1 name,column 2 name, column 3 name
first row data 1,first row data 2,first row data 3
second row data 1,second row data 2,second row data 3
...
```

Notice how each piece of data is separated by a comma. Normally, the first line identifies each piece of data — in other words, the name of a data column. Every subsequent line after that is actual data and is limited only by file size constraints.

In general, the separator character is called a delimiter, and the comma is not the only one used. Other popular delimiters include the tab (\t), colon (:) and semi-colon (;) characters. Properly parsing a CSV file requires us to know which delimiter is being used.

CSV files are very easy to work with programmatically. Any language that supports text file input and string manipulation (like Python) can work with CSV files directly.


Let's read a `data.csv` file with the following content:

```
a, b, c, d, e
```

```
import csv

# Reading a CSV File
with open('data.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# The output is:
['a', ' b', ' c', ' d', ' e']
```

Let's read the data.txt file with the csv module in python:

```
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March
```

To read the data:

  ```
  import csv

  with open('data.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
          if line_count == 0:
              print(f'Column names are {", ".join(row)}')
              line_count += 1
          else:
              print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
              line_count += 1

      print(f'Processed {line_count} lines.')
  ```


The output is:

  ```
  Column names are name, department, birthday month
	  John Smith works in the Accounting department, and was born in November.
	  Erica Meyers works in the IT department, and was born in March.
  Processed 3 lines.
  ```

**Reading CSV Files into a Dictionary With csv**

Rather than deal with a list of individual String elements, you can read CSV data directly into a dictionary (technically, an Ordered Dictionary) as well.

```
import csv

with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

# The output is:
Column names are name, department, birthday month
    John Smith works in the Accounting department, and was born in November.
    Erica Meyers works in the IT department, and was born in March.
Processed 3 lines.
```

The first line of the CSV file is assumed to contain the keys to use to build the dictionary. If you don’t have these in your CSV file, you should specify your own keys by setting the `fieldnames` optional parameter to a list containing them.


**Writing to a csv file**

You can also write to a CSV file using a `writer` object and the `.write_row()` method:

```
# Writing to a CSV File
data_to_write = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 22, 'Chicago']
]

with open('new_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_to_write)

# The output is:
Name,Age,City
Alice,25,New York
Bob,30,Los Angeles
Charlie,22,Chicago
```

**Writing CSV file from a dictionary with csv**

Since you can read our data into a dictionary, it’s only fair that you should be able to write it out from a dictionary as well:

```
import csv

with open('data.csv', mode='w', newline='') as csv_file:
    fieldnames = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})

# A new file, data.csv with the following output is created:
emp_name,dept,birth_month
John Smith,Accounting,November
Erica Meyers,IT,March
```

Unlike `DictReader`, the fieldnames parameter is required when writing a dictionary. Without a list of fieldnames, the `Dictwriter` can’t know which keys to use to retrieve values from your dictionaries. `Dictwriter` also uses the keys in fieldnames to write out the first row as column names.

Most CSV reading, processing, and writing tasks can be easily handled by the basic csv Python library. If you have a lot of data to read and process, the pandas library provides quick and easy CSV handling capabilities as well. 

Take an indepth look into [importing data using csv python library and pandas library](https://realpython.com/python-csv/#optional-python-csv-reader-parameters).

**Updating a csv file**

```
# Updating a CSV File
data_to_update = [
    ['Dave', 28, 'San Francisco'],
    ['Eve', 35, 'Seattle']
]

with open('new_data.csv', 'a', newline='') as file:  # Use 'a' mode to append to an existing file
    writer = csv.writer(file)
    writer.writerows(data_to_update)

# Reading the Updated CSV File
with open('new_data.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```


## 7. Read, write and update a `json` file

- Javascript Object Notation (JSON) is a script (executable) file which is made of text in a programming language and it is used to store and transfer the data.
- JSON is language independent and because of that, it is used for storing or transferring data in files.  
- Python supports JSON through a built-in package called JSON.
- To use this feature, we import the JSON package in Python script. The text in JSON is done through quoted-string which contains the value in key-value mapping within `{ }`.
- To handle the data flow in a file, the JSON library in Python uses `dump()` or `dumps()` function to convert the Python objects into their respective JSON object, so it makes it easy to write data to files.

**Serializing and deserializing complex JSON data**

- The conversion of data from JSON object string is known as [Serialization](https://www.geeksforgeeks.org/serialize-and-deserialize-complex-json-in-python/) and its opposite string JSON object is known as Deserialization. 
- Serializing JSON refers to the transformation of data into a series of bytes (hence serial) to be stored or transmitted across a network.
- JSON Object is defined using curly braces `{}` and consists of a key-value pair. It is important to note that the JSON object key is a string and its value can be any primitive(e.g. int, string, null) or complex data types(e.g. array).
- To handle the data flow in a file, the JSON library in Python uses `dump()` or `dumps()` function to convert the Python objects into their respective JSON object, so it makes it easy to write data to files.

A list of python and json objects are given below:

| Python Objects      | JSON Objects |
| ----------- | ----------- |
| Dict      | Object       |
| list, tuple   | array       |
| str   | string   |
| int, long, float	|  numbers	|
| True	| true	|
| False	| false	|
| None	| null	|


1. **Writing a JSON File:**

**Method 1: Writing JSON to a file in Python using `json.dumps()`** 

The JSON package in Python has a function called `json.dumps()` that helps in converting a dictionary to a JSON object. It takes two parameters:

- `dictionary` – the name of a dictionary which should be converted to a JSON object.
- `indent` – defines the number of units for indentation

After converting the dictionary to a JSON object, simply write it to a file using the `write` function:

```
import json

# Data to be written
dictionary = {
    "name": "samuel",
    "emp_id": 7,
    "salary": 50000,
    "ph_no": "9123203986"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("data.json", "w") as outfile:
	outfile.write(json_object)

# Output:
A data.json file with the following output is created:
{"name": "samuel", "emp_id": 7, "salary": 50000, "ph_no": "9123203986"}
```

**Method 2: Writing JSON to a file in Python using `json.dump()`**

- Another way of writing JSON to a file is by using `json.dump()` method.
- The JSON package has the `dump` function which directly writes the dictionary to a file in the form of JSON, without needing to convert it into an actual JSON object.
- It takes 2 parameters:
  - `dictionary` – the name of a dictionary which should be converted to a JSON object.
  - `file pointer` – pointer of the file opened in write or append mode.

```
import json

# Data to be written
dictionary = {
    "name": "samuel",
    "emp_id": 7,
    "salary": 50000,
    "ph_no": "9123203986"
}

with open("data.json", "w") as outfile:
    json.dump(dictionary, outfile)

# Output:
A data.json file with the following output is created:
{"name": "samuel", "emp_id": 7, "salary": 50000, "ph_no": "9123203986"}
```

2. **Reading a JSON File:**

- The `load` method is used for deserialization, i.e. conversion of JSON objects into their respective Python objects.
- If you have used JSON data from another program or obtained it as a string format of JSON, then it can easily be deserialized with `load()`, which is usually used to load from a string, otherwise, the root object is in a list or Dict.

**Reading JSON from a file using `json.load()`**

- The JSON package has `json.load()` function that loads the JSON content from a JSON file into a dictionary. It takes one parameter:
- **File pointer:** A file pointer that points to a JSON file.

Assume you have a JSON file named "data.json" with the following content:

```json
{
    "name": "samuel",
    "emp_id": 007,
    "salary": 50000,
    "ph_no": "9123203986"
}
```

You can read and parse the JSON data using the following code:

```python
import json

# Opening JSON file
with open('data.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))

# Output: The console give the output
{'name': 'samuel', 'emp_id': 7, 'salary': 50000, 'ph_no': '9123203986'}
<class 'dict'>
```

3. **Updating a JSON File:**

You can read the existing JSON data, update it, and then write the updated data back to the file using the following code:

```python
with open("data.json", "r") as file:
    existing_data = json.load(file)

existing_data["age"] = 26
existing_data["city"] = "Bangalore"

with open("data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

print("JSON data updated and written back to data.json")

# Output:
The file is updated as:
{
    "name": "samuel",
    "emp_id": 7,
    "salary": 50000,
    "ph_no": "9123203986",
    "age": 26,
    "city": "Bangalore"
}
```

## Give example of reading, writing and updating excel files

- Nearly 54% of businesses use Excel to perform arithmetic operations, analyze data, create visualizations, and generate reports. You can also perform predictive modeling tasks like regression and clustering using Excel.

- However, despite Excel’s undisputed strengths, the tool comes with its own set of drawbacks, making it, at times, inefficient when performing specific tasks involving huge datasets. 

- One limitation of Excel is its inability to handle large amounts of data. You can run into serious performance issues when trying to perform complex operations on a lot of data entries in Excel, especially if your formulas and macros are not optimized for performance.

- Excel can also become very time-consuming if you need to perform repetitive tasks. For instance, if you need to replicate an analysis on multiple Excel files every week, you would have to open them manually and copy-paste the same formulas over and over.

- These drawbacks can be solved by automating Excel workflows with Python. Tasks like spreadsheet consolidation, data cleaning, and predictive modeling can be done in minutes using a simple Python script that writes to an Excel file.

- Excel users can also create a scheduler in Python that runs the script automatically at different time intervals, dramatically reducing the amount of human intervention required to perform the same task again and again.

- Some common operations that python can be used to perform on excel are:
  - Read and write Excel files using Python
  - Create arithmetic operations and Excel formulas
  - Manipulate Excel worksheets
  - Build visualizations in Python and save them to an Excel file
  - Format Excel cell colors and styles using Python
 
**OpenPyxl**

- Openpyxl is a Python library that allows users to read Excel files and write to them. 
- This framework can help you write functions, format spreadsheets, create reports, and build charts directly in Python without even having to open an Excel application.
- Furthermore, Openpyxl allows users to iterate through worksheets and perform the same analysis on multiple sets of data at the same time.

**Reading excel file in python with Openpyxl**

**1. Loading the workbook with Openpyxl**

The `load_workbook()` function from the openpyxl module loads the excel workbook. It allows the user to access and manipulate the data in the Excel file using Python.

```
import openpyxl 
wb = openpyxl.load_workbook('file.xlsx')
```

After loading, simply call the active worksheet, which is the first sheet in the workbook, using the following line of code as:

```
ws = wb.active
```

If you know the name of the worksheet, you can also access it by its name. We will be using the “sheet1”:

```
ws = wb['sheet1']
```

Count the number of rows and columns in this worksheet:
- To find the maximum number of rows and columns in the worksheet `ws`, use `ws.max_row` and `ws.max_column` functions. The `str()` function is used to convert the integer values returned by `ws.max_row` and `ws.max_column` into strings so that they can be concatenated with the rest of the string.

```
print('Total number of rows: '+str(ws.max_row)+'. And total number of columns: '+str(ws.max_column))
```

**2. Reading Data From a Cell**

To retrieve data from a specific cell with Openpyxl, you can type the cell’s value in like this:

```
print('The value in cell A1 is: '+ws['A1'].value)
```

**3. Reading Data From Multiple Cells**

To print all cell values in a certain row of the spreadsheet, you can write a simple `for loop` to iterate through all the values in a specific row:

```
values = [ws.cell(row=1,column=i).value for i in range(1,ws.max_column+1)]
print(values)
```

The above code will print all the values in the first row.

To print the first 10 rows from Column 1 to Column 6:

```
# reading data from a range of cells (from column 1 to 6)

my_list = list()

for value in ws.iter_rows(
    min_row=1, max_row=11, min_col=1, max_col=6, 
    values_only=True):
    my_list.append(value)
    
for ele1,ele2,ele3,ele4,ele5,ele6 in my_list:
    (print ("{:<8}{:<35}{:<10}
             {:<10}{:<15}{:<15}".format(ele1,ele2,ele3,ele4,ele5,ele6)))
```

- The `iter_rows()` method takes in the parameters `min_row`, `max_row`, `min_col`, and `max_col` to specify the range of cells to read from.
- The `values_only=True` parameter ensures that only the values of the cells are returned, not any formatting or other metadata.
- The `<` symbol is used to left-align the values within their respective columns, and the `{:8}` syntax specifies the width of each column.

**4. Writing to excel files**

**4.1 Writing to a cell**:
- You can access a cell directly, using its key, `ws['K1'] = 'Sum of Sales'`. The string `'Sum of Sales'` gets assigned to the cell `K1`.
- Alternatively, you can specify the row and column position of the cell that you’d like to write to, `ws.cell(row=1, column=11, value = 'Sum of Sales')`. The `cell()` method is used to specify the cell to write to.
- Every time you write to an Excel file with Openpyxl, you need to save your changes with the following line of code or they will not be reflected in the worksheet, `wb.save('filename.xlsx')`.
- Make sure to close the Excel file before saving your changes. You can then open it again to make sure that the change is reflected in your worksheet.

**4.2 Creating a New Column**

Let’s add the sum of sales in every region and write it to column `K`. We will do this for the sales data in the first row:

```
row_position = 2
col_position = 7

total_sales = ((ws.cell(row=row_position, column=col_position).value)+
               (ws.cell(row=row_position, column=col_position+1).value)+
               (ws.cell(row=row_position, column=col_position+2).value)+
               (ws.cell(row=row_position, column=col_position+3).value))

ws.cell(row=2,column=11).value=total_sales
wb.save('videogamesales.xlsx')
```

**4.3 Appending new rows**

To append a new row to the workbook, simply create a tuple with the values you’d like to include and write it to the sheet:

```
new_row = (1,'The Legend of Zelda',1986,'Action','Nintendo',3.74,0.93,1.69,0.14,6.51,6.5)

ws.append(new_row)
    
wb.save('videogamesales.xlsx')
```

You can confirm that this data has been appended by printing the last row in the workbook:

```
values = [ws.cell(row=ws.max_row,column=i).value for i in range(1,ws.max_column+1)]
print(values)
```

- This code uses list comprehension to extract the values of all cells in the last row of a worksheet *ws* in a spreadsheet.
- The `range()` function generates a sequence of numbers from 1 to the maximum number of columns in the worksheet `ws`.
- The `ws.max_column` attribute returns the maximum number of columns in the worksheet.
- The `ws.cell()` method returns the cell object at the specified row and column.
- In this case, it returns the cell object at the last row and the current column in the loop.
- The value attribute of the cell object returns the value of the cell.
- The list comprehension creates a list of values by iterating over the range of columns and extracting the value of each cell in the last row.
- The resulting list is assigned to the variable values.
- Finally, the `print()` function is used to display the list of values.

The following output will be generated:

```
[1, 'The Legend of Zelda', 1986, 'Action', 'Nintendo', 3.74, 0.93, 1.69, 0.14, 6.51, 6.5]
```

**4.4 Deleting rows**

To delete the new row we just created, you can run the following line of code:

```
ws.delete_rows(ws.max_row, 1) # row number, number of rows to delete

wb.save('videogamesales.xlsx')
```

- [DataCamp - Reading, writing and updating excel sheets](https://www.datacamp.com/tutorial/python-excel-tutorial)
- [FreeCodeCamp- Reading, writing and updating excel sheets](https://www.freecodecamp.org/news/how-to-create-read-update-and-search-through-excel-files-using-python-c70680d811d4/)

## Give example of reading, writing and updating zip files

ZIP is an archive file format that supports lossless data compression. By lossless compression, we mean that the compression algorithm allows the original data to be perfectly reconstructed from the compressed data. So, a ZIP file is a single file containing one or more compressed files, offering an ideal way to make large files smaller and keep related files together.

ZIP files are mainly used to:
- To reduce storage requirements.
- To improve transfer speed over standard connections.

The inbuilt [zipfile](https://docs.python.org/3.11/library/zipfile.html) module provided by Python is used to work with zip files.

[GFG](https://www.geeksforgeeks.org/working-zip-files-python/), [Real Python](https://realpython.com/python-zipfile/)

## Give example of reading, writing and updating pdf files

[DataCamp] - (https://www.datacamp.com/tutorial/reading-and-editing-pdfs-and-word-documents-from-python)


## Give example of reading, writing and updating xml files



## 7. File open modes

In Python, the `open()` function is used to open files. It takes two arguments: the file name and the file mode. The file mode specifies the purpose of opening the file, such as reading, writing, or appending. Here are the different file open modes:

1. **'r' (Read Mode):** Opens the file for reading (default mode). Raises an error if the file doesn't exist.

```python
with open('file.txt', 'r') as f:
    content = f.read()
```

2. **'w' (Write Mode):** Opens the file for writing. Creates a new file if it doesn't exist, or truncates the existing file.

```python
with open('file.txt', 'w') as f:
    f.write('Hello, world!')
```

3. **'a' (Append Mode):** Opens the file for appending data. Creates a new file if it doesn't exist.

```python
with open('file.txt', 'a') as f:
    f.write(' Appending new content.')
```

4. **'x' (Exclusive Creation Mode):** Opens the file for writing, but only if the file doesn't already exist.

```python
with open('file.txt', 'x') as f:
    f.write('Creating a new file.')
```

5. **'b' (Binary Mode):** Opens the file in binary mode, allowing you to read or write binary data.

```python
with open('image.png', 'rb') as f:
    binary_data = f.read()
```

6. **'t' (Text Mode):** Opens the file in text mode (default mode), allowing you to read or write text data.

```python
with open('file.txt', 'rt') as f:
    text_content = f.read()
```

7. **'+' (Read and Write Mode):** Opens the file for both reading and writing.

```python
with open('file.txt', 'r+') as f:
    content = f.read()
    f.write('Adding new content.')
```

Sure, let's go through examples of file open modes using `w+`, `a+`, and `r+`:

8. **`w+` Mode - Write and Read:**

The `w+` mode opens a file for writing and reading. If the file exists, it will be truncated (emptied), and if it doesn't exist, a new file will be created. You can both write and read from the file.

```python
# Writing and reading using w+ mode
with open("write_read_file.txt", "w+") as file:
    file.write("Hello, world!\n")
    file.seek(0)  # Go back to the beginning of the file
    content = file.read()

print("Content:", content)
```

9. **`a+` Mode - Append and Read:**

The `a+` mode opens a file for appending and reading. If the file exists, new data will be appended at the end, and if it doesn't exist, a new file will be created. You can both append new content and read the file.

```python
# Appending and reading using a+ mode
with open("append_read_file.txt", "a+") as file:
    file.write("This is appended content.\n")
    file.seek(0)  # Go back to the beginning of the file
    content = file.read()

print("Content:", content)
```

10. **`r+` Mode - Read and Write:**

The `r+` mode opens a file for both reading and writing. If the file exists, you can read and write to it without truncating it. If it doesn't exist, you'll get a `FileNotFoundError`.

```python
# Reading and writing using r+ mode
with open("read_write_file.txt", "r+") as file:
    content = file.read()
    file.write("\nThis is added using r+ mode.")

print("Content:", content)
```

Please note that when using the `write` method, it will overwrite existing content and write new content from the current file position. You might need to use the `seek` method to move the file pointer if you want to read content after writing or vice versa. Also, remember that opening files in modes that allow both writing and reading can have some complexities in terms of file pointer positioning, so be cautious when using them.

It's important to note that combining modes is possible, such as `'rb'` for reading binary files or `'a+'` for reading and appending. When using the `open()` function with the `with` statement, the file is automatically closed when the block is exited, ensuring proper resource management.


## 9. Give example open, read-write-append, close without exception handling

Let's look at an example of how to open a file, write content to it, and close the file without using explicit exception handling:

```python
# Opening a file, writing content, and closing the file without exception handling
file = open("example.txt", "w")  # Open the file in write mode
file.write("Hello, world!\n")    # Write content to the file
file.close()                     # Close the file

print("File closed.")
```

In this example:

- The `open` function is used to open a file named "example.txt" in write mode (`"w"`).
- The `write` method is used to write the string "Hello, world!\n" to the file.
- The `close` method is called to close the file.

Another example of opening a file, reading from it, writing to it, appending to it, and closing the file without explicit exception handling:

```python
# Opening a file, reading from it, writing to it, appending to it, and closing the file without exception handling
file = open("example.txt", "r+")  # Open the file in read and write mode

# Reading from the file
content = file.read()
print("Content read from the file:", content)

# Writing to the file
file.write("This is new content written using r+ mode.\n")

# Appending to the file
file.write("This is appended content using r+ mode.\n")

file.close()  # Close the file

print("File closed.")
```

In this example:

- The `open` function is used to open a file named "example.txt" in read and write mode (`"r+"`).
- The `read` method is used to read the entire content of the file.
- The `write` method is used to write new content to the file (overwriting some of the existing content) and to append content to the end of the file.
- The `close` method is used to close the file.

However, it's important to note that not using explicit exception handling can leave your code vulnerable to errors. If an exception occurs while working with files (e.g., if the file cannot be opened due to permissions, or if there's an issue with writing), your program might terminate unexpectedly. Therefore, it's a good practice to include exception handling when working with files to ensure that your code is robust and can handle unexpected situations gracefully.

## 10. Give examples of open, write and close a file using exception handling

Certainly! Here's an example of how to open a file, write content to it, and close the file with proper exception handling:

```python
try:
    # Opening a file, writing content, and closing the file with exception handling
    file = open("example.txt", "w")  # Open the file in write mode
    file.write("Hello, world!\n")    # Write content to the file
except IOError as io:
    print("An error occurred:", io)
except FileNotFoundError as fnf:
    print("File not found at specified path", fnf)
except Exception as e:
    print("An exception occured:", e)
finally:
    file.close()  # Close the file if no exception occurred
    print("File closed.")
```

In this example:

- The `try` block is used to enclose the code that may raise an exception.
- Inside the `try` block, the `open` function is used to open a file named "example.txt" in write mode (`"w"`).
- The `write` method is used to write the string "Hello, world!\n" to the file.
- If an `IOError` (or any exception related to file I/O) occurs, the `except` block is executed, which prints an error message.
- If no exception occurs, the `else` block is executed, and the `close` method is called to close the file. `else` can be used in place of `finally`.

By using exception handling, your code can handle errors gracefully and provide meaningful error messages to help identify and diagnose any issues that may arise during file operations.

Another example of opening a file, reading from it, writing to it, appending to it, and closing the file with proper exception handling:

```python
try:
    # Opening a file, reading from it, writing to it, appending to it, and closing the file with exception handling
    file = open("example.txt", "r+")  # Open the file in read and write mode

    try:
        # Reading from the file
        content = file.read()
        print("Content read from the file:", content)

        # Writing to the file
        file.write("This is new content written using r+ mode.\n")

        # Appending to the file
        file.write("This is appended content using r+ mode.\n")

    except IOError as e:
        print("An error occurred during file operations:", e)
    finally:
        file.close()  # Close the file in the finally block to ensure it's closed regardless of exceptions

except IOError as e:
    print("An error occurred when opening the file:", e)

print("File handling completed.")
```

In this example:

- The outer `try` block is used to handle any potential issues that might occur when opening the file.
- Inside the outer `try` block, the inner `try` block is used to enclose the code that performs reading, writing, and appending to the file. If any exception occurs during these operations, the inner `except` block is executed.
- The `finally` block is used to close the file, ensuring it's closed regardless of whether an exception occurred during the inner operations.
- If there's an exception when opening the file, the outer `except` block handles that exception.

By using exception handling in multiple levels (both for file opening and file operations), your code can handle errors gracefully and provide meaningful error messages to help identify and diagnose any issues that may arise during file handling.

# 11. Open, write and close a file using functions

Certainly! Here are examples of how to create functions to open, write to, and close a file in Python:

**Opening, Writing, and Closing a File Using Functions:**

```python
def open_write_close_file(filename, content):
    try:
        file = open(filename, "w")  # Open the file in write mode
        file.write(content)         # Write content to the file
    except IOError as e:
        print("An error occurred:", e)
    finally:
        file.close()               # Close the file

# Usage
filename = "output.txt"
content_to_write = "Hello, this is written using a function."
open_write_close_file(filename, content_to_write)
print("File handling using functions completed.")
```

In this example:

- The `open_write_close_file` function takes a filename and content as arguments.
- Inside the function, it attempts to open the file in write mode, write the content, and close the file.
- Proper exception handling is included to catch potential errors.

Remember that using functions like this is a good way to encapsulate file handling logic and improve code organization and readability.

Another example of how to create functions to open a file, read from it, write to it, append to it, and close the file in Python:

```python
def open_file(filename, mode):
    try:
        file = open(filename, mode)
        return file
    except IOError as e:
        print("An error occurred when opening the file:", e)
        return None

def read_from_file(file):
    content = file.read()
    return content

def write_to_file(file, content):
    try:
        file.write(content)
    except IOError as e:
        print("An error occurred when writing to the file:", e)

def append_to_file(file, content):
    try:
        file.write(content)
    except IOError as e:
        print("An error occurred when appending to the file:", e)

def close_file(file):
    file.close()

# Usage
filename = "example.txt"
content_to_write = "This is new content."
content_to_append = "This is appended content."

# Open file, write, append, and close using functions
file = open_file(filename, "r+")
if file:
    content = read_from_file(file)
    print("Content read from the file:", content)

    write_to_file(file, content_to_write)
    append_to_file(file, content_to_append)

    close_file(file)
    print("File handling using functions completed.")
```

In this example:

- Separate functions are defined to encapsulate different aspects of file handling: opening the file, reading from the file, writing to the file, appending to the file, and closing the file.
- The functions handle exception cases and return appropriate values.
- By using these functions, you can handle different file operations in a more modular and organized manner.

Using functions like these can make your code more maintainable and readable, as well as provide a structured way to handle file operations with proper exception handling.

## 12. Give example to open, write and close a file using OOPs concept of instance method

An example of using OOPs concept instance method:
```
class FileHandling:
    def __init__(self, file_obj):
        self.file_obj = file_obj

    def write_data(self, in_data, mode):
        try:
            file_obj = open(self.file_obj, mode)
            print("File type ", file_obj, type(file_obj))
            file_obj.write(in_data)  # TextIOWrapper.write(my_file,in_data)
        except FileNotFoundError as fnf:
            print("File not found at specified path")
            print(fnf)
        finally:
            # condition to check whether object my_file exists or not
            file_obj.close()

    def read_data(self, mode):
        f_obj = open(self.file_obj,mode)
        data = f_obj.read()
        print("Read data : ", data)
        f_obj.close()

myfile = FileHandling("write_data.txt") # C:/Users/uname/Desktop/write_data4.txt
data = 'Hello world. This is my fourth file using oops concepts'
myfile.write_data(data, 'w')
myfile.read_data('r')

# Output:
File type  <_io.TextIOWrapper name='write_data.txt' mode='w' encoding='cp1252'> <class '_io.TextIOWrapper'>
Read data :  Hello world. This is my fourth file using oops concepts
```

Example of how to create a class with instance methods to open a file, write to it, and close the file using object-oriented programming (OOP) concepts:

```python
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def open_file(self, mode):
        try:
            self.file = open(self.filename, mode)
            print(f"File '{self.filename}' opened in {mode} mode.")
        except IOError as e:
            print("An error occurred when opening the file:", e)
    
    def write_to_file(self, content):
        try:
            self.file.write(content)
            print("Content written to the file.")
        except AttributeError:
            print("File not opened. Call open_file() first.")
        except IOError as e:
            print("An error occurred when writing to the file:", e)
    
    def close_file(self):
        if self.file:
            self.file.close()
            print("File closed.")
        else:
            print("File is not open.")

# Usage
filename = "oop_example.txt"
content_to_write = "This is content written using OOP."

# Creating an instance of FileHandler
file_handler = FileHandler(filename)

# Opening, writing, and closing using instance methods
file_handler.open_file("w")
file_handler.write_to_file(content_to_write)
file_handler.close_file()

print("File handling using OOP instance methods completed.")
```

In this example:

- The `FileHandler` class is defined with instance methods to open a file, write to it, and close the file.
- The constructor `__init__` initializes the filename and sets the `file` attribute to `None`.
- The `open_file`, `write_to_file`, and `close_file` methods are instance methods that perform their respective file operations.
- Proper exception handling is included in each method.

By using OOP concepts and instance methods, you can encapsulate file handling logic within a class, making your code more organized and modular.

Another example of using object-oriented programming (OOP) concepts to create a class with instance methods for opening, reading from, writing to, appending to, and closing a file:

```python
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def open_file(self, mode):
        try:
            self.file = open(self.filename, mode)
            print(f"File '{self.filename}' opened in {mode} mode.")
        except IOError as e:
            print("An error occurred when opening the file:", e)
    
    def read_from_file(self):
        try:
            content = self.file.read()
            print("Content read from the file:", content)
        except AttributeError:
            print("File not opened. Call open_file() first.")
        except IOError as e:
            print("An error occurred when reading from the file:", e)
    
    def write_to_file(self, content):
        try:
            self.file.write(content)
            print("Content written to the file.")
        except AttributeError:
            print("File not opened. Call open_file() first.")
        except IOError as e:
            print("An error occurred when writing to the file:", e)
    
    def append_to_file(self, content):
        try:
            self.file.write(content)
            print("Content appended to the file.")
        except AttributeError:
            print("File not opened. Call open_file() first.")
        except IOError as e:
            print("An error occurred when appending to the file:", e)
    
    def close_file(self):
        if self.file:
            self.file.close()
            print("File closed.")
        else:
            print("File is not open.")

# Usage
filename = "oop_file_example.txt"
content_to_write = "This is content written using OOP."
content_to_append = "\nThis is appended content using OOP."

# Creating an instance of FileHandler
file_handler = FileHandler(filename)

# Opening, reading, writing, appending, and closing using instance methods
file_handler.open_file("r+")
file_handler.read_from_file()
file_handler.write_to_file(content_to_write)
file_handler.append_to_file(content_to_append)
file_handler.close_file()

print("File handling using OOP instance methods completed.")
```

In this example:

- The `FileHandler` class is defined with instance methods to open a file, read from it, write to it, append to it, and close the file.
- The constructor `__init__` initializes the filename and sets the `file` attribute to `None`.
- Each method includes proper exception handling to handle potential errors.
- By using OOP principles, you can create a more organized and modular approach to file handling in your code.

## 13. Open, write and close a file using OOPs concept static method

An example of using OOPs static method concept to handle file

```
class FileHandling:

    @staticmethod
    def write_data(file_path, in_data):
        try:
            file_obj = open(file_path, 'w+')  
            file_obj.write(in_data)           
        except FileNotFoundError as fnf:
            print("File not found at specified path", fnf)
        finally:
            file_obj.close()                   

file_p = "write_data5.txt"
data = 'Fifth file using static method in oops'
FileHandling.write_data(file_p, data)
```

An example of how to create a class with static methods to open a file, write to it, and close the file using object-oriented programming (OOP) concepts:

```python
class FileHandler:
    @staticmethod
    def open_file(filename, mode):
        try:
            file = open(filename, mode)
            print(f"File '{filename}' opened in {mode} mode.")
            return file
        except IOError as e:
            print("An error occurred when opening the file:", e)
            return None
    
    @staticmethod
    def write_to_file(file, content):
        try:
            file.write(content)
            print("Content written to the file.")
        except AttributeError:
            print("File is not open.")
        except IOError as e:
            print("An error occurred when writing to the file:", e)
    
    @staticmethod
    def close_file(file):
        if file:
            file.close()
            print("File closed.")
        else:
            print("File is not open.")

# Usage
filename = "oop_static_example.txt"
content_to_write = "This is content written using OOP static methods."

# Opening, writing, and closing using static methods
file = FileHandler.open_file(filename, "w")
if file:
    FileHandler.write_to_file(file, content_to_write)
    FileHandler.close_file(file)

print("File handling using OOP static methods completed.")
```

In this example:

- The `FileHandler` class is defined with static methods to open a file, write to it, and close the file.
- Static methods don't require an instance of the class to be called; you can call them directly on the class itself.
- The `open_file` method accepts a filename and mode as arguments and returns the opened file (or `None` in case of an error).
- The `write_to_file` and `close_file` methods accept the file object as an argument.
- Proper exception handling is included in each static method.

Using static methods in a class is useful when you have methods that don't require access to instance-specific data but are still logically related to the class's functionality.

```
class FileHandler:
    @staticmethod
    def open_file(filename, mode):
        try:
            file = open(filename, mode)
            print(f"File '{filename}' opened in {mode} mode.")
            return file
        except IOError as e:
            print("An error occurred when opening the file:", e)
            return None
    
    @staticmethod
    def read_from_file(file):
        try:
            content = file.read()
            print("Content read from the file:", content)
        except AttributeError:
            print("File is not open.")
        except IOError as e:
            print("An error occurred when reading from the file:", e)
    
    @staticmethod
    def write_to_file(file, content):
        try:
            file.write(content)
            print("Content written to the file.")
        except AttributeError:
            print("File is not open.")
        except IOError as e:
            print("An error occurred when writing to the file:", e)
    
    @staticmethod
    def append_to_file(file, content):
        try:
            file.write(content)
            print("Content appended to the file.")
        except AttributeError:
            print("File is not open.")
        except IOError as e:
            print("An error occurred when appending to the file:", e)
    
    @staticmethod
    def close_file(file):
        if file:
            file.close()
            print("File closed.")
        else:
            print("File is not open.")

# Usage
filename = "oop_static_file_example.txt"
content_to_write = "This is content written using OOP static methods."
content_to_append = "\nThis is appended content using OOP static methods."

# Opening, reading, writing, appending, and closing using static methods
file = FileHandler.open_file(filename, "r+")
if file:
    FileHandler.read_from_file(file)
    FileHandler.write_to_file(file, content_to_write)
    FileHandler.append_to_file(file, content_to_append)
    FileHandler.close_file(file)

print("File handling using OOP static methods completed.")
```

## 14. Example of performing a read on a file

```
my_file = open("read_data1.txt", 'r')   # 1 # C:/Users/nette/Desktop/
f_data = my_file.read()   # 2
print(f_data)

word = input("Enter a word: ")
counter = 0
for line in f_data.split(" "):
    if word in line:
        counter += 1

print("Python word repeated times in file:", counter)

my_file.close()

# Output:
Hello World. This is a Python test file. Python is amazing.
Python word repeated times in file: 2
```

## 15. Perform a read using functions

```
def find_word_count(file, word):
    my_file = open(file, 'r')
    f_data = my_file.read()
    counter = 0
    for line in f_data.split(" "):
        if word in line:
            counter += 1

    return f"The word {word} appears {counter} times."

file = "read_data1.txt"
word = input("Enter the word to search: ")
print(find_word_count(file, word))
```

Example:
```
Enter the word to search: Python
The word Python appears 2 times.
```

## 16. Perform a read using exceptional handling

```
def find_word_count(file, word):
    try:
        with open(file, 'r') as my_file:
            f_data = my_file.read()
            counter = 0
            for line in f_data.split(" "):
                if word in line:
                    counter += 1
            return f"The word {word} appears {counter} times."
    except FileNotFoundError as fne:
        return "File not found: {fne}"
    except Exception as e:
        return f"An error occurred: {e}"

file = "read_data1.txt"
word = input("Enter the word to search: ")
result = find_word_count(file, word)
print(result)
```

## 17. Perform a read using OOPS instance method

```
class WordCounter:
    def __init__(self, file):
        self.file = file

    def find_word_count(self, word):
        try:
            with open(self.file, 'r') as my_file:
                f_data = my_file.read()
                counter = 0
                for line in f_data.split(" "):
                    if word in line:
                        counter += 1
                return f"The word {word} appears {counter} times."
        except FileNotFoundError as fne:
            return "File not found: {fne}"
        except Exception as e:
            return f"An error occurred: {e}"

# Create an instance of the WordCounter Class
file = "read_data1.txt"
word_counter = WordCounter(file)


# Call the instance method and print the result
word = input("Enter the word to search: ")
result = word_counter.find_word_count(word)
print(result)
```

The output is:
```
Enter the word to search: amazing
The word amazing appears 1 times.
```

## 18. Perform a read using OOPs class method

```
class WordCounter:
    def __init__(self, file):
        self.file = file

    @classmethod
    def find_word_count(cls, file, word):
        try:
            with open(file, 'r') as my_file:
                f_data = my_file.read()
                counter = 0
                for line in f_data.split(" "):
                    if word in line:
                        counter += 1
                return f"The word {word} appears {counter} times."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return f"An error occurred: {e}"

# Prompt the user for a word to search
word = input("Enter the word to search: ")

# Call the class method and print the result
file = "read_data1.txt"
result = WordCounter.find_word_count(file, word)
print(result)
```

## 19. Perform a read using OOPs static method.

```
class WordCounter:
    @staticmethod
    def find_word_count(file, word):
        try:
            with open(file, 'r') as my_file:
                f_data = my_file.read()
                counter = 0
                for line in f_data.split(" "):
                    if word in line:
                        counter += 1
                return f"The word {word} appears {counter} times."
        except FileNotFoundError:
            return "File not found."
        except Exception as e:
            return f"An error occurred: {e}"

# Prompt the user for a word to search
word = input("Enter the word to search: ")

# Call the static method and print the result
file = "read_data1.txt"
result = WordCounter.find_word_count(file, word)
print(result)
```

## 20. Importance of context manager.Explain in detail

[Context Managers](https://book.pythontips.com/en/latest/context_managers.html)

A context manager in Python is a mechanism that allows you to properly manage resources, such as files or network connections, by allocating and releasing them automatically when they are no longer needed. Context managers are implemented using a protocol that defines two methods: `__enter__()` and `__exit__()`.

The importance of context managers can be better understood through the following points:

1. **Resource Management:** Context managers provide a clean and efficient way to manage resources that need to be acquired and released, such as files, network connections, database connections, etc. They ensure that resources are properly released even if exceptions occur within the context.

2. **Automatic Cleanup:** Context managers ensure that resources are properly closed or released when they are no longer needed. This helps prevent resource leaks and improves memory management.

3. **Readability and Maintenance:** Context managers improve the readability of code by encapsulating resource management logic within a well-defined context. This makes the code more maintainable and less error-prone.

4. **Error Handling:** Context managers are designed to handle exceptions and errors gracefully. They ensure that resources are released regardless of whether an exception occurs within the context.

5. **Avoiding Repetition:** Context managers eliminate the need for repetitive code to open and close resources. This leads to more concise and modular code.

6. **Safe Operations:** When using context managers, you can be confident that resources are being handled safely. For instance, even if an exception occurs during a write operation on a file, the file will still be closed properly.

Here's an example to illustrate the importance of context managers in file handling:

```python
# Without context manager
file = open('example.txt', 'r')
try:
    content = file.read()
    print(content)
finally:
    file.close()

# With context manager
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed when exiting the block
```

In the first example, you need to explicitly close the file, and if an exception occurs before the `file.close()` line, the file might not be closed properly. In the second example, the context manager takes care of opening and closing the file automatically, even if an exception occurs.

**Context manager with exceptional handling**

Example of using a context manager with exceptional handling for file operations:

```python
try:
    with open("example.txt", "r") as file:
        content = file.read()
        # Simulate a potential exception
        result = 10 / 0
        print(content)
except ZeroDivisionError:
    print("Error: Division by zero.")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
```

In this example, we:

1. Use the `with` statement to open the file "example.txt" for reading.
2. Inside the `with` block, read the content of the file and then intentionally create a division by zero exception to simulate an error.
3. Since an exception occurs, the control transfers to the relevant `except` block, in this case, `ZeroDivisionError`, where we print an error message.
4. If no division by zero error occurred, the content of the file would have been printed before encountering the exception.

Using a context manager with exceptional handling ensures that the file is automatically closed, even if an exception occurs within the block. This helps in proper resource management and error handling.

In summary, context managers play a crucial role in ensuring resource management, error handling, and cleaner code in Python. They make programming more efficient, maintainable, and less error-prone, especially when dealing with resources that need proper allocation and release.

## 21. enter vs exit

In Python, `__enter__()` and `__exit__()` are special methods used to define the behavior of context managers. They are part of the context manager protocol and are used to establish and release a context for a block of code.

1. **`__enter__()` Method:**
   - This method is called when entering the context of a `with` statement.
   - It is responsible for setting up the context and acquiring necessary resources.
   - The value returned by `__enter__()` is typically assigned to a variable after the `as` keyword in the `with` statement.
   - If an exception occurs within the `with` block, the `__exit__()` method is called, allowing for proper cleanup.

2. **`__exit__()` Method:**
   - This method is called when exiting the context of a `with` statement, regardless of whether an exception occurred.
   - It is responsible for releasing resources, performing cleanup, and handling exceptions.
   - The method receives information about any exception that occurred (if any), allowing you to handle exceptions or suppress them if needed.
   - If an exception occurs within the `with` block and is not handled within the block itself, it can be handled or propagated further in the `__exit__()` method.

Here's a basic example to illustrate the use of `__enter__()` and `__exit__()`:

```python
class MyContext:
    def __enter__(self):
        print("Entering the context")
        return self  # Value to be assigned after 'as' in the 'with' statement

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exiting the context")
        if exc_type is not None:
            print(f"Exception: {exc_type} - {exc_value}")
        # Return True to suppress the exception, or False to propagate it

# Using the context manager
with MyContext() as context:
    print("Inside the context")
    # Uncomment the line below to test exception handling
    # raise ValueError("An error occurred")

print("Outside the context")
```

In this example, the `MyContext` class defines the `__enter__()` and `__exit__()` methods. When the `with` statement is used to create a context, the `__enter__()` method is called, and its return value is assigned to the variable `context`. Inside the block, the code executes. If an exception is raised within the block, the `__exit__()` method is called, allowing for proper cleanup. The exception information is provided as arguments to the `__exit__()` method.

Using the context manager with `with` statements ensures proper resource management and error handling, making your code more reliable and maintainable.

## 22. How to open text, csv, excel, pdf, image, audio, video, jpeg using `open` and `with` statements

The `open()` function is commonly used to open files in text mode. However, for different file formats like CSV, Excel, PDF, images, audio, and video, you will need to use different libraries specifically designed for those formats. Here's a general overview of how to open and work with these different file types using various libraries in Python:

1. **Text File:**
   You can use the `open()` function to open a text file in text mode.
   
   ```python
   with open('text_file.txt', 'r') as file:
       content = file.read()
       print(content)
   ```

2. **CSV File:**
   Use the `csv` module to read and write CSV files.
   
   ```python
   import csv
   
   with open('data.csv', 'r') as csvfile:
       reader = csv.reader(csvfile)
       for row in reader:
           print(row)
   ```

3. **Excel File:**
   You can use the `openpyxl` or `xlrd` library to read and write Excel files.
   
   ```python
   import openpyxl
   
   with openpyxl.load_workbook('data.xlsx') as workbook:
       sheet = workbook.active
       for row in sheet.iter_rows(values_only=True):
           print(row)
   ```

4. **PDF File:**
   You can use the `PyPDF2` or `pdfplumber` library to extract text and data from PDF files.
   
   ```python
   import PyPDF2
   
   with open('document.pdf', 'rb') as pdf_file:
       pdf_reader = PyPDF2.PdfReader(pdf_file)
       text = pdf_reader.pages[0].extract_text()
       print(text)
   ```

5. **Image File:**
   Use the `PIL` (Pillow) library to open and manipulate image files.
   
   ```python
   from PIL import Image
   
   with Image.open('image.jpg') as img:
       img.show()
   ```

6. **Audio and Video Files:**
   For audio and video files, you can use the `moviepy` library.
   
   ```python
   from moviepy.editor import VideoFileClip, AudioFileClip
   
   video = VideoFileClip('video.mp4')
   video.preview()
   
   audio = AudioFileClip('audio.mp3')
   audio.preview()
   ```

Remember that working with different file formats often requires installing additional libraries beyond the built-in `open()` function. Always make sure to install the required libraries using tools like `pip` before using them in your code.

## 23. Importance of file handling in python

File handling in Python is crucial for several reasons:

1. **Data Persistence:** Files provide a way to store data beyond the lifetime of a program's execution. They allow you to save data to disk and retrieve it later, ensuring data persistence even after the program is closed.

2. **Input and Output:** Files are used for input and output operations. You can read data from files (input) or write data to files (output) as needed. This is essential for tasks such as reading configuration files, storing user data, and more.

3. **Data Storage:** Files are used to store structured and unstructured data in various formats, including text, binary, JSON, XML, CSV, and more. This makes them versatile for handling different types of data.

4. **Log Management:** Files are commonly used for logging information, errors, and debugging details. This helps in tracking the behavior of a program and diagnosing issues.

5. **Database Backup:** Files are used to create backups of databases, ensuring that data is not lost in case of system crashes or failures.

6. **Data Analysis:** In data science and analysis, file handling is crucial for reading and processing large datasets. Files can be used to store data in various formats, which can then be analyzed using libraries like pandas.

7. **Configuration Management:** Configuration files are often used to store settings, preferences, and options for applications. File handling allows you to read and modify these configuration files.

8. **Reporting:** Files are used to generate reports by collecting data and formatting it in a structured manner. These reports can then be shared with others.

9. **Collaboration:** Files provide a way for multiple users or programs to interact and share data. This is especially important in collaborative projects where data needs to be exchanged.

10. **Resource Management:** In some cases, files are used to manage resources such as images, videos, audio, and more.

In Python, the built-in functions and libraries for file handling, such as `open()`, `read()`, `write()`, and context managers (`with` statement), make it easy to work with files. Proper file handling helps in improving the efficiency, reliability, and maintainability of programs that involve data storage, manipulation, and analysis.

## 24. Give a list of file handling operations

File handling operations in Python allow you to interact with files on your system. The common file handling operations include:

1. **Opening a File:**
   To open a file, you use the `open()` function. It takes a filename and a mode as arguments and returns a file object.
   
   ```python
   file = open("example.txt", "r")
   ```

2. **Reading from a File:**
   You can read the contents of a file using methods like `read()`, `readline()`, or `readlines()`.
   
   ```python
   content = file.read()         # Read the entire content
   line = file.readline()       # Read a single line
   lines = file.readlines()     # Read all lines into a list
   ```

3. **Writing to a File:**
   To write to a file, open it in write mode ("w" or "a" for append) and use the `write()` method.
   
   ```python
   with open("output.txt", "w") as output_file:
       output_file.write("Hello, world!")
   ```

4. **Appending to a File:**
   You can append content to an existing file using append mode ("a").
   
   ```python
   with open("output.txt", "a") as output_file:
       output_file.write("\nAppending new content.")
   ```

5. **Closing a File:**
   Always close the file using the `close()` method to free up resources.
   
   ```python
   file.close()
   ```

6. **Context Managers (`with` Statement):**
   Using the `with` statement ensures that the file is properly closed after use, even if an exception occurs.
   
   ```python
   with open("example.txt", "r") as file:
       content = file.read()
   ```

7. **Seek and Tell:**
   You can move the cursor within the file using `seek()` and get the cursor position using `tell()`.
   
   ```python
   file.seek(10)   # Move cursor to position 10
   position = file.tell()   # Get current cursor position
   ```

8. **Working with Binary Files:**
   For binary files, you can open files in binary mode ("rb" for read and "wb" for write).
   
   ```python
   with open("binary_file.bin", "rb") as binary_file:
       data = binary_file.read()
   ```

9. **Working with CSV Files:**
   Use the `csv` module for reading and writing CSV files.
   
   ```python
   import csv
   
   with open("data.csv", "r") as csvfile:
       reader = csv.reader(csvfile)
       for row in reader:
           print(row)
   ```

10. **File Iteration:**
    Files can be iterated line by line without reading the entire content into memory.
   
    ```python
    with open("example.txt", "r") as file:
        for line in file:
            print(line)
    ```

Remember to handle exceptions when working with files to ensure your program doesn't crash due to file-related issues.

## 25. Converting CSV file to JSON using Pandas

Also involves converting pandas dataframe to JSON with compression (`gzip`) and read back the compressed, uncompressed file using python.

We have a `water-physical-stock-account.csv` that is delineated with comma. Delimiters affect the way data is read in the pandas dataframe.

```
region,variable,RID,yq,value,year,Series,Unit,Source,Quarter
NORTHLAND,Discharge by Hydrogeneration,1,1995.1,0,1995,Quarterly,Mm3,NIW,1
NORTHLAND,Discharge by Hydrogeneration,1,1995.2,0,1995,Quarterly,Mm3,NIW,2
NORTHLAND,Discharge by Hydrogeneration,1,1995.3,0,1995,Quarterly,Mm3,NIW,3
NORTHLAND,Discharge by Hydrogeneration,1,1995.4,0,1995,Quarterly,Mm3,NIW,4
.......
```

Pass in the raw location of the csv file and read the csv using the `read_csv` method provided by python:

```
csv_file = r"/content/water-physical-stock-account-quarterly-1995-2020-CSV.csv"
water_df = pd.read_csv(csv_file, sep=',')
print(water_df)
```

**Output**
```
region                        variable  RID      yq  value  year  \
0         NORTHLAND    Discharge by Hydrogeneration    1  1995.1      0  1995   
1         NORTHLAND    Discharge by Hydrogeneration    1  1995.2      0  1995   
2         NORTHLAND    Discharge by Hydrogeneration    1  1995.3      0  1995   
3         NORTHLAND    Discharge by Hydrogeneration    1  1995.4      0  1995   
4          AUCKLAND    Discharge by Hydrogeneration    2  1995.1      0  1995   
...             ...                             ...  ...     ...    ...   ...   
17003  SOUTH_ISLAND  Abstraction by Hydrogeneration   19  2018.4 -27594  2018   
17004  SOUTH_ISLAND  Abstraction by Hydrogeneration   19  2019.1 -27052  2019   
17005  SOUTH_ISLAND  Abstraction by Hydrogeneration   19  2019.2 -26601  2019   
17006  SOUTH_ISLAND  Abstraction by Hydrogeneration   19  2019.3 -28203  2019   
17007  SOUTH_ISLAND  Abstraction by Hydrogeneration   19  2019.4 -30802  2019   

          Series Unit Source  Quarter  
0      Quarterly  Mm3    NIW        1  
1      Quarterly  Mm3    NIW        2  
2      Quarterly  Mm3    NIW        3  
3      Quarterly  Mm3    NIW        4  
4      Quarterly  Mm3    NIW        1  
...          ...  ...    ...      ...  
17003  Quarterly  Mm3    NIW        4  
17004  Quarterly  Mm3    NIW        1  
17005  Quarterly  Mm3    NIW        2  
17006  Quarterly  Mm3    NIW        3  
17007  Quarterly  Mm3    NIW        4  

[17008 rows x 10 columns]
```

**Converting Pandas Dataframe to JSON**

First create a file that ends with a `.json` specification, `water-stock-account.json`. The `to_json` method can be used to convert the pandas dataframe to `JSON`.
Without specifying the `indent` and `orient` arguments, the records are written to the json file in the first row where the column format is the default format. 
Orient based on the records.

```
json_output = r"/content/sample_data/water-stock-account.json"
output = water_df.to_json(json_output, indent=1, orient='records')
```

The output is:
```
[
 {
  "region":"NORTHLAND",
  "variable":"Discharge by Hydrogeneration",
  "RID":1,
  "yq":1995.1,
  "value":0,
  "year":1995,
  "Series":"Quarterly",
  "Unit":"Mm3",
  "Source":"NIW",
  "Quarter":1
 },
 ....
....
```

**Writing the Pandas Dataframe as a compressed JSON file (gzip)**

Create a compressed file with the `.gz` specification, `water-stock-account.json.gz`:

```
json_output_compressed = r"/content/sample_data/water-stock-account.json.gz"
output_compressed = water_df.to_json(json_output_compressed, orient='records', indent=1, compression='gzip')
```

Read the compressed JSON file
```
pd.read_json(json_output_compressed)
```

The output is:
```
	region	variable	RID	yq	value	year	Series	Unit	Source	Quarter
0	NORTHLAND	Discharge by Hydrogeneration	1	1995.1	0	1995	Quarterly	Mm3	NIW	1
1	NORTHLAND	Discharge by Hydrogeneration	1	1995.2	0	1995	Quarterly	Mm3	NIW	2
2	NORTHLAND	Discharge by Hydrogeneration	1	1995.3	0	1995	Quarterly	Mm3	NIW	3
3	NORTHLAND	Discharge by Hydrogeneration	1	1995.4	0	1995	Quarterly	Mm3	NIW	4
4	AUCKLAND	Discharge by Hydrogeneration	2	1995.1	0	1995	Quarterly	Mm3	NIW	1
...	...	...	...	...	...	...	...	...	...	...
17003	SOUTH_ISLAND	Abstraction by Hydrogeneration	19	2018.4	-27594	2018	Quarterly	Mm3	NIW	4
17004	SOUTH_ISLAND	Abstraction by Hydrogeneration	19	2019.1	-27052	2019	Quarterly	Mm3	NIW	1
17005	SOUTH_ISLAND	Abstraction by Hydrogeneration	19	2019.2	-26601	2019	Quarterly	Mm3	NIW	2
17006	SOUTH_ISLAND	Abstraction by Hydrogeneration	19	2019.3	-28203	2019	Quarterly	Mm3	NIW	3
17007	SOUTH_ISLAND	Abstraction by Hydrogeneration	19	2019.4	-30802	2019	Quarterly	Mm3	NIW	4
17008 rows × 10 columns
```

**Reading the compressed JSON file without pandas**

Without pandas, reading the compressed file involves a couple more steps:

```
with gzip.open(json_output_compressed, 'r') as jsonfile:
  data = json.loads(jsonfile.read().decode('utf-8'))
  
```



## 25. Reading and writing JSON file using Pandas

