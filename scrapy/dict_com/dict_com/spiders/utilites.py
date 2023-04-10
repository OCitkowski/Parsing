import json, os


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


def get_words_from_file_2(full_file_name: str = None) -> list:
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


def save_data_in_json_file(data, json_file_name):
    result = False
    try:
        with open(json_file_name, 'w') as write_file:
            json.dump(data, write_file, ensure_ascii=False, indent=2)
            result = True
        print(f'{json_file_name}.json save to root')
    except:
        print(f'{json_file_name}.json don`t save to root')
    return result


def get_data_from_json_file_deck(json_file_name):
    try:
        words = []
        with open(json_file_name + '.json', 'r+') as read_file:
            template = json.load(read_file)
            for i, note in enumerate(template['notes']):

                len_row = len(note['fields'][0].split(' '))
                row = note['fields'][0].split(' ')

                if len_row > 2:
                    continue

                if row[0] in ['der', 'Der', 'die', 'das'] and len_row != 2:
                    continue

                words.append(
                    {i: {
                        "word": note['fields'][0],
                        "id": note['fields'][12],
                        "translation": '',
                        "part_of_speech": note['fields'][10],
                        "german_alternatives": '',
                        "status": False
                    }})

    except:
        pass

    return words


def get_data_from_json_file_words(json_file_name):
    row = []

    try:
        with open(json_file_name, 'r') as file:
            data = json.load(file)

        for item in data:
            for key, value in item.items():

                if value['status'] == False:
                    row.append([value['word'],
                                value['id'],
                                value['status']])

    except Exception as ex:
        print(ex, os.path.abspath(__file__))

    return row


if __name__ == '__main__':
    words = get_data_from_json_file_deck('deck')

    save_data_in_json_file(words, 'words.json')

    file_json = '/home/fox/PycharmProjects/python_parsing/scrapy/dict_com/dict_com/spiders/words.json'
    words = get_data_from_json_file_words(file_json)
    for row in words:
        # if row != None:
        print(row[1])

    #
    # start_urls = [f"https://dict.com/ukrainisch-deutsch/{row}" for row in words]
