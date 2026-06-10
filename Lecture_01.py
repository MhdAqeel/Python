python -m venv my_env                  //create new enviroment

C:\Users\DCSuser\csc209s3>my_env\Scripts\activate
                                      //to activate the enviroment
(my_env) C:\Users\DCSuser\csc209s3>

(my_env) C:\Users\DCSuser\csc209s3>python
Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> 5+8
13
>>> 10-4.5
5.5
>>> 10*2
20
>>> 10/3                    //true divition
3.3333333333333335
>>> 10//3                   //claw divition 
3
>>> 10%3                    //reminder
1
>>> 2**4                    //two to the power four
16
>>> 9**0.5                  //square root
3.0
>>> 2+3*4                   //python follows BODMAS rules
14

>>> import math              //import pakage
>>> math.sqrt(16)
4.0
>>> math.sin(30)
-0.9880316240928618
>>> math.sin(math.pi/2)
1.0
>>> math.pi
3.141592653589793
>>> math.inf
inf
>>> math.inf/2
inf

print("1.check if 28 is divisible by 4?")
if(28%4 == 0):
    print("yes")
else:
    print("no")

print("2.check if 37 is even or odd?")
if(37%2==0):
    print("even")
else:
    print("odd")

print("3.find the reminder of 999 divided by 10")
print(999%10)

print("4.in a square one side = 6, find the area")
side=6
print(side*side)

print("5.in a square one side = 11, find the perimeter")
side=11
print(side*4)

print("6.in a square one side = 8, find the area and perimeter")
side=8
print("perimeter = " , side*4)
print("Area = " , side * side)

print("7.in a tri angele sides are 3,4,5 find area")

print("8.in a tri angele base is 12 and height is 9,find area")
base = 12
height=9
print(0.5 * base * height)

print("9.in a circle radius is 7, find the area")
radius=7
import math
print(math.pi*radius*radius)

>>> from decimal import Decimal
>>> Decimal(0.1)+Decimal(0.3)
Decimal('0.3999999999999999944488848769')
>>> Decimal('0.1')+Decimal('0.3')
Decimal('0.4')


