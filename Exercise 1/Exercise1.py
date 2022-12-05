compare = 0
max = 0
max2 = 0
max3 = 0
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
        if compare >= max:
            #print("I made it to compare>max")
            max = compare
            #print(max)
            compare = 0
        if compare > max2:
            max2 = compare
            compare =0
        if compare > max3:
            max3 = compare
            compare=0
        else:
            #print("I set it to zero whoops")
            compare = 0
print("elf1: ",max)
print("elf2: ",max2)
print("elf3: ",max3)
max = max+max2+max3        
print("maximum calorie: ", max)
