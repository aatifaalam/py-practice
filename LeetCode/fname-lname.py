fname = ["Aatif", "Taleev", "Wasif"]
lname = ["Aalam", "Aalam2", "Aalam3"]

lname.reverse()
finalName = []
for i in range(len(fname)):
    finalName.append(fname[i] + " " + lname[i])

for i in range(len(finalName)):
    print(finalName[i])