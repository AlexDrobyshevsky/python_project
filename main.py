
import random

words_list = [
    "яблоко",
    # "змей", "лев", "гора", "тетрадь", "апельсин", "карандаш", "королева", "река", "солнце",
    # "дерево", "зонт", "ваза", "кит", "ксилофон", "яхта", "зебра", "мяч", "кошка", "дельфин", "яйцо", "банан",
    # "машина", "собака", "слон", "цветок", "гитара", "дом", "остров", "куртка", "рыба", "виноград", "шляпа", "лед",
    # "кувшин", "ключ", "лампа", "луна", "гнездо", "сова", "пианино", "одеяло",
    # "кольцо", "звезда", "стол", "единорог", "вулкан", "парк", "музей", "замок", "дверь", "море",
    # "лес", "книга", "стул", "окно", "вокзал", "песок", "молоко", "ветер", "снег", "дождь", "хлеб", "сыр",
    # "кафе", "музыка", "колесо", "птица", "река", "часы", "лестница", "балкон", "сапог", "пальма", "письмо",
    # "кровать", "подушка", "спальня", "ковёр", "лампа", "кофе", "чай", "сок", "кресло", "диван",
    # "радио", "пульт", "экран", "кино", "парк", "дружба", "семья", "друг", "улица", "сумка", "картина", "чашка",
    # "тарелка", "ложка", "вилка", "нож", "полка", "шкаф"
]  # СПИСОК СЛОВ ДЛЯ УГАДЫВАНИЯ, ВЫБИРАЕТСЯ РАНДОМНО


