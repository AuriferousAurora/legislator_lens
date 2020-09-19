import json
import os
import requests

update_data = False
data_dir = os.curdir # may change if I decide to move the data out of parent dir
file_name = 'legislators-current'

if update_data:
    yr = requests.get('https://github.com/unitedstates/congress-legislators/blob/master/legislators-current.yaml')
    yr.raise_for_status()

    with open('legislators-current.yaml', 'w', encoding='utf-8') as file:
        file.write(yr.text)

    jr = requests.get('https://theunitedstates.io/congress-legislators/legislators-current.json')
    jr.raise_for_status()

    with open('legislators-current.json', 'w', encoding='utf-8') as file:
        file.write(jr.text)

pathname = os.path.join(data_dir, file_name + '.json')
json_list = None

with open(pathname, 'r') as file:
    try:
        json_list = json.load(file) # returns a list
    except Error:
        print(str(Error))

if json_list:
    class Legislator():
        def __init__(self, index):
            name = json_list[index].get('name')
            self.first_name = name['first']
            self.last_name = name['last']
            self.full_name = self.first_name + ' ' + self.last_name

            latest_pos_index = len(json_list[index].get('terms')) - 1
            latest_term = json_list[index].get('terms')[latest_pos_index]
            self.type = latest_term['type']
            self.term_start_date = latest_term['start']
            self.term_end_date = latest_term['end']
            
    
    first_ten_legislators = []
    count = 0
    while count < 10:
        l = Legislator(count)
        first_ten_legislators.append(l)
        count = count + 1
    
    for legislator in first_ten_legislators:
        print(legislator.full_name)
        print(type(legislator))
        








