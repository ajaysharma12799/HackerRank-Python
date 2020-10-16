def findSecondLargest(array):
    length = len(array)
    largest = secondLargest = -12345

    for i in range(0, length): # Finding Largest
        print(array[i])
        largest = max(array[i], largest)
    
    for i in range(0, length): # Finding Second Largest
        if array[i] != largest:
            secondLargest = max(array[i], secondLargest)

    print(secondLargest)

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    convertedList = []
    for i in arr:
        convertedList.append(i)
    
    findSecondLargest(convertedList)