import json

clipboard = []

def to_clip_board():
    from tkinter import Tk

    if len(clipboard) == 1:
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(clipboard[0])
    elif len(clipboard) == 0:
        pass
    else:
        import getch
        while True:
            key = ord(getch.getch())
            print(str(range(49, 49+len(clipboard))))
            print(key)
            if key in range(49, 49+len(clipboard)):
                r = Tk()
                r.withdraw()
                r.clipboard_clear()
                r.clipboard_append(clipboard[key-49])
                print("clip to board: " + clipboard[key-49])
                break
            elif key == 27:
                break
            else:
                print("please choose in range")

def find_text(text, chi_dict):
    words = text.split()
    find_word(words, "", chi_dict)

def find_word(words, append, chi_dict):
    if len(words) == 0:
        print(append)
        clipboard.append(append)
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
    global clipboard
    while text != "exit()":
        clipboard = []
        find_text(text, chi_dict)
        to_clip_board()
        text = input()

if __name__ == '__main__':
    main()