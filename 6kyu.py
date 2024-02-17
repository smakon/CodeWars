words = {"A": ".-",
         "B": "-...",
         "C": "-.-.",
         "D": "-..",
         "E": ".",
         "F": "..-.",
         "G": "--.",
         "H": "....",
         "I": "..",
         "J": ".---",
         "K": "-.-",
         "L": ".-..",
         "M": "--",
         "N": "-.",
         "O": "---",
         "P": ".--.",
         "Q": "--.-",
         "R": ".-.",
         "S": "...",
         "T": "-",
         "U": "..-",
         "V": "...-",
         "W": ".--",
         "X": "-..-",
         "Y": "-.--",
         "Z": "--..",
         " ": " "
         }
result = " "
wordeee = []


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def word():
    global wordeee, words
    res = "".join(wordeee)
    val = words.values()
    if str(res) in val:
        global result
        result += get_key(words, res)
        wordeee.clear()
        return result
    else:
        print("Err")
        wordeee.clear()

