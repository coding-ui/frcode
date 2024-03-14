randomsd->function(length,start,end){
rnorm(length,start,end)
}
length=as.integer(readline(prompt="Enter the length :- 
"))
start=as.integer(readline(prompt="Enter the starting 
point :- "))
end=as.integer(readline(prompt="Enter the ending point
:- "))
randomsd(length,start,end)



PROGRAM:
samplepop <- function(data,size){
print(sample(data,size))
}
data=c(23,45,21,34,5,6,7,8,86,45,3)
size=as.integer(readline(prompt="Enter the size :- "))
samplepop(data,size)

# Creating a vector

x <- c(7, 4, 3, 9, 1.2, -4, -5, -8, 6)

print(x)

print(“Minimum is”)

print(min(x))

print(“Maximum is”)

print(max(x))

print(“Sorted”)

sort(x)

facto <- function(){

n=as.integer(readline(prompt = ‘Input a num to factorial :’))

fact=1

if (n<0){

cat(“Cannot give factorial”)

} else if(n=0){

cat(“Factorial is 1”)

} else {

for(i in 1:n){

fact=fact*i}

cat(“Factorial of”,n,”is”,fact)

}

}

facto()


mult.tab <- function(x,y){

for( t in 1:y)

{

 cat( x, '*', t, '=', x* t,”\n”))

}

}
multiplication table
num= as.integer(readline(prompt=”Enter No for 

Multiplication table:”)

tab= as.integer(readline(prompt=”Enter No of times to be 

multiplied:”)

mult.tab(num,tab)

prime
PROGRAM:

num = as.integer(readline(prompt="Enter a number: "))

flag = 0

if(num > 1) {

flag = 1

for(i in 2:(num-1)) {

if ((num %% i) == 0) {

flag = 0

break }

}

} 

if(num == 2) flag = 1

if(flag == 1) {

print(paste(num,"is a prime number"))

} else {

print(paste(num,"is not a prime number"))

}

PROGRAM:

num = as.integer(readline(prompt="Enter a number: "))

sum = 0

temp = num

while(temp > 0) {

digit = temp %% 10

sum = sum + (digit ^ 3)

temp = floor(temp / 10)

}

if(num == sum) {

print(paste(num, "is an Armstrong number"))

} else {

print(paste(num, "is not an Armstrong number"))

}


nterms = as.integer(readline(prompt="How many terms? "))

n1 = 0

n2 = 1

count = 2

if(nterms <= 0) {

print("Plese enter a positive integer")

} else {

if(nterms == 1) {

print("Fibonacci sequence:")

print(n1)

} else {

print("Fibonacci sequence:")

print(n1)

print(n2)

while(count < nterms) {

nth = n1 + n2

print(nth)

n1 = n2

n2 = nth

count = count + 1

}}}


PROGRAM:

year = as.integer(readline(prompt="Enter a year: "))

if((year %% 4) == 0) {

if((year %% 100) == 0) {

if((year %% 400) == 0) {

print(paste(year,"is a leap year"))

} else {

print(paste(year,"is not a leap year"))

}

} else {

print(paste(year,"is a leap year"))

}

} else {

print(paste(year,"is not a leap year"))

}


		DATAFRAME

AIM:

To write an R program to create and print dataframe.

PROGRAM:

x <- data.frame("SN" = 1:2, "Age" = c(21,15), "Name" = 

c("John","Dora"),stringsAsFactors=FALSE)

str(x)

x["Name"]

print(“Adding a row of data”)

rbind(x,list(1,16,"Paul"))


 # Create a data frame
x <- data.frame("SN" = 1:3, "Age" = c(21, 15,22), "Name" = c("John", "Dora","Sanjai"))

# Check the structure of the data frame
str(x)

# Access the 'Name' column
x["Name"]

# Print a message indicating the addition of a row of data
print("Adding a row of data")

# Add a row to the data frame
x <- rbind(x, list(4, 16, "Paul"))
print(x)

[14/03, 8:27 am] Sanjai Clg: # Create a data frame
x <- data.frame("SN" = 1:3, "Age" = c(21, 15,22), "Name" = c("John", "Dora","Sanjai"))

# Check the structure of the data frame
str(x)

# Access the 'Name' column
x["Name"]

# Print a message indicating the addition of a row of data
print("Adding a row of data")

# Add a row to the data frame
x <- rbind(x, list(4, 16, "Paul"))
print(x)
[14/03, 8:27 am] Sanjai Clg: # Create two 3x3 matrices
matrix1 <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3, byrow = TRUE)
matrix2 <- matrix(c(9, 8, 7, 6, 5, 4, 3, 2, 1), nrow = 3, byrow = TRUE)

# Display the matrices
cat("Matrix 1:\n")
print(matrix1)
cat("\nMatrix 2:\n")
print(matrix2)

# Addition
addition_result <- matrix1 + matrix2
cat("\nAddition Result:\n")
print(addition_result)

# Subtraction
subtraction_result <- matrix1 - matrix2
cat("\nSubtraction Result:\n")
print(subtraction_result)

# Multiplication
multiplication_result <- matrix1 * matrix2
cat("\nMultiplication Result:\n")
print(multiplication_result)

# Division
# Note: Division of matrices is not defined in R. You can perform element-wise division instead.
division_result <- matrix1 / matrix2
cat("\nElement-wise Division Result:\n")
print(division_result)


# bar plot Student names
students <- c("Student 1", "Student 2", "Student 3", "Student 4", "Student 5")

# Marks of the students
marks <- c(80, 65, 75, 90, 85)

# Create a bar plot
barplot(marks, names.arg = students, col = "skyblue", main = "Marks of Five Students", xlab = "Students", ylab = "Marks")
