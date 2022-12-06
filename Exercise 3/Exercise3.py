# cut the strings in half
# find the common character in each string between the two
# assign a value 1-52
score = 0
d = {}
setlist = []
total = 0
with open("Score3.txt") as f:
    for line in f:
        (key, val) = line.split()
        d[key] = val

#print (d)
rps = open('Data3.txt','r')
data = rps.readlines()
for line in data:
    variable = line
    length = len(variable)
    half= length//2
    string1 = slice(0,half)
    string2 = slice(half,length)
    common = set.intersection(set(variable[string1]),set(variable[string2]))
    #print(common)
    setlist = setlist + list(common)
    
    #print(mylist)
# creating inverse dictionary of elements 
temp = {j : i for i, k in d.items() for j in k}
# creating end result by mapping elements
res = [temp.get(key) for key in setlist]

for x in range(len(res)):
    total += int(res[x])
print("score: ", total)
#must add all values togeteher still
