# A = Rock
# B = Paper
# C = Scissors

# X = Rock = 1
# Y = Paper = 2
# Z = Scissors = 3

# X = Lose = 0
# Y = Draw = 3
# Z = Win = 6

# if A X = 0 + 3
# if A Y = 3 + 1
# if A Z = 6 + 2

# if B X = 0 + 1
# if B Y = 3 + 2
# if B Z = 6 + 3

# if C X = 0 + 2
# if C Y = 3 + 3
# if C Z = 6 + 1

score = 0
max = 0
max2 = 0
max3 = 0
#Add up each entry
# If entry is more than previous highest entry overwrite the variable
#return variable with highest value
rps = open('Data2.txt','r')
data = rps.readlines()
for line in data:
    variable = line
    if "A X" in variable :
        score += 0 + 3   
    if "A Y" in variable :
        score += 3 + 1
    if "A Z" in variable :
        score += 6 + 2
    if "B X" in variable :
        score += 0 + 1    
    if "B Y" in variable :
        score += 3 + 2
    if "B Z" in variable :
        score += 3+6         
    if "C X" in variable :
        score += 0 + 2
    if "C Y" in variable :
        score += 3 + 3
    if "C Z" in variable :
        score += 6+1
print("score: ", score)
