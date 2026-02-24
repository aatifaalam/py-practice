fname = ["Aatif", "Taleev", "Wasif"]
lname = ["Aalam", "Aalam2", "Aalam3"]

reversedLname = []

# lname.reverse()
for i in range(len(lname) - 1, -1, -1):
    reversedLname.append(lname[i])

finalName = []
j = len(lname)-1
for i in range(len(fname)):
    finalName.append(fname[i] + " " + reversedLname[i])

for i in range(len(finalName)):
    print(finalName[i])
