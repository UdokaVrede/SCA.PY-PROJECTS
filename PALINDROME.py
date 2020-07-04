def palindrome():    #function initiliazation 

    while True:     #condition check 
    
        num=input('Enter a number:')  #accept user input
        reverseNum=num[::-1]          #reverse of string
        
        if reverseNum == num:         #condition check 
            print(num,'is a palindrome')
            
        elif reverseNum != num:
            print(num, 'is not a palindrome')
            
        else:
            print('You have entered a wrong input, check that the value you entered is an unsigned number')
        
        
        
palindrome()    #calling the function
