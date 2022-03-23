import requests
import csv
import datetime
from bs4 import BeautifulSoup
from itertools import chain
import sys
import os

url = 'https://www.chp.gov.hk/en/statistics/data/10/26/43/6994.html'
r = requests.get(str(sys.argv[1]))
soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find('table', border='1', style='border: 1px #cccccc;')

file_name = 'chp-' + str(datetime.datetime.today().date()) + '.csv'
curr_path = os.getcwd()
full_path = os.path.join(curr_path, file_name)
print(full_path)
csv_writer = csv.writer(open(file_name, 'w'))
header = []
data = []
row_data = []

for tab in table.find_all('tbody'):
    rows = tab.find_all('tr')
    for row in rows:
        th = row.find_all('th', class_=['dnstabletxt', 'dnstablewhitetitletxt', 'dnstabletitletxt'])
        td = row.find_all('td', class_=['dnstabletxt', 'dnstablewhitetitletxt','dnstabletitletxt'])
        header = [x.text for x in th]
        data = [x.text for x in td]
        if len(header) > 2:
            csv_writer.writerow(header)
        if len(header) <= 2:
            for i in range(len(header)):
                row_data = [[header[i]]]
        if row_data:
            row_data.append([x for x in data])
            file = csv_writer.writerow(list(chain.from_iterable(row_data)))
            with open(full_path, 'w') as f:
                f.write(str(file))



