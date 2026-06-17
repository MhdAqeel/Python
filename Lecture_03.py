C:\Users\dcsuser>mkdir CSC209S3

C:\Users\dcsuser>python -m venv my_env

C:\Users\dcsuser>my_env\Scripts\activate

(my_env) C:\Users\dcsuser>python

>>> print(range(0,21,2))                  #prit the even numbers from 0 to 20
range(0, 21, 2)

#first five chareecters of 'PROGRAMMIG'
>>> s="programming"
>>> s[0:5]
'progr'

#laST5 CHArecters of programming
>>> s[-1:-6:-1]
'gnimm'
#Python - Modify Strings
>>> name  = "john"
>>> name.upper()
'JOHN'
>>> name.lower()
'john'

>>> name = " name "
>>> name.strip()                        #STRIP key word(remove key word)
'name'

>>> name = "John"
>>> id(name)                    #id can show the memory address where it saved
2325526090720

>>> name = "John"                      #immutable behaviour of String
>>> id(name)
2325526090720
>>> name = name + " mary"
>>> print(name)
John mary
>>> id(name)
2325524661488

>>> arr = [1,2,3]                    #mutable behavior of lists
>>> id(arr)
2325709038592
>>> arr.append(4)
>>> id(arr)
2325709038592
>>> print(arr)
[1, 2, 3, 4]

>>> arr = [1,2,3]
>>> id(arr)
2325709038592
>>> arr.append(4)
>>> id(arr)
2325709038592
>>> print(arr)
[1, 2, 3, 4]
>>> arr.insert(3,5)
>>> arr
[1, 2, 3, 5, 4]
>>> arr[3]=10
>>> arr
[1, 2, 3, 10, 4]
>>> id(arr)
2325709038592

>>> a = [1,2,3]
>>> b=a        # pass reference
>>> id(a)
2325521633664
>>> id(b)
2325521633664
>>> b.append(4)              #both share same mamory location
>>> a
[1, 2, 3, 4]
>>> b
[1, 2, 3, 4]
>>> id(b)
2325521633664

>>> a=[1,2,3]
>>> id(a)
2325526071808
>>> b=a.copy()        #only pass the data not the momory address
>>> id(b)
2325709039104
>>> b
[1, 2, 3]

>>> arr = [1,2,3]
>>> arr.append(4)
>>> arr
[1, 2, 3, 4]
>>> arr.insert(2,5)
>>> arr
[1, 2, 5, 3, 4]
>>> arr.pop()
4
>>> arr
[1, 2, 5, 3]

>>> arr = [1,2,3,2,6]
>>> arr.remove(2)
>>> arr
[1, 3, 2, 6]
>>> arr.remove(2)
>>> arr
[1, 3, 6]

>>> a = {1 , 2 ,4}
>>> b = {2 , 3 , 4}            # SET data structure
>>> a & b                  # inter section
{2, 4}
>>> a | b                  # union
{1, 2, 3, 4}
>>> a -b
{1}
>>> b - a
{3}

>>> cars = {"Audi","BMW","Honda"}
>>> bike = {"BMW" ,"Honda" , "Hero Honda" }
>>> cars & bike
{'Honda', 'BMW'}
>>> cars | bike
{'Honda', 'BMW', 'Hero Honda', 'Audi'}
>>> cars - bike
{'Audi'}
>>> bike - cars
{'Hero Honda'}

>>> cars.add(1)
>>> cars
{1, 'Honda', 'BMW', 'Lambo', 'Audi'}
>>> cars.remove(1)
>>> cars
{'Honda', 'BMW', 'Lambo', 'Audi'}
>>> cars.remove(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 1
>>> cars.discard(1)
>>> cars
{'Honda', 'BMW', 'Lambo', 'Audi'}


#########    tuples
>>> s1 = (1 ,2, 3,4,5,6)
>>> s1                            ##tuples are immutable
(1, 2, 3, 4, 5, 6)
>>> s1 + (7,)
(1, 2, 3, 4, 5, 6, 7)

#####  homogeneous vs heterogeneous data types
