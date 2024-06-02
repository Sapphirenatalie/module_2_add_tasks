# На вход подаётся строка, некоторые слова в которой "испорчены".
# Признак "испорченного" слова - 1я буква в нём заменена на *.
# Выведете на печать список "не испорченных" слов.

str_ = 'drama, *torage, wife, *assion, *oem, presentation, *reference, candidate, *tranger'
print('строка: ', str_)
str_2 = str_.replace(',', '')
lst = str_2.split()


def find_right_word():

    check = '*'
    lst1 = []
    for word_ in lst:
        if word_[0] != check:
            lst1.append(word_)
    print('список "неиспорченных" слов: ', lst1)


find_right_word()
