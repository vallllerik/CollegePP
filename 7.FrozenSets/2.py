testList = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
printSet = set()
printSet1 = []
for i in testList:
    if type(i) == list or type(i) == set or type(i) == dict:
        printSet1.append(i)
    else:
        printSet.add(i)
if len(testList) == len(printSet1):
    print(True)
else:
    print(False)
print(printSet1)