chi_dict = {}

def find_text(text):
    if len(text) == 0:
        print("Not found")
    elif text in chi_dict:
        print(chi_dict[text])
    else:
        find_text(text[:-1])

def main():
    input_str = open("input").readline()
    elem = input_str.split(",")
    for x in elem:
        raw = x.split()
        chi_dict[raw[0]] = raw[1:]

    text = input()
    while text != "exit()":
        find_text(text)
        text = input()

if __name__ == '__main__':
    main()