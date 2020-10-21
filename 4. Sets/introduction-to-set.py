def average(array):
    convertedList = set(array)
    setSum = sum(convertedList)
    length = len(convertedList)
    return setSum/length

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)