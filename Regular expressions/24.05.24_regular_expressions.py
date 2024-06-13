import re

sample_html = ("<img src='https://example.com/image1.jpg'> "
               "<img src='http://example.com/image2.png'> "
               "<img src='https://example.com/image3.gif'>")


def extract_image_links(text):
    pattern = r'([^\']+(?:png|jpg|jpeg|gif))'
    text = re.finditer(pattern, sample_html)

    if text:
        for matched in text:
            print(f'{matched.group()}')
    else:
        print("Нет ссылок с картинками в HTML тексте.")


image_links = extract_image_links(sample_html)
