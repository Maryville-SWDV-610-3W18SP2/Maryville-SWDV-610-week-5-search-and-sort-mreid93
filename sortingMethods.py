"""bubbleSort will pass through a list len-1 times, comparing every pair of items at each pass
   this will take up more time than other sorting methods because we have to go through our list
   so many times and make comparisons at each step"""
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
"""selectionSort is a more refined function than bubbleSort. It will pass through once, finding the
   largest value, placing it at the end of the list. Then, it will pass once more, finding the largest remaining
   value, putting it at the spot just before the largest value, and so on. This will take less time
   and consume less processing power than bubbleSort"""
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

"""insertionSort is strange. It will begin by creating a sublist of the first item in our list.
   Next, we will add the second item in our list to the sublist and sort the two. We continue building
   our sublist until we have sorted the span of the original list. It functions much differently
   from the previous two as it creates a new list and doesnt pass through our initial list."""
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
        alist[position]=currentvalue
        

alist = [1,2,3,4,5,6,7,8,9,10]
bubbleSort(alist)
selectionSort(alist)
insertionSort(alist)
