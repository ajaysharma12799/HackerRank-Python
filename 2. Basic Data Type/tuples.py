if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    array = []
    for i in integer_list:
        array.append(i)
    
    convertedTuple = tuple(array)
    print( hash(convertedTuple) )
    
    """
        hash(value) => Return hash value of passed object if any
        Hash Value are just integer that are used for comparing two dictionary
        hash() method internally call __hash__() of an object that is internally and "SET" by default for na object
    """