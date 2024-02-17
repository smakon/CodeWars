def to_camel_case(text):
    text = list(text)
    text2 = " "
    for i in range(len(text)):
        if text[i] == '_' or text[i] == '-':
            text[i] = ''
            text[i + 1]= str(text[i+1]).upper()
        else:
            text2="".join(map(str, text))
    return text2

