years = input().split()         # читаем года как строки, разделённые пробелами
limit = int(input())            # читаем число, с которым сравниваем
years = list(map(int, years))

for y in years:
    year = int(y)               # переводим каждый год в число
    if year > limit:            # проверяем условие
        print(year)
    