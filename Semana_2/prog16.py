# coding=utf-8

#Analisando nomes de um arquivo csv para uma lista HTML

import csv

html_output = ''
names = []

with open('e-mails.csv', 'r') as csv_reader:
    csv_reader = csv.DictReader(csv_reader)

    for line in csv_reader:
        names.append('{} {}'.format(line['Name'], line['Last_Name']))


html_output += '<p>There are currently {} names in the e-mail list.</p>'.format(len(names))
html_output += '\n<ul>'
for name in names:
    html_output += '\n\t<li>{}</li>'.format(name)
html_output += '\n</ul>'

print(html_output)
