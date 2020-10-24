setA_length = int(input())
setA = set(map(int, input().split()))
operation_length = int(input())
for _ in range(operation_length):
    cmd, _ = input().split()
    setB = set(map(int, input().split()))
    if cmd == "intersection_update":
        setA.intersection_update(setB)
    elif cmd == "update":
        setA.update(setB)
    elif cmd == "symmetric_difference_update":
        setA.symmetric_difference_update(setB)
    elif cmd == "difference_update":
        setA.difference_update(setB)

print( sum(setA) )