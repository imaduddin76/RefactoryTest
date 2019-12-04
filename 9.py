def BubbleSort(val):
    for passnum in range(len(val) - 1, 0, -1):
        for i in range(passnum):
            if val[i] > val[i + 1]:
                temp = val[i]
                val[i] = val[i + 1]
                val[i + 1] = temp


ListAngka = [123, 27, 532, 9, 44, 815, 211, 420]
BubbleSort(ListAngka)
print(ListAngka)