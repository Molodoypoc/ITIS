# задание 1
# 1. а не больше b
# 2. a!= b
# 3. ошибок нет
# 4. ошибок нет
# 5. 1 не может быть больше 1
# 6. 2 не может быть больше 2

# задание 2
password = 'Дракон-капуста'
input_password = input()
if input_password == password:
    print('да')
else: print('нет')

# задание 3
string1 = input()
string2 = input()
if len(string1) > len(string2):
    print(string1)
else: print(string2)

# задание 4
number = int(input())
if number % 2 == 0:
    print('чётное')
else: print('нечётное')

# задание 5
input_data = input()
string = '0123456789'
if all(x in string for x in input_data):
    print('Дa')
else: print('Heт')

# задание 6
import random
input_number = int(input('Введите число от 1 до 10: '))
random_number = random.randint( 1, 10)
if input_number == random_number: print('Угадал, поздравляю')

# задание 7
vowels = 'аеёиоуыэюя'
consonants = 'бвгджзйклмнпрстфхчцшщ'
input_letter = input().lower()
if input_letter in vowels: print('гласная')
elif input_letter in consonants: print('согласная')
else: print('неверный ввод')

# задание 8
a, b, c = int(input()), int(input()), int(input())
if a == b == c: print('равносторонний')
elif a == b or b == c or a == c: print('равнобедренный')
else: print('разносторонний')

# задание 9
height = int(input())
if 80 <= height <= 130: print('Всё в порядке')
else: print('В посещении отказано!')

# задание 10
height = int(input())
if 90 <= height <= 105: print('Вход только в сопровождении взрослых')
elif height > 105: print('Всё в порядке проходите')
else: print('В посещении отказано!')

# задание 11
number = int(input())
if 0 <= number <= 24: print('Ужасно, оценка 0')
elif 25 <= number <= 44: print('Плохо, оценка 1')
elif 45 <= number <= 64: print('Сойдёт, оценка 2')
elif 65 <= number <= 79: print('Средне, оценка 3')
elif 80 <= number <= 89: print('Хорошо, оценка 4')
elif 90 <= number <= 100: print('Отлично, оценка 5')
else: print('ОШИБКА')

# задание 12
input_money= int(input())
if input_money== 10: print('Красноярск')
elif input_money == 50: print('Санкт-Петербург')
elif input_money == 100: print('Mocква')
elif input_money == 200: print('Севастополь')
elif input_money == 500: print('Архангельск')
elif input_money== 1000: print('Ярославль')
elif input_money== 2000: print('Владивосток')
elif input_money == 5000: print('Хабаровск')
else: print('ОШИБКА')

# задание 13
question1 = input('Kормит детей молоком?\n')
if question1 == 'да':
    question2 = input('Ест мяco?\n')
    if question2 == 'да': print('хищник')
    else: print('в базе нет такого типа животного')
else:
    question2 = input('Имеет перья?\n')
    if question2 == 'дa': print('птица')
    else: print('в базе нет такого типа животного')