import numpy as np
import pandas as pd

contacts = pd.read_csv('../../data/csv_to_vcard/Contacts.csv', header=0)
filtered = contacts[contacts['Category'] == 'Agents'].fillna('')

vcards = []

for index, row in filtered[['First', 'Last', 'Company', 'Email', 'Other']].iterrows():
	vcards.append('BEGIN:VCARD')
	vcards.append('VERSION:3.0')
	vcards.append('N:{};{}'.format(row['Last'], row['First']))
	vcards.append('FN:{} {}'.format(row['First'], row['Last']))
	vcards.append('ORG:{}'.format(row['Company']))
	vcards.append('EMAIL;type=INTERNET;type=WORK;type=pref:{}'.format(row['Email']))
	if row['Other'] != '':
		vcards.append('TEL;type=WORK;type=VOICE;type=pref:{}'.format(row['Other']))
	vcards.append('END:VCARD')
	vcards.append('')

with open('../../data/csv_to_vcard/Contacts.vcf', 'w') as file:
    file.writelines('{}\n'.format(vcard) for vcard in vcards)
