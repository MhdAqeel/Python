C:\Users\dcsuser>cd csc209s3

C:\Users\dcsuser\csc209s3>python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 3+3
6
>>> nums = [10,20,30]
>>> nums.append(40)
>>> nums
[10, 20, 30, 40]
>>> fruits=["apple","banana","orange"]
>>> fruits.remove("banana")
>>> fruits
['apple', 'orange']
>>> colors=["red","green","blue"]
>>> colors.insert(1,"yellow")
>>> colors
['red', 'yellow', 'green', 'blue']
>>> marks=[50,60,70,80]
>>> last=marks.pop()
>>> last
80
>>> marks
[50, 60, 70]

>>> student={"name":"Alice","age":"20"}
>>> student["city"]="kandy"
>>> student
{'name': 'Alice', 'age': '20', 'city': 'kandy'}
>>> employee={"id":101,"name":"john","salary":50000}
>>> employee["salary"]
50000
>>> t=(10,20,30,40)
>>> t.count(20)
1
>>> t.index(20)
1
###########   INPUT ################
>>> name = input("enter your name : ")
enter your name : aqeel
>>> name
'aqeel'
>>> age = input("Enter your name : ")
Enter your name : 23
>>> age = input("Enter your age : ")
Enter your age : 23
>>> name
'aqeel'
>>> age
'23'
>>> type(age)
<class 'str'>
>>> age = int(age)      #type casting
>>> type(age)
<class 'int'>
>>> age
23

>>> tall = int(input("enter tall : "))
enter tall : 100
>>> type(tall)
<class 'int'>

>>> ls = "10,20,30,40"
>>> ls[0]
'1'
>>> ls[2]
','
>>> ls.split(",")
['10', '20', '30', '40']

>>> txt = input("List of nums : ")
List of nums : 10,20,30,40
>>> txt
'10,20,30,40'
>>> txt.split(",")
['10', '20', '30', '40']
>>> txt[0]
'1'
>>> txt = txt.split(",")
>>> txt[0]
'10'
>>> txt[0]=int(txt[0])
>>> txt
[10, '20', '30', '40']
>>> txt = int(txt)
Traceback (most recent call last):
  File "<python-input-61>", line 1, in <module>
    txt = int(txt)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
>>> txt  =  map(int , txt)
>>> txt
<map object at 0x0000024EF0E946D0>
>>> list(txt)
[10, 20, 30, 40]


>>> list(map(int,input().split(",")))
10,20,30,40
[10, 20, 30, 40]


>>> arr = ["10","20","30","40"]
>>> mp = map(int,arr)
>>> list(mp)
[10, 20, 30, 40]

