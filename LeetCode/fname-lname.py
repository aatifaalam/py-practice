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

n = Name(fname, lname)

finalName = n.getFinalName()

for i in finalName:
    print(i)