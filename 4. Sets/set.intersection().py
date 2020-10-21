englishLength = int(input()) # Length of English Student
englishRollNumber = set( map( int, input().split() ) ) # Roll Number of English Student


frenchLength = int(input()) # Length of French Student
frenchRollNumber = set( map( int, input().split() ) ) # Roll Number of Frehch Student

Operation = len( englishRollNumber.intersection(frenchRollNumber) )
print( Operation )

"""
    Note :- Set Intersection is Common Value Present in Both Set
"""