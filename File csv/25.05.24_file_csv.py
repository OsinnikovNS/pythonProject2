import csv
name = []
name_visited = set()
name_want_to_visit = set()
next_city_to_visit = name_want_to_visit


def write_holiday_cities(first_letter):
    with open('travel-notes.csv', 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        for column in csv_reader:
            print(column)
            if first_letter.lower() in column[1][0].lower():
                for row in column[1].split(','):
                    name.append(row)
                for row in column[2].split(';'):
                    name_visited.add(row)
                for row in column[3].split(';'):
                    name_want_to_visit.add(row)

    with open(file='holiday.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(('Студенты:', sorted(name)))
        writer.writerow(('Посетили:', sorted(name_visited)))
        writer.writerow(('Хотят посетить: ', sorted(name_want_to_visit)))
        writer.writerow(('Никогда не были в: ', sorted(name_want_to_visit.difference(name_visited))))
        writer.writerow(('Следующим городом будет: ', sorted(name_want_to_visit.difference(name_visited))[0]))


write_holiday_cities(first_letter='R')
