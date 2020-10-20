"""

    any() function return true if any item in iterable is true otherwise false

"""
def validateString(stringArray):
    print( any( c.isalnum() for c in stringArray ) )
    print( any( c.isalpha() for c in stringArray ) )
    print( any( c.isdigit() for c in stringArray ) )
    print( any( c.islower() for c in stringArray ) )
    print( any( c.isupper() for c in stringArray ) )

if __name__ == '__main__':
    s = input()
    convertedString = list(s)
    validateString(convertedString)