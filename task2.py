import string


def text_stat(filename: str) -> dict:
    '''Эта функция возвращает статистику текста.'''
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        return {'error': 'File not found'}

    # Создаем счетчик.
    rus_alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    letters_stat = {
        letter: [0, 0] for letter in (string.ascii_letters + rus_alp)
    }

    # Считаем количество слов, параграфов, билингвальных слов.
    text = text.lower()
    words = text.split()
    word_amount = len(words)
    paragraph_amount = text.count('\n') + 1
    bilingual_word_amount = 0
    for word in words:
        bil_rus = 0
        bil_eng = 0
        for letter in word:
            if letter in letters_stat:
                letters_stat[letter][0] += 1
            if letter in rus_alp:
                bil_rus += 1
            elif letter in string.ascii_letters:
                bil_eng += 1
        if bil_rus != 0 and bil_eng != 0:
            bilingual_word_amount += 1

    # Считаем долю слов.
    for letter in letters_stat:
        if letters_stat[letter][0] > 0:
            s = 0
            for word in words:
                if letter in word:
                    s += 1
            letters_stat[letter][1] = s / word_amount

    # Удаляем неиспользуемые буквы и преобразовываем в tuple.
    letters_stat = {k: tuple(v) for k, v in letters_stat.items() if v[0] > 0}

    return {
        'letters_stat': letters_stat,
        'word_amount': word_amount,
        'paragraph_amount': paragraph_amount,
        'bilingual_word_amount': bilingual_word_amount
    }
