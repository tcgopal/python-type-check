import json
import re

with open('excel.json') as file:
    excel_details = json.load(file)

final_resut = []

def process(operate_on, contraint, z, y):
    response = ''
    if contraint == 'Optional':
        print(y.replace(':', ','))

    if 'string' in operate_on or 'String' in operate_on:

        if 'Min' in operate_on or 'Max' in operate_on:
            num = operate_on.split('(')[-1].replace(')', '').strip()
            if 'Min' in operate_on:
                pattern = r'Min: (\d+)' 

                match = re.search(pattern, operate_on)
                if match:
                    number = int(match.group(1))
                    response += 'constr(' + 'min_length=' + str(number)  + ')' + num
            
        else:
            num = operate_on.split('(')[-1].replace(')', '').strip()
            response += 'constr(' + 'max_length=' + num + ')'
    
    if 'Number' in operate_on or 'NUMBER' in operate_on:
        response = 'int'
        num = operate_on.split('(')[-1].replace(')', '').strip()
        response += '[' + num + ']'

    result = ''
    if contraint == 'Optional':
        result = 'Optional[' + response + ']'
    
    else:
        result = response

    return result

r = []
rrrrrr = {}
for obj in  excel_details['Transaction']:
    temp = obj['Field Name']
    temp2 = obj['Data Type'] 
    resss = process(temp2, obj['Constraint'], obj['Column No.'], temp)
    rrrrrr[temp] =  ''
    r.append('{}: {}'.format(temp, resss))


json_object = json.dumps(rrrrrr, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)



