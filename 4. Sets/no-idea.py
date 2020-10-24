n, m = input().split()
array = input().split()
likeArray = set(input().split())
dislikeArray = set(input().split())

print( sum(( i in likeArray ) - ( i in dislikeArray ) for i in array ))