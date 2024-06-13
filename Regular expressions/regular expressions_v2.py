import re


class RegularExpressions:
    def extract_image_links(self, matched):
        image_links = r'\w{4,5}\W{3}\w{7}.\w{3}.\w{5}\d.(?:jpg|jpeg|gif|png)'
        html_text = ("<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'>"
                     " <img src='https://example.com/image3.gif'>")

        matched = re.search(image_links, html_text)
        searching_iterator = re.finditer(image_links, html_text)
        for matched in searching_iterator:
            print(f'Следующее совпадение: {matched.group()}')


regex = RegularExpressions()    # Создаем экземпляр класса
regex.extract_image_links('matched')    # Вызываем метод и выводим результат
