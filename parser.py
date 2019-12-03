import os
from bs4 import BeautifulSoup

INSTRUCTIONS = ['sclick', 'sinput']

class Match:
    def __init__(self, id, tag, instructions):
        self.id = id
        self.tag = tag
        self.instructions = instructions
    
    def getStrippedId(self):
        stripped_id = self.id
        for instruction in self.instructions:
            stripped_id = stripped_id.replace('-' + instruction, '')
            if '-' in stripped_id:
                temp = ''
                names = stripped_id.split('-')
                for name in names:
                    temp += name.capitalize()
                stripped_id = temp
            else:
                stripped_id.capitalize()
        return stripped_id
    


def getHtmlAsLines(html_doc):
    soup = BeautifulSoup(open(html_doc, 'r'), 'html.parser')
    pretty = soup.prettify()
    return pretty.split('\n')

def getMatches(html_doc):
    matches = []
    for line in getHtmlAsLines(html_doc):
        if ('id=' not in line) and ('id =' not in line):
            continue
        
        before, value = line.split('id')
        _, value, _ = value.split('"', 2)

        instructions = getInstructions(value)
        if instructions == []:
            continue

        _, tag = before.split('<', 1)
        tag, _ = tag.split(' ', 1)
        tag = tag.replace(' ', '')
            
        matches.append(Match(value, tag, instructions))    
    return matches

def getInstructions(id):
    found = []
    for instruction in INSTRUCTIONS:
        if instruction in id:
            found.append(instruction)
    return found

def getTemplates(match):
    formatter = {
        'sclick' : ['def click%s()\n' % match.getStrippedId(),
                    '\tputs \'CLICKING %s\'\n' % match.getStrippedId(),
                    '\t@driver.findById(\'%s\').click\n' % match.id,
                    'end'],
        'sinput' : ['def inputTo%s(content)\n' % match.getStrippedId(),
                    '\tputs \'INPUTTING %%s TO %s\' %% content\n' % match.getStrippedId(),
                    '\t@driver.findById(\'%s\').send_keys content\n' % match.id,
                    'end']
    }

    templates = []
    for instruction in match.instructions:
        templates.append(formatter[instruction])
    return templates

def processMatches(matches):
    raw_data = []
    for match in matches:
        raw_data.append(getTemplates(match))
    
    new_file_path = os.path.join('output', 'test.rb')

    with open(new_file_path, 'w') as newFile:
        for data in raw_data:
            for func in data:
                for line in func:
                    newFile.write(line)
                newFile.write('\n\n')
        newFile.close()

processMatches(getMatches('example2.html'))