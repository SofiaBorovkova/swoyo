from typing import Union


def roman_numerals_to_int(roman_numeral: str) -> Union[int, None]:
    '''Эта функция переводит риимское число в арабское.'''
    rom_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    count = 0
    for i, v in enumerate(roman_numeral):
        if not rom_num.get(v):
            return None
        elif (i+1 < len(roman_numeral)
                and rom_num[v] < rom_num[roman_numeral[i+1]]):
            count -= rom_num[v]
        else:
            count += rom_num[v]
    return count
