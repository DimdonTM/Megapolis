f = open("game.txt") # Читаем файл
d = [[i for i in s.split("$")] for s in f.readlines()] # Сортируем данные
c = [] # переменная для хранения данных
for i in range(len(d)):
    c.append(d[i][0]) # вставляем в массив все строки с названиями игр
v = [i for i in set(c)] # получаем названия игр
for i in range(len(v)):
    print(f"{v[i]} - количество багов: {c.count(v[i])}") # выводим название игры и количество багов