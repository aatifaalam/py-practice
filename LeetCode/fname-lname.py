class Name:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def getFinalName(self):
        finalName = []
        j = len(self.lname)-1
        for i in range(len(self.fname)):
            finalName.append(self.fname[i] + " " + self.lname[j])
            j -= 1
        return finalName

fname = ["Aatif", "Taleev", "Wasif"]
lname = ["Aalam", "Aalam2", "Aalam3"]

fname2 = ["A", "B", "C"]
lname2 = ["D", "E", "F"]

fname3 = ["X", "Y", "Z"]
lname3 = ["L", "M", "N"]


n = Name(fname, lname)
n2 = Name(fname2, lname2)
n3 = Name(fname3, lname3)

finalName = n.getFinalName()
finalName2 = n2.getFinalName()
finalName3 = n3.getFinalName()

for i in finalName:
    print(i)
for i in finalName2:
    print(i)
for i in finalName3:
    print(i)