import xml.etree.cElementTree as ET

try:
    tree = ET.parse('homework.xml')
    root = tree.getroot()
    for item in root.findall('subject'):
        if item.find('name').text == 'Math':
            print('Total point from Math is', item.find('totalpoint').text)
except:
    print('Something went wrong')
finally:
    print('XML')


import json

try:
    with open('jsonhome.json') as f:
        data = json.load(f)
        exams = data['Exams']
        subject = exams['Subject']

        for item in subject:
            if item['name'] == 'Math':
                print('Total point from Math is', item['totalpoint'])
except:
    print('Something went wrong')
finally:
    print('JSON')
