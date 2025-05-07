import json
import matplotlib.pyplot as plt

f1 = open("life_expectancy_original.csv", "r")
lines = f1.readlines()

dictionary ={}

years = lines[4].split(",")
can = lines[5].split(",")
mex = lines[6].split(",")
usa = lines[7].split(",")
ca = [
]
me = []
us = []
year = []
for i in range(5,66):
    year.append(int(years[i-1]))
    ca.append(float(can[i]))
    me.append(float(mex[i]))
    us.append(float(usa[i]))
print(ca)
dictionary["United States"] = {}
dictionary["Mexico"] = {}
dictionary["Canada"] = {}
for i in range(4,65):
    dictionary["United States"][int(years[i])] = float(usa[i+1])
    dictionary["Mexico"][int(years[i])] = float(mex[i+1])
    dictionary["Canada"][int(years[i])] = float(can[i+1])

print(dictionary)

# Create the dictionary here
f1.close()

#Save the json object to a file
f2 = open("life_expectancy.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()

# plt.plot(year,us)
# plt.plot(year,me)
# plt.plot(year,ca)
# # plt.yticks([50,60,70,80,90])
# plt.xticks([1960,1970,1980,1990,2000,2010,2020])
# plt.show()