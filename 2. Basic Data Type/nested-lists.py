n = int(input())
marksheet = []
gradelist = []

if __name__ == '__main__':
    for _ in range(n):
        name = input()
        score = float(input())
        marksheet.append([name, score]) # Creating Nested List of Name and Score
        gradelist.append(score) # Creating List of Score
    
    sortedList = (sorted(set(gradelist)))[1]
    """
        1. First Convert ScoreList into Set To Remove Duplicate
        2. Sort List in Increasing Order Using Sorted Method
        3. Take 1 Argument From List
    """
    for i, j in sorted(marksheet): # Traverse Whole Marksheet List and Extract Name and Marks
        if j == sortedList: # If Marks is Equal to SortedList or Fetched Marks Then Print Name
            print(i)
