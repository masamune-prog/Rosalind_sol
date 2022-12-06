with open('input.txt') as f:
    weights = []
    for i in f:
        weights.append(float(i.rstrip('\n')))




massTableDictionary = {"A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259,
            "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406,
            "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293,
            "P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203,
            "T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333}

#print(weights)
diff = []
for j in range(1,len(weights)):
    diff.append(weights[j]-weights[j-1])
masses = list(massTableDictionary.values())
takeClosest = lambda num,collection:min(collection,key=lambda x:abs(x-num))
ans_masses = []
for d in diff:
    ans_masses.append(takeClosest(d,masses))
inverse_dict = {v: k for k, v in massTableDictionary.items()}
for weights in ans_masses:
    print(inverse_dict[weights],end = '')
