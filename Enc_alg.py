ua_alf = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'а', 'м', 'н', 'о', 'п', 'р',
          'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']

morze_ua = []

ua_dict = dict(zip(ua_alf, morze_ua))

eng_alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

morze_eng = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', '._..', '__', '_.', '___',
             '.__.', '__._', '._.', '...', '_', '.._', '..._', '.__', '_.._', '_.__', '__..']

eng_dict = dict(zip(eng_alf, morze_eng))

symbols = ['.', ',', ':', ';', '!', '?', ' ', '-', '(', ')', '`', '\'', '\"', '_']


def input_text():
    return input("Enter your text: ")


def language_type(a):
    pass


def encrypt(text: str):
    key = ''
    morze_list = []
    work_text = text.lower()

    for j in range(len(symbols)):  # delete special symbols
        work_text = work_text.replace(symbols[j], '')

    work_text = list("".join(work_text))  # split text by letters

    for i in range(len(work_text)):  # convert text to morze
        morze_list.append(eng_dict.get(work_text[i]))

    for i in range(len(morze_list)):  # key creator, 1 part
        key = key + str(len(morze_list[i]))

    for obj in range(len(morze_list)):  # convert morze text to 01
        for sumb in range(len(morze_list[obj])):
            if morze_list[obj][sumb] == ".":
                morze_list[obj] = morze_list[obj][:sumb] + "0" + morze_list[obj][sumb + 1:]
            else:
                morze_list[obj] = morze_list[obj][:sumb] + "1" + morze_list[obj][sumb + 1:]

    encoded_text = ''.join(morze_list)
    count = 0

    for i in encoded_text:
        if i == "0":
            count += 1
        else:
            break
    key = str(count) + "." + key

    message = int(encoded_text, 2)

    #parne or neparne

    return message, key


if __name__ == '__main__':
    word = input_text()
    # word = "Hello, World!"
    print(encrypt(word))

