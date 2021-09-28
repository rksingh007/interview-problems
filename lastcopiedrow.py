def copyListFromLastCheckPoint(l1, l2, v):
    lastwritten = v
    for i in range(v + 1, len(l1)):
        writeTokafka(l1[i],i)
        data =  readFromKafka():

        l2.append(l1[i])
        lastwritten += 1
        saveCheckPoint(lastwritten)

    print(l2)


def saveCheckPoint():


l1 = [8, 7, 3, 4]
l2 = []
lastCopiedRow(l1, l2, 1)
