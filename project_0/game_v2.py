import numpy as np


def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min = 1
    max = 100
    print(max)
    #number = np.random.randint(min, max+1)
    while True:
        count+=1
        mid = round((max+min) / 2)
        
        if mid > number:
            max = mid
        elif mid < number:
            min = mid
        else:
            # print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break #конец игры выход из цикла
    print(count)
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    #np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score


#if __name__ == '__main__':
 #   score_game(random_predict)

