from pyexcel import get_records

# records = iget_records(file_name='example.xls', encoding='ISO-8859-1')
# char_to_polish = {
#     '¹': 'ą',
#     '13': 'Ą',
#     'æ': 'ć',
#     '15': 'Ć',
#     'ê': 'ę',
#     '1': 'Ę',
#     '³': 'ł',
#     '3': 'Ł',
#     '4': 'ń',
#     '5': 'Ń',
#     'ó': 'ó',
#     '7': 'Ó',
#     'œ': 'ś',
#     'Œ': 'Ś',
#     '¿': 'ż',
#     '0': 'Ż',
#     '11': 'ź',
#     '12': 'Ź'
# }
# next(records)
# for record in records:
#     print(record)
    # for key in record:
    #     print(f'{key} : {record[key]}')

records = get_records(file_name='example1.xlsx', encoding='utf-8')

for record in records:
    print(record)
