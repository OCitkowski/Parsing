import json


def get_words_from_file(full_file_name: str = None) -> list:
    words = []

    if full_file_name == None:
        return words

    file_txt = open(full_file_name, "r+")

    while True:
        row = file_txt.readline()
        if row == '':
            break
        else:
            new_word = row.split("|")[0]
            words.append(new_word)

    return words


def get_data_from_json_file(json_file_name):
    try:
        words = {}
        with open(json_file_name + '.json', 'r') as read_file:
            template = json.load(read_file)
            for note in template['notes']:

                len_row = len(note['fields'][0].split(' '))
                row = note['fields'][0].split(' ')

                if len_row > 2:
                    continue

                if row[0] in ['der', 'Der', 'die', 'das'] and len_row != 2:
                    continue

                item = note['fields'][12]
                value = [note['fields'][0], note['fields'][10], ' ', False]
                words[item] = value
    except:
        pass

    return words


def save_data_in_json_file(data, json_file_name):
    result = False
    try:
        with open(json_file_name, 'w') as write_file:
            json.dump(data, write_file, ensure_ascii=False)
            result = True
        print(f'{json_file_name}.json save to root')
    except:
        print(f'{json_file_name}.json don`t save to root')
    return result


def get_data_from_json_file2(json_file_name):
    try:
        with open(json_file_name, 'r') as read_file:
            template = json.load(read_file)
            # print(template)

    except:
        pass
    finally:
        read_file.close()

    return template


if __name__ == '__main__':
    words = get_data_from_json_file('deck')

    # for i, x in words.items():
    #     print(i, x)

    save_data_in_json_file(words, 'words2.json')

    words = get_data_from_json_file2('words2.json')

    for i, row in words.items():
        print(i, row)
