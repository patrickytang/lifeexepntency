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

avg = 0
avg2 = 0
for i in range(4,65):
    avg += (float(mex[i+1]) + float(usa[i+1]) + float(can[i+1]))
    avg2+=3
    dictionary[int(years[i])] = {}
    dictionary[int(years[i])]["United States"] = float(usa[i+1])
    dictionary[int(years[i])]["Mexico"] = float(mex[i+1])
    dictionary[int(years[i])]["Canada"] = float(can[i+1])
    dictionary[int(years[i])]["Mean"] = (float(mex[i+1]) + float(usa[i+1]) + float(can[i+1]))/3
    
print(avg/avg2)
dictionary["Meaner"] = avg/avg2
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