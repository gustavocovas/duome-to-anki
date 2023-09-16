from lxml import html
import sys

html_file_path = sys.argv[1]

with open(html_file_path, "rb") as file:
    html_content = file.read()

print("word;translation")

parsed_html = html.fromstring(html_content)

ul_element = parsed_html.find(".//ul[@class='plain list']")

if ul_element is not None:
    list_items = ul_element.xpath(".//li/span[@class='wA']")
    for item in list_items:
        title_attr = item.xpath("@title")[0]
        parts = title_attr.split("]")

        word = item.text_content().strip()
        translation = parts[1]

        print(f"{word};{translation}")
