birthdays={'Mum': 'Aug 15th',
           'Butter boy' : 'July 10th',
           'Bambi' : 'Apr 11th'}
           
while True:
    
    name=input('Enter a name or leave blank to quit: ')
    
    if name == '':
        print('The birthdays in the record are:')
        print(birthdays)
        break
    
    if name in birthdays:
        print(name,'is born on ' + birthdays[name])
        
    else:
        print('Sorry the name '+ name +' is not valid','\n')
        
        print('Do you wish to update the record?')
        user=input('Enter yes or no to quit: ')
        
        if user == 'yes':
            birthdate=input('Enter the birthdate: ')
            birthdays[name]=birthdate
            print('The record has been updated','\n')
            print('Thank you for using this, you may continue or blank to quit')
            
        else:
            print('Thank you for using this, You may wish to continue or quit')
        
        
