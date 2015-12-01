import json

def find_text(text, chi_dict):
    words = text.split()
    find_word(words, "", chi_dict)

def find_word(words, append, chi_dict):
    if len(words) == 0:
        print(append)
    else:
        for word in _find_text(words[0], chi_dict):
            if word != "Not Found":
                find_word(words[1:], append+word, chi_dict)


def _find_text(text, chi_dict):
    if len(text) == 0:
        return "Not Found"
    elif text in chi_dict:
        return chi_dict[text]
    else:
        find_text(text[:-1], chi_dict)

def main():
    chi_dict = json.load(open("chi_dict.json"))

    text = input()
    while text != "exit()":
        find_text(text, chi_dict)
        text = input()

if __name__ == '__main__':
    main()