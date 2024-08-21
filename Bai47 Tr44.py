tupleA = (1, 2, 3)
tupleB = (2, 3, 4, 5)
tupleC = (tupleA + tupleB)
print(tupleC)
tupleD = tupleC[::-1]
print(tupleD)
print(tupleD[0], tupleD[1])
print(tupleD[len(tupleD)-1], tupleD[len(tupleD)-2])