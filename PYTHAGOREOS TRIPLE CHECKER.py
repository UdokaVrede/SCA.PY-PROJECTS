#PROGRAM TO SHOW IF A TRIANGLE IS A RIGHT_ANGLED OR NOT A RIGHT_ANGLED TRIANGLE

#Importing the math module
import math

#check on all code blocks in scope of 'while loop'
while True:
    
    #display for user input
    print('Enter the value of the first side of your triangle:')
    
    #accepting user input
    num1=input()
    
    print("Enter the value of the second side of your triangle:")
    
    num2=input()
    
    #converting input to integer
    a=int(num1)
    b=int(num2)

    #condition check on accepted input
    if  a > 0 and b > 0:
    
        #mathematical operation to calculate the result 
        c=(a**2)+(b**2)
        
        #getting the squareroot of 'c'
        result=math.sqrt(c)
        
        #getting the decimal part of the result
        val=result-math.floor(result)
    
    #condition check on the value of 'val'
    if val == 0.00:
        
        #output if condition is true
        print ("The triangle is a right-angle triangle",'\n')
        
        #output if condition is false
    else:
        print("This is not a right angle triangle",'\n')
  
