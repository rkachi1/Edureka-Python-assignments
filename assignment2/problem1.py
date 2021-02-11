specialCharacters = [ '@', '&']
while True:
    password= input("Enter a password to be valid for currency withdrawing\n")
    if(len(password)>10):
        print('The maximum length of the password should be 10')
    elif(len(password)<5):
        print('The minimum length of the password should be 5')
    elif(not(password.isalpha()) or (not(password in specialCharacters))):
        print('you have to enter atleast one character and must contain a special character like @ and &')
    elif(not(password.isdigit()) and(password in range(0,9))):
        print('your password has to contain atleast 1 numeral and must be in the range from 0 to 9')
    else:
        print('your password is valid')
        break
