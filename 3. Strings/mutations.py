def mutate_string(string, position, character):
    convertedString = list(string)
    length = len(convertedString)

    for i in range(0, length):
        if i == position:
            convertedString[i] = character
    
    changedString = "".join(convertedString)
    return changedString

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)