import csv

answers=[

   {'key':'привет','value':"и тебе привет"},

   {'key':'как дела?','value':"лучше всех"},

   {'key':'пока','value':"увидимся"}

]

with open('export.csv', 'w', encoding = 'utf-8') as f:
    fields = ['key', 'value']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for elem in answers:
        writer.writerow(elem)