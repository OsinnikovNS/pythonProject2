import re

sample_html = ("<img src='https://example.com/image1.jpg'> "
               "<img src='http://example.com/image2.png'> <im "
               "src='https://example.com/image3.gif'>")


def extract_image_links(text):
    pattern = r'([^\']+(?:png|jpg|gif))'
    text = re.finditer(pattern, sample_html)
    for matched in text:
        print(f'{matched.group()}')


image_links = extract_image_links(sample_html)
