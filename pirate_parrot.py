pirate_replacements = {
    'hello': 'ahoy',
    'stop': 'avast',
    'yes': 'aye',
    'my': 'me',
    'you': 'ye',
    'sweetie': 'matey',
    'wow': 'shiver me timbers'
}


def make_piratey(user_input):
    input_words = user_input.split()
    output_words = []
    for word in input_words:
        output_words.append(pirate_replacements.get(word, word))
    output = ' '.join(output_words)
    return output


if __name__ == '__main__':
    while True:
        user_input = raw_input('> ')
        if user_input.lower() == 'exit':
            break
        print make_piratey(user_input)
