import os
import csv


class PriceMachine:

    def __init__(self):
        self.data = []

    def load_prices(self, directory):
        key_mapping = {
            'название': ['название', 'продукт', 'товар', 'наименование'],
            'цена': ['цена', 'розница'],
            'вес': ['фасовка', 'масса', 'вес']
        }

        for file in os.listdir(directory):
            if file.endswith('.csv') and 'price' in file.lower():
                with open(os.path.join(directory, file), 'r', encoding='utf-8') as csv_file:
                    csv_reader = csv.DictReader(csv_file, delimiter=',')
                    for row in csv_reader:
                        data = {'файл': file}
                        for key, possible_keys in key_mapping.items():
                            for key_possible in possible_keys:
                                if key_possible in row:
                                    data[key] = row[key_possible]
                                    break
                        self.data.append(data)

    def search_product(self, search):
        res = [product for product in self.data if search.lower() in product.get('название', '').lower()]
        results_sorted = sorted(res, key=lambda x: float(x.get('цена')) / float(x.get('вес')))
        return results_sorted

    # вывод в html:
    def export_to_html(self, output_file_path=r'C:\Темп\Price_scan\output.html'):
        if self.data:
            sorted_data = sorted(self.data, key=lambda x: float(x.get('цена')) / float(x.get('вес')))
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write('''
                <!DOCTYPE html>
                <html lang='ru'>
                <head>
                    <meta charset='UTF-8'>
                    <title>Позиции продуктов</title>
                </head>
                <body>
                    <table>
                        <tr>
                            <th>№</th>
                            <th>Наименование</th>
                            <th>Цена</th>
                            <th>Вес</th>
                            <th>Файл</th>
                            <th>Цена за кг.</th>
                        </tr>
                ''')
                for idx, row in enumerate(sorted_data, start=1):
                    price_per_kg = float(row.get('цена')) / float(row.get('вес'))
                    file.write(
                        f"<tr><td>{idx}</td>"
                        f"<td>{row.get('название', '')}</td>"
                        f"<td>{row.get('цена', '')}</td>"
                        f"<td>{row.get('вес', '')}</td>"
                        f"<td>{row.get('файл', '')}</td>"
                        f"<td>{price_per_kg:.2f}</td></tr>"
                    )
                file.write('''
                    </table>
                </body>
                </html>
                ''')
            print(f"HTML файл успешно создан: {output_file_path}")
        else:
            print("Нет данных для экспорта в HTML файл.")


pm = PriceMachine()
pm.load_prices(r'C:\Темп\Price_scan')

try:
    while True:
        search_query = input("Введите фрагмент названия товара для поиска (или 'exit' для выхода): \n")
        if search_query.lower() == 'exit':
            pm.export_to_html()
            print("Работа завершена.")
            break

        results = pm.search_product(search_query)

        if results:
            print(f'По запросу "{search_query}" найдено:')
            sorted_results = sorted(results, key=lambda x: float(x.get('цена')) / float(x.get('вес')))

            for n, result in enumerate(sorted_results, 1):
                print(
                    f"{n}. Название: {result.get('название')}, Цена: {result.get('цена')}, Вес: {result.get('вес')}, "
                    f"Файл: {result.get('файл')}, "
                    f"Цена за кг: {round(float(result.get('цена')) / float(result.get('вес')), 2)}")
        else:
            print(f'По запросу "{search_query}" ни чего не найдено')
except Exception as e:
    print(f"Произошла ошибка: {e}")
