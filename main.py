import csv

import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern = r'(\+7|8)(\s*)(\(?)(\d{3})(\)?)(\s*)' \
              r'(\-*)(\d{3})(\-*)(\d{2})(\-*)' \
              r'(\d{2})(\s*)(\(?)(доб)?(\.?)(\s*)(\d+)?(\)*)'

pattern_new = r'+7(\4)\8-\10-\12\13\15\16\18'

contacts_list_new = list()
for contacts in contacts_list:
    contact = ','.join(contacts)
    format_contact = re.sub(pattern, pattern_new, contact)
    contact_list = format_contact.split(',')
    contacts_list_new.append(contact_list)

pattern = r'^([а-яёА-ЯЁ]+)(\,?)(\s*)([а-яёА-ЯЁ]+)' \
               r'(\,?)(\s*)([а-яёА-ЯЁ]*)(\,?)(\,?)(\,?)'

pattern_new = r'\1\2\10\4\5\9\7\8'

contacts_list = list()
for contacts in contacts_list_new:
    print(contacts)
    contact = ','.join(contacts)
    format_contact = re.sub(pattern, pattern_new, contact)
    contact_list = format_contact.split(',')
    if contact_list not in contacts_list:
        contacts_list.append(contact_list)

for i in contacts_list:
    for j in contacts_list:
        if i[0] == j[0] and i[1] == j[1] and i != j:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]

contact_list = list()
for page in contacts_list:
    if page not in contact_list:
        contact_list.append(page)

with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contact_list)
