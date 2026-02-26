fname = ["Aatif", "Taleev", "Wasif"]
lname = ["Aalam", "Aalam2", "Aalam3"]

j = len(lname)-1

finalName = []
j = len(lname)-1
for i in range(len(fname)):
    finalName.append(fname[i] + " " + lname[j])
    j -= 1

def getFinalName():
    return finalName

for i in range(len(getFinalName())):
    print(getFinalName()[i])