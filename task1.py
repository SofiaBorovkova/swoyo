def prime_numbers(low: int, high: int) -> list[int]:
    '''Эта функция возвращает список в заданном диапазоне.'''
    number_list = []
    if high > low:
        for i in range(low, high):
            number_list.append(i)
        return number_list
    else:
        return []
