englishLength = int(input()) # Length of English Student
englishRollNumber = set( map( int, input().split() ) ) # Roll Number of English Student


frenchLength = int(input()) # Length of French Student
frenchRollNumber = set( map( int, input().split() ) ) # Roll Number of Frehch Student

Operation = len( englishRollNumber.symmetric_difference(frenchRollNumber) )
print( Operation )

"""
    Note :- Symmetric Difference of Two Set is The Set of All Those Element Which Belong To Either of One Set but Not To Both
            Symmetric Difference is Denoted By ^
            
            Example :- A ^ B = ( A U B ) - ( A ∩ B )
"""