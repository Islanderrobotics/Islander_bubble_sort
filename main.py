def BubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if (array[j]>array[j+1]):
                array[j],array[j+1] = array[j+1],array[j]


if __name__ == '__main__':
    array = [30,43,69,20,1,90]
    print(f"this is the array before sorting {array}")
    BubbleSort(array)
    print(f"this is the array after sorting {array}")