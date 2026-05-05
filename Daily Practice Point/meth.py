class Name:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def getfinalName(self):

        finalName = []

        for i in range(len(self.fname)):

            if i == 0:
                finalName.append(self.fname[i] + " " + self.lname[i])

            else:
                finalName.append(self.fname[len(self.fname) - 1] + " " + self.lname[i])    

        return finalName
    
fname = ["Aatif", "Taleev", "Wasif"]
lname = ["Aalam", "Aalam2", "Aalam3"]

n = Name(fname, lname)

finalName = n.getfinalName()
for i in finalName:
    print(i)
               