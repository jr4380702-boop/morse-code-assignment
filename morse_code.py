
alphabet_to_morse_code = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--. ",
    " ": "  ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "0": "----- ",
}

morse_code_to_alphabet = {
    ".- ": "A",
    "-... ": "B",
    "-.-. ": "C",
    "-.. ": "D",
    ". ": "E",
    "..-. ": "F",
    "--. ": "G",
    ".... ": "H",
    ".. ": "I",
    ".--- ": "J",
    "-.- ": "K",
    ".-.. ": "L",
    "-- ": "M",
    "-. ": "N",
    "--- ": "O",
    ".--. ": "P",
    "--.- ": "Q",
    ".-. ": "R",
    "... ": "S",
    "- ": "T",
    "..- ": "U",
    "...- ": "V",
    ".-- ": "W",
    "-..- ": "X",
    "-.-- ": "Y",
    "--. ": "Z",
    "  ": " ",
    ".---- ": "1",
    "..--- ": "2",
    "...-- ": "3",
    "....- ": "4",
    "..... ": "5",
    "-.... ": "6",
    "--... ": "7",
    "---.. ": "8",
    "----. ": "9",
    "----- ": "0",
}



def encode(prompt:str):
    """converts english to morse code"""
    prompt = prompt.upper().strip()
    str = ""
    for i in range(len(prompt)):
        if alphabet_to_morse_code.get(prompt[i]):
            str = f"{str}{alphabet_to_morse_code[prompt[i]]}"
        else:
            print(f"[Warning] Character {prompt[i]} not recognized. Skipped. ")
    return str

def decode(prompt:str):
    """converts morse code to english"""
    prompt = f"{prompt} "
    str = ""
    letter = ""
    last_letter = ""
    for i in range(len(prompt)):
        if prompt[i] == "." or prompt[i] == "-":
            last_letter = ""
            letter = f"{letter}{prompt[i]}"
        elif last_letter == "  ":
            str = f"{str}{morse_code_to_alphabet[last_letter]}"
        else:
            if morse_code_to_alphabet.get(f"{letter} ") and letter != "":
                str = f"{str}{morse_code_to_alphabet[f"{letter} "]}"
            elif letter.count(".") > 0 or letter.count("-") > 0:
                print(f"[Warning] Sequence {letter} not recognized. Skipped. ")
            elif letter != "":
                print(f"[Warning] Character {prompt[i]} not recognized. Skipped. ")
            last_letter = f"{last_letter} "
            letter = ""
    return str