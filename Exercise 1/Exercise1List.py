compare = 0
max = 0
max2 = 0
max3 = 0
list = []
#Add up each entry
# If entry is more than previous highest entry overwrite the variable
#return variable with highest value
calorie = open('Data1.txt','r')
data = calorie.readlines()
for line in data:
    variable = line
    #print(variable)
    try:
        int(variable)
        status = True
    except ValueError:
        status = False
    if status == True:
        compare += int(variable)
    else:  
        list.append(compare)
        compare = 0
list.sort()
print(list)
max = list[-1]+list[-2]+list[-3]
print(max)
