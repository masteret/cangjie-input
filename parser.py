import json

def find_text(text, chi_dict):
    if len(text) == 0:
        print("Not found")
    elif text in chi_dict:
        print(chi_dict[text])
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