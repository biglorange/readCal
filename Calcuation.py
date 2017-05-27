def readSummary() :
    filepath = "./Summary.OUT"
    f = open(filepath)
    str = f.readlines()[4]
    data = str.split()
    print(data[19])
    print(data[39])
    return data[19]+data[39]

def readOverview():
    filepath = "./OVERVIEW.OUT"
    f = open(filepath)

    for line in f.readlines()[62:70]:

    str = f.readlines()[62:70]
    print(str)

readOverview()