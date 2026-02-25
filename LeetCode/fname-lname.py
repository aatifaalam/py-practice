fname = ["Aatif", "Taleev", "Wasif"]
lname = ["Aalam", "Aalam2", "Aalam3"]

j = len(lname)-1

def getFinalName():
    finalName = []
    j = len(lname)-1
    for i in range(len(fname)):
        finalName.append(fname[i] + " " + lname[j])
        j -= 1
    return finalName
finalName = getFinalName()
for i in range(len(finalName)):
    print(finalName[i])



print(getFinalName())



# def fun():
#     print("Hello, World!")
# fun()

# def fun2():
#     print("Hello, World!2")
# fun2()


