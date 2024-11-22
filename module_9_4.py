#Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x,y: x == y, first, second)))

#Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a',encoding='utf-8') as file:
            for i in data_set:
                # Проверяем тип данных и приводим к строке
                if isinstance(i, list):
                    # Если это список, преобразуем его в строку
                    file.write(' '.join(map(str, i)) + '\n')
                else:
                    # Если это не список, просто записываем его
                    file.write(str(i) + '\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__:
from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words  # Сохраняем переданные слова в атрибуте words

    def __call__(self):
        return choice(self.words)  # Возвращаем случайное слово из words


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball.__call__())
print(first_ball.__call__())
print(first_ball.__call__())