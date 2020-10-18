def swap_case(string):
    # print(string)
    convertedString = ""

    for char in string:
        if char >= "a" and char <= "z": # Lower Case
            convertedString += (char.upper())
        elif char >= "A" and char <= "Z": # UpperCase
            convertedString += (char.lower())
        else: # Special Character and Numbers
            convertedString += (char)

    return convertedString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

"""

Note :- We Have One More Approach That is To Play With ASCII Values

a-z = 97-122
A-Z = 65-90

"""