inputstring = input("Enter the string to count characters\n")

frequencyOfCharacters ={}

for i in inputstring:
    if i in frequencyOfCharacters:
        frequencyOfCharacters[i]+=1
    else:
        frequencyOfCharacters[i]=1

print(frequencyOfCharacters)
