def hIndex(citations):
    citations.sort(reverse=True)
    hindex = 0

    for i in range(len(citations)):
        if citations[i] >= i+1:
            hindex = i+ 1
        else:
            break
    return hindex

citations =[3,0,6,1,5]
print(hIndex(citations))