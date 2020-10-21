englishLength = int(input()) # Length of English Student
englishRollNumber = set( map( int, input().split() ) ) # Roll Number of English Student


frenchLength = int(input()) # Length of French Student
frenchRollNumber = set( map( int, input().split() ) ) # Roll Number of Frehch Student

Operation = len( englishRollNumber.union(frenchRollNumber) )
print( Operation )

"""
    Note :- Set Union is Combination of All Value Present in Both Set
"""