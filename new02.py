#armstrong number.
num = int(input("Enter a number: "))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

#fibonacci series
n=int(input("enter the number"))
a = 0 
b = 1 
print(a,end=" ")
for i in range(0,n):
        c = a + b             
        a = b              
        b = c  
        print(c,end=" ")        

#factorial
def factorial(n):
    if n==0:
       return 1
    else:
       return n*factorial(n-1)

num=int(input("Enter a num"))
print("Factorial of",num,"is",factorial(num))

#positive range1
minimum=int(input("Enter the Minimum Number"))
maximum=int(input("Enter the Maximum Number"))

print("\nAll Positive Numbers from",minimum,"and",maximum) 
for num in range(minimum,maximum+1):
    if num>0:
        print(num,end=" ")
#positive range2
a=int(input("Enter the number:")) 
if  a > 0: 
    print("It is a positive number") 
elif a==0:      
    print("It is a zero") 
else:     
    print("It is a negative number") 

        
#prime number
num=int(input("Enter the Number:"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
          print(num,"is not a prime number")
          break
    else:
          print(num,"is a prime number")

#palindrome
s=input("Enter a string")

if s==s[::-1]:
    print("String is a palindrome")
else:
    print("String is not a palindrome")

#vowels
string ="Guru Nanak College"
vowels ="AeEeIiOoUu"

def checkVow(string,vowels):
        final = [each for each in string if each in vowels]
        print(len(final))
        print(final)  

checkVow(string,vowels)

#creatingdict
x={}
n=int(input("How many element"))

for i in range(n):
    k=input("Enter the key")
    v=int(input("value"))
    x.update({k:v})
print("The dictionary is=",x)
    
#tuple
tup1 = ('physics', 'chemistry', 1997,  2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = ( "a", "b", "c", "d" ) 
print (tup1) 
print (tup2) 
print (tup3)
 # Positive Indexing
print ("tup1[0]: ", tup1[0]) 
 # Slicing
print ("tup2[1:5]: ", tup2[1:5]) 
 # Concatenating tuples
tup3 = tup1 + tup2
print (tup3)
print ("After deleting tup1: ",tup1) 
 # Existence of an element
print(1 in tup2)
print(1997 not in tup2) 
 # Length of a tupleprint(len(tup1))
print(len(tup1))
  # Deleting a tuple 
del tup1 

#towerofhanoi
def tower_of_hanoi(n, source, destination, helper):
	if n==1:
		print ("Move disk 1 from peg", source," to peg", destination)
		return
	tower_of_hanoi(n-1, source, helper, destination)
	print ("Move disk",n," from peg", source," to peg", destination)
	tower_of_hanoi(n-1, helper, destination, source)		
# n = number of disks
n = 3
tower_of_hanoi(n,' A','B','C')

#listtodictionary
countries=["USA","INDIA","GERMANY","FRANCE"]
cities=["WASINGTON","NEWDELHI","BERLIN","PARIS"]
z=zip(countries,cities)

d=dict(z)
print('{}--{}'.format('COUNTRY','CAPITAL'))
for k in d:
    print('{}--{}'.format(k,d[k]))

#bubblesort
arr=[64,34,25,72,22,11,90]
n = len(arr)
def bubblesort(arr):    
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j] 
 
bubblesort(arr) 
print("sorted array is :") 
for i in range(len(arr)):
    print(arr[i],end=" ")

#linear search
arr= [1, 2, 3, 4,5, 6]
n=len(arr)

def search(arr,x):
    for i in range(n):
        if arr[i] == x:
            return i 
    return False
   
x = 10 
result=search(arr, x)
if result:
    print("Found at index",result)  
else:
    print("Not Found")         

#constructor
class employee:
    def __init__(self,name,ids):
        self.ids = ids
        self.name = name
    def display (self):
        print('ID:{ids}\nName:{name}'.format(ids=self.ids,name = self.name))
emp1 = employee("John",101)       
emp2 = employee("David",102)         
emp1.display()       
emp2.display() 

#from abc import ABC 
class Car(ABC):   
    def mileage(self):   
        pass  
  
class Tesla(Car):   
    def mileage(self):   
        print("The mileage is 30kmph")

class Suzuki(Car):   
    def mileage(self):   
        print("The mileage is 25kmph ")
        
class Duster(Car):   
     def mileage(self):   
          print("The mileage is 24kmph ")   
  
class Renault(Car):   
    def mileage(self):   
            print("The mileage is 27kmph ")  
   
t=Tesla ()   
t.mileage()   
  
r = Renault()   
r.mileage()   
  
s = Suzuki()   
s.mileage()   
d = Duster()   
d.mileage()  

#exception handling
import sys
a=10
b=int(input("enter num to divide"))

try:
    print(a/b)               
except:
    print("Oops!",sys.exc_info()[0],"occured.")

#inheritance
class human:
    def speak(self):   
        print("Human Speaking")   

class Dog(human):       
  def bark(self):          
      print("Dog barking")
      
d=Dog()   
d.bark()
d.speak()

#lamda usind dictionary
colors = {"red":10,"green":35,"blue":15,"white":25} 
c1 = sorted(colors.items(),key = lambda t:t[0]) 
print(c1) 
c2 = sorted(colors.items(),key = lambda t:t[1]) 
print(c2)

#length of string
str1 =input("Enter a sting")

length=len(str1)
print("The Length is :",length)

#A DICTIONARY WITH PLAYERS NAME AND SCORES
x={}

n = int(input("how many players ? ")) 
for i in range(n):
    k = input("enter player name:")
    v = int(input("enter runs:")) 
    x.update({k:v})
    
print("\nplayers in this match:") 
for name in x.keys(): 
    print(name,end=" ") 
name = input("\nenter the players name:") 
runs= x.get(name, -1) 
if(runs == -1): 
    print("players not found") 
else:     
    print("{} made runs {}.".format(name,runs)) 

#tuple in loop
tup1=("one","two","three")
for i in tup1:
    print(i)

tup2=("tup")

for x in range(5):
    tup2=tup2,
    print(tup2)

tup3=("python,")*3
print(tup3)

#tuple functions
x = (10, 20, 30, 40, 50, 60, 70, 80, 90) 
print("Tuple : ", x) 
 
total = sum(x) 
print("The Sum of Integer Tuple is : ", total)  
 
fruits = ('Banana', 'Orange', 'Blackberry', 'Apple', 'Kiwi', 
'Grape') 
print("Tuple : ", fruits) 
 
minimum = min(fruits) 
print("The Minimum Value in Fruits Tuple is : ", minimum)
maximum = max(fruits) 
print("The Maximum Value in Fruits Tuple is : ", maximum) 
list1 = (0, 1, 2) 
print(list(list1))  
print(tuple('python')) 












    






    





  



        
        
    




        
        
        
        
    


