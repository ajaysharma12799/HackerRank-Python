def split_and_join(line):
    splitedString = line.split(" ")
    splitedString = "-".join(splitedString)
    return splitedString

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)