def display_hangman(tries):  # ФУНКЦИЯ ОТОБРАЖЕНИЯ ВИСЕЛИЦЫ, СОСТОИТ ИЗ СПИСКА [0-5]
    stages = [
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / \\
        |
        |  ПОВЕШЕН, СЛЕДУЮЩИЙ

        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    /
        |
        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |
        |
        ''',
        '''
        _______
        |     |
        |     O
        |    \|
        |     |
        |
        |
        ''',
        '''
        _______
        |     |
        |     O
        |     |
        |     |
        |
        |
        ''',
        '''
        _______
        |     |
        |     O
        |
        |
        |
        |
        ''',
        '''
        _______
        |     |
        |
        |
        |
        |
        '''
    ]
    return stages[tries]


def get_word(word_list):  # Ф-ИЯ РАНДОМНО ВЫБИРАЕТ СЛОВО И СПИСКА
    return random.choice(word_list).upper()


def input_check():  # Ф-ИЯ ПРОВЕРЯЕТ В ВВОД НА ПУСТОТУ, ПРОБЕЛЫ, ЛИШНИЕ СИМВОЛЫ
    while True:
        answer_let = input('Введите букву или слово целиком: ').upper()
        if not answer_let.strip():
            print('Строка не может быть пустой, повтори ввод')
            continue
        if not answer_let.replace(' ', '').isalpha():
            print('Вы ввели не букву, повторите ввод: ')
            continue
        return answer_let


def check_guess_list_letter(answer_let, guessed_letters):
    # Ф-ИЯ ПРОВЕРЯЕТ ЕСТЬ ЛИ ВВЕДЕННАЯ БУКВА В СПИСКЕ ВВЕДЕНЫХ БУКВ
    while True:
        if answer_let in guessed_letters:
            print('Вы уже вводили эту букву, введи новую')
            return True
        return False


def check_guess_list_words(answer_let, guessed_words):
    # Ф-ИЯ ПРОВЕРЯЕТ ЕСТЬ ЛИ ВВЕДЕННООЕ СЛОВО В СПИСКЕ ВВЕДЕНЫХ СЛОВ
    while True:
        if answer_let in guessed_words:
            print('Вы уже вводили это слово, повтори ввод')
            return True
        return False


def subtraction_tries(tries, word_completion):  # Ф-ИЯ  УМЕНЬШЕНИЯ КОЛИЧЕСТВА ПОПЫТОК

    tries -= 1
    print(f"Нет такой буквы, осталось {tries} попыток/тки {display_hangman(tries)} {''.join(word_completion)}")
    return tries


def print_victory(word):  # ВЫВОДИТ ПРИНТ -> (ВЫ ПОБЕДИЛИ)
    print(f'Поздравляю вы угадали загаданное слово {word} ')


def check_char(answer_let, word, word_completion):
    # Ф-ИЯ ПОСИМВОЛЬНО ПРОВЕРЯЕТ ЗАДАННУЮ БУКВУ В СЛОВЕ И МЕНЯЕТ _ НА БУКВУ
    for i in range(len(word)):
        if word[i] == answer_let:
            word_completion[i] = answer_let
    print(''.join(word_completion))


def play(word):  # Ф-ИЯ ОСНОВНАЯ ЛОГИКА ИГРЫ
    word_completion = ['_'] * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print('Давайте играть в угадайку слов!')
    print(f'Тебе доступно {tries} попыток: {display_hangman(tries)} ')
    print('Загаданное слово -> ', ''.join(word_completion))

    while tries > 0:
        answer_let = input_check()  # Ф-ИЯ ПРОВЕРЯЕТ В ВВОД НА ПУСТОТУ, ПРОБЕЛЫ, ЛИШНИЕ СИМВОЛЫ

        if len(answer_let) == 1:
            # Ф-ИЯ ПРОВЕРЯЕТ ЕСТЬ ЛИ ВВЕДЕННАЯ БУКВА В СПИСКЕ ВВЕДЕНЫХ БУКВ
            if check_guess_list_letter(answer_let, guessed_letters):
                continue

            guessed_letters.append(answer_let)

            if answer_let not in word:
                # ЕСЛИ БУКВЫ НЕТ В СЛОВЕ, ВЫЗЫВАЕНТСЯ Ф-ИЯ УМЕНЬШЕНИЯ ПОПЫТОК
                tries = subtraction_tries(tries, word_completion)

            else:
                #  Ф-ИЯ ПОСИМВОЛЬНО ПРОВЕРЯЕТ ЗАДАННУЮ БУКВУ В СЛОВЕ И МЕНЯЕТ _ НА БУКВУ
                check_char(answer_let, word, word_completion)

                if '_' not in word_completion:
                    print_victory(word)  # Ф-ИЯ ВЫВОДИТ ПРИНТ -> (ВЫ ПОБЕДИЛИ)
                    break


        elif len(answer_let) == len(word):
            # Ф-ИЯ ПРОВЕРЯЕТ ЕСТЬ ЛИ ВВЕДЕННООЕ СЛОВО В СПИСКЕ ВВЕДЕНЫХ СЛОВ
            if check_guess_list_words(answer_let, guessed_words):
                continue

            guessed_words.append(answer_let)

            if answer_let == word:
                print_victory(word)  # ВЫВОДИТ ПРИНТ -> (ВЫ ПОБЕДИЛИ)
                break
            else:
                # ЕСЛИ БУКВЫ НЕТ В СЛОВЕ, ВЫЗЫВАЕНТСЯ Ф-ИЯ УМЕНЬШЕНИЯ ПОПЫТОК
                tries = subtraction_tries(tries, word_completion)

        else:
            if len(answer_let) > len(word):
                print('Вы ввели больше символов, чем в загаданном слове, будьте внимательны, не буду вас вешать')
            else:
                print('Вы должны ввести 1 букву или слово целиком, сегодня не буду вас вешать')

    if tries == 0:
        print(f'Вы проиграли загаданное слово было {word}')


while True:
    print('Сыграем в смертельно опасную игру? ')
    x = input('ДА/НЕТ: ').lower().strip()
    if x == 'да':
        word = get_word(words_list)
        play(word)
    else:
        print('Очень жаль, сыграем в другой раз')
        break
