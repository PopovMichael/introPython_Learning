# 1
# У вас есть список my_list со значениями типа int. Распечатать те значения,
# которые больше 100. Задание выполнить с помощью цикла for.
my_list = [95, 105, 90, 110, 85, 115]
for value in my_list:
    if value < 100:
        my_list.remove(value)
print(my_list)

####################

# 2
# У вас есть список my_list со значениями типа int и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results. Задание выполнить с помощью цикла for.
my_list = [95, 105, 90, 110, 85, 115]
my_results = []
for value in my_list:
    if value > 100:
        my_results.append(value)
print(my_results)

####################

# 3
# У вас есть список my_list со значениями типа int.
# Если в my_list кол-во элементов < 2, то в конец добавить значение 0.
# Если кол-во элементов >= 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list).
my_list = [95, 105, 90, 110, 85, 115]
# my_list = [95]  # для быстрой проверки
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)

####################

# 4
# Пользователь вводит value - число с запятой (например 3.14) с клавиатуры.
# Вы приводите это value к типу float и выводите результат выражения value ** -1.
# Написать программу, которая вычисляет данное выражение и корректно
# обрабатывает возможные исключения.
value = input("Введите число с точкой: ")
try:
    value = float(value)
    result = value ** -1
except (ValueError, TypeError):
    print("Не вверный ввод!")
    print("Используйте только цифровые значения.")
    value = 0
    result = 1
except ZeroDivisionError:
    print("Не вверный ввод!")
    print("Ноль не может быть возведен в отрицательную степень.")
    value = 0
    result = 1
print(result)

####################

# 5
# У вас есть список my_list со значениями типа int и пустой список my_results.
# Добавить в my_results те значения из my_list для которых сумма индекса и значения
# будет четной. Пример. [1, 11, 20, 100]. Ответ [11, 20], потому что:
# индекс 1 + значение 11 это 12 - четное,
# индекс 2 + значение 20 это 22 - четное.
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
my_results = []
for index, value in enumerate(my_list):
    new_value = index + value
    if not new_value % 2:
        my_results.append(new_value)
print(my_results)

####################

# 6
# У вас есть два списка my_list_1 и my_list_2 равной длины.
# Распечатать пары значений из my_list_1 и my_list_2 через обращение по индексу
# (можно range, можно enumerate).
# Например для списков [1, 3] и [2, 4]:
# (1, 2)
# (3, 4)
my_list_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
my_list_2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for index in range(len(my_list_1)):
    print((my_list_1[index], my_list_2[index]))

####################

# 7
# У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле и приведение типов.
my_string = "0123456789"
my_list = []
for symbol_1 in my_string:
    for symbol_2 in my_string:
        my_list.append(int(symbol_1 + symbol_2))
print(my_list)
