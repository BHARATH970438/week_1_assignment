'''Q1. Create one variable containing following type of data:
(i) string
(ii) list
(iii) float
(iv) tuple'''
#(i)
str1='python'
#(ii)
list1=[1,2,3,4,5,6]
#(iii)
float1=1.23
#(iv)
tuple1=(1,2,3,4)

'''Q2. Given are some following variables containing data:
(i) var1 = ‘ ‘
(ii) var2 = ‘[ DS , ML , Python]’
(iii) var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
(iv) var4 = 1.
What will be the data type of the above given variable.'''
#(i) string
#(ii) string
#(iii) list
#(iv)  float

'''Q3. Explain the use of the following operators using an example:
(i) /
(ii) %
(iii) //
(iv) **'''
#(i) Float Division ,it return type is float, it results quotient from division of two numbers
print(1.2/2)

#(ii) Modules , it return type is integer, it results reminder from division of two numbers
print(2.3%2)

#(iii) Floor Division , it return type is integer, it results the no. of times denominater divies the numerator
print(4//2)

#(iv)  Exponent, its return type is integer, it used to perform power operation, there is inbuilt function py. pow()
print(2**3)

'''Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the
element and its data type.'''

list1=[1,2,3,4,'pw','cw',12.3,1234.5,'sss','sss']
for  i in list1:
    print(type(i))

'''Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
times it can be divisible.'''

a=int(input('a: '))
b=int(input('b: '))
count=0
if a>=b and a%b==0:
    while a >= b:
        count+=1
        a= a-b
    print('No of times it can be divisible: ',count)

'''Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
divisible by 3 or not.'''

list1=[1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,66,77,88,99,111,222,333,444,555,666]
for i in list1:
    if i%3==0:
        print('It is divisible by 3')
    else:
        print('It is not divisible by 3')

'''Q7. What do you understand about mutable and immutable data types? Give examples for both showing
this property.'''
#ans
'''
mutable Datatypes: Which we can able to change or modify data once it has been created. 
Ex: list, Dictionary

Immutable data types : Datatypes are those whose values cannot be modified after they are created, while mutable data types allow for modifications
Ex: strings, tuples'''
# Immutable Example

#(i) string
message = "Hello"
new_message = message + " World!"  # Concatenating two strings
print(new_message) 

#(ii) tuple
point = (3, 4)
point[0] = 1  # This will result in an error since tuples are immutable


# Mutable

#(i) list
numbers = [1, 2, 3, 4]
numbers[2] = 10  # Modifying the third element of the list
print(numbers)  # Output: [1, 2, 10, 4]

#(ii) Dict
person = {"name": "John", "age": 25}
person["age"] = 26  # Modifying the value associated with the "age" key
print(person)  # Output: {"name": "John", "age": 26}
