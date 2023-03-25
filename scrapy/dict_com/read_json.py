import json


def get_words_from_json_file(full_file_name: str = None) -> list:
    words = []

    if full_file_name == None:
        return words

    # Відкрийте файл та завантажте його в змінну data
    with open('deck.json', 'r') as f:
        data = json.load(f)

    # Перезаписати значення "тут перезаповнити" на "******"
    for note in data['notes']:
        fields = note['fields']
        words.append(fields[0])

        # for i, field in enumerate(fields):
        #     print(i, field)
        #     if i == 2:
        #         fields[i] = "Ukr"
        #     elif i == 7:
        #         fields[i] = "german_alternatives"
        #
        # print(fields)

        # if field == "тут перезаповнити":
        #     fields[i] = "******"

    # # Зберегти нові дані у файл
    # with open('file.json', 'w') as f:
    #     json.dump(data, f)

    return words


def set_words_from_json_file(full_file_name: str = None) -> list:
    words = []

    if full_file_name == None:
        return words

    # Відкрийте файл та завантажте його в змінну data
    with open('deck.json', 'r') as f:
        data = json.load(f)

    # Перезаписати значення "тут перезаповнити" на "******"
    for note in data['notes']:
        fields = note['fields']
        words.append(fields[0])

        # for i, field in enumerate(fields):
        #     print(i, field)
        #     if i == 2:
        #         fields[i] = "Ukr"
        #     elif i == 7:
        #         fields[i] = "german_alternatives"
        #
        # print(fields)

        # if field == "тут перезаповнити":
        #     fields[i] = "******"

    # # Зберегти нові дані у файл
    # with open('file.json', 'w') as f:
    #     json.dump(data, f)

    return words


if __name__ == '__main__':
    print(get_words_from_json_file(full_file_name='deck.json'))
