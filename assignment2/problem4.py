reversestring =''

str = input('Enter the string to reverse\n')

for i in range(len(str)-1,-1,-1):
    reversestring = reversestring + str[i]
print(reversestring)