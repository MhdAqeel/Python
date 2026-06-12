C:\Users\dcsuser>mkdir csc209s3
C:\Users\dcsuser>cd csc209s3

C:\Users\dcsuser\csc209s3>python -m venv my_env

C:\Users\dcsuser\csc209s3>my_env\Scripts\activate

(my_env) C:\Users\dcsuser\csc209s3>pip install numpy
Collecting numpy
  Downloading numpy-2.4.6-cp313-cp313-win_amd64.whl.metadata (6.6 kB)
Downloading numpy-2.4.6-cp313-cp313-win_amd64.whl (12.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.3/12.3 MB 6.2 MB/s eta 0:00:00
Installing collected packages: numpy
Successfully installed numpy-2.4.6

[notice] A new release of pip is available: 24.3.1 -> 26.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip

(my_env) C:\Users\dcsuser\csc209s3>python
Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> arr = [1,2,3,4]
>>> import numpy as np
>>> arr1 = np.array([1,2,3])
>>> type(arr1)
<class 'numpy.ndarray'>
>>> type([1,2,3])
<class 'list'>
>>> arr1.mean()
np.float64(2.0)
>>> arr1 = np.array([1,2,3])
>>> arr2 = np.array([4,5,6])
>>> arr1 + arr2
array([5, 7, 9])
>>> arr1*arr2
array([ 4, 10, 18])
>>> arr1/arr2
array([0.25, 0.4 , 0.5 ])

>>> arr = np.array([4,9,16,25])
>>> np.sqrt(arr)
array([2., 3., 4., 5.])                       #find the square root of a array

>>> np.pi
3.141592653589793
>>> angles = np.array([0,np.pi/2,np.pi])
>>> angles
array([0.        , 1.57079633, 3.14159265])
>>> angles.dtype
dtype('float64')
>>> np.sin(angles)
array([0.0000000e+00, 1.0000000e+00, 1.2246468e-16])

# we stated data types
>>> name = "john"
>>> print(name)
john
>>> name = "peter"
>>> print(name)
peter

>>> s = "Python"
>>> s[0]
'P'
>>> s[-1]
'n'
>>> s[1:4]
'yth'

>>> l1 = list(range(0,1001))
>>> l1[1000]
1000
>>> l1[-1]
1000
>>> len(l1)                  #length of a list
1001

>>> list (range(3,15,2))
[3, 5, 7, 9, 11, 13]

>>> list (range(3,16,2))          #range
[3, 5, 7, 9, 11, 13, 15]

