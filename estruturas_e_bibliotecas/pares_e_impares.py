numberList = []
pairList = []
oddList = []

## functions
def bubbleSort(vector):
    for i in range(len(vector) - 1):
        for j in range(len(vector) - 1):
            if(vector[j+1] < vector[j]):
                vector[j], vector[j + 1] = vector[j + 1], vector[j]

def reverseBubbleSort(vector):
    for i in range(len(vector) - 1):
        for j in range(len(vector) - 1):
            if(vector[j+1] > vector[j]):
                vector[j], vector[j + 1] = vector[j + 1], vector[j]


# code
qtd = int(input())
for number in range(qtd):
    n = int(input())
    if(n % 2 == 0):
        pairList.append(n)
    else:
        oddList.append(n)

bubbleSort(pairList)
reverseBubbleSort(oddList)

# output
for number in pairList:
    print (number)
    
for number in oddList:
    print (number)