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
        with open(json_file_name + '.json', 'r') as read_file:
            template = json.load(read_file)
            words = (note['fields'][0] for note in template['notes'])
    except:
        pass

    return words


if __name__ == '__main__':

    for i, word in enumerate(get_data_from_json_file('deck')):
        print(i, word)

