import re

from bs4 import BeautifulSoup
import requests

url = 'https://www.imot.bg/pcgi/imot.cgi?act=3&slink=8obds7&f1=1'
result = requests.get(url)


pattern = r'>(\d+ \d+) EUR<'

result2 = re.findall(pattern, result.text)

result_int = []
for num in result2:
    if ' ' in num:

        num = num.replace(' ','')
        result_int.append(int(num))

average_sum = sum(result_int) / len(result_int)
print(f'The average sum is: {average_sum:.2f} EUR')