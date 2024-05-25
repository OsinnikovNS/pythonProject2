import json


def format(register):
    standard_lower = ['firstname', 'lastname', 'department', 'salary']
    standard = ['firstName', 'lastName', 'department', 'salary']
    for i in range(0, len(standard)):
        if register.lower() == standard_lower[i].lower():
            return standard[i]


def employees_rewrite(sort_type):
    try:
        res = format(sort_type)
        with open(file='employees.json', mode='r') as json_file:
            json_data = json.load(json_file)
            if res == 'salary':
                sort = sorted(json_data['employees'], key=lambda employee: employee[res], reverse=True)
            else:
                sort = sorted(json_data['employees'], key=lambda employee: employee[res])

        with open(file=f'my_employees_{sort_type}_sorted.json', mode='w') as file:
            json.dump(sort, file, indent=4)
    except:
        print('ValueError("Bad key for sorting")')


employees_rewrite('firstNAME')
employees_rewrite('lastNAME')
employees_rewrite('department')
employees_rewrite('salary')
