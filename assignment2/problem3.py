userInput = input('Enter string to print')
print("The characters with even indexes are")
for i in range(len(userInput)):
    if(i%2==0 and userInput[i].isalpha()):
        print(userInput[i])
