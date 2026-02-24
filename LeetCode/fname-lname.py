fname = ["Aatif", "Taleev", "Wasif"]
lname = ["Aalam", "Aalam2", "Aalam3"]

# reversedLname = []

# # lname.reverse()
# for i in range(len(lname) - 1, -1, -1):
#     reversedLname.append(lname[i])

j = len(lname)-1
finalName = []

for i in range(len(fname)):
    finalName.append(fname[i] + " " + lname[j])
    j -= 1

for i in range(len(finalName)):
    print(finalName[i])