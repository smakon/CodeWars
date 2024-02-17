def disemvowel(string):
    a = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    string = list(string)
    text2 = ""
    for i in range(len(string)):
        if string[i] in a:
            string[i] = ''
            text2="".join(map(str, string))
    return text2

print(disemvowel('ESRA'))
