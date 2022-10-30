def get_count_char(str_):
    dict_ = {}
    str_ = "".join(str_.lower().split())
    for letter in str(str_):
        if letter.isalpha():
            if letter not in dict_:
                dict_[letter] = 1
            else:
                dict_[letter] += 1

    return dict_


def percent(dict_):
    dict_new = {}
    total_count = sum(dict_new.values())
    for value in dict_new.values():
        value = round(value / total_count * 100, 1)
    return dict_new


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
