list = []

for i in range(1,1500):
    if (i%5==0 and i%7==0):
        list.append(i)
    if(len(list)>6):
        break

print(list)