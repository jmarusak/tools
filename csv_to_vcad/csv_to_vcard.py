import numpy as np
import pandas as pd
from datetime import datetime

contacts = pd.read_csv('../../data/csv_to_vcard/contacts.csv', header=0)
filtered = contacts[contacts['Job title'] == 'Agent'].fillna('')

prefix = 'Z'

vcards = []

for index, row in filtered[['Name', 'Employer', 'Email 1', 'Phone 1']].iterrows():
	first_last_name = row['Name'].split(' ')

	vcards.append('BEGIN:VCARD')
	vcards.append('VERSION:3.0')
	vcards.append('N:{};{} {}'.format(first_last_name[1], prefix, first_last_name[0]))
	vcards.append('FN:{} {}'.format(prefix, row['Name']))
	if row['Employer'] != '':
		vcards.append('ORG:{}'.format(row['Employer']))
	vcards.append('EMAIL;type=INTERNET;type=WORK;type=pref:{}'.format(row['Email 1']))
	if row['Phone 1'] != '':
		vcards.append('TEL;type=MOBILE;type=VOICE;type=pref:{}'.format(row['Phone 1']))
	vcards.append('END:VCARD')
	vcards.append('')

for vcard in vcards:
	print(vcard)

now = datetime.now()
timestamp = now.strftime("%Y%d%m%H%M")

with open('../../data/csv_to_vcard/contacts_{}.vcf'.format(timestamp), 'w') as file:
    file.writelines('{}\n'.format(vcard) for vcard in vcards)
