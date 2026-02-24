fname = ["Aatif", "Taleev", "Wasif"]
lname = ["Aalam", "Aalam2", "Aalam3"]

finalName = []
#this parameter 0 is unncessary in range method since start=0 already by default
for i in range(0, len(fname)):
    finalName.append(fname[i] + " " + lname[i])
    print(finalName[i])

#create a seperate loop on finalName to print the full names
