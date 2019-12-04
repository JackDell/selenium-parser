import os
from formatters import *
from helper import getOutputDirectory, INDENT, INSTRUCTIONS
from match import Match
from component import Component
from bs4 import BeautifulSoup

# Takes a document of type .html and breaks it into individual lines
# each line is added to a list as a string and then the list is returned
def getHtmlAsLines(html_doc):
    soup = BeautifulSoup(open(html_doc, 'r'), 'html.parser')
    pretty = soup.prettify()
    return pretty.split('\n')

# Creates returns a list of match objects
def getMatches(html_lines):
    matches = []
    for line in html_lines:
        if ('id=' not in line) and ('id =' not in line):
            continue
        
        before, value = line.split('id')
        _, value, _ = value.split('"', 2)
        _, tag = before.split('<', 1)
        tag, _ = tag.split(' ', 1)
        tag = tag.replace(' ', '')
            
        match = Match(value, tag)

        if match.instructions != []:
            matches.append(match)
    return matches

def strip_keywords(file_name, component):
    lines = getHtmlAsLines(file_name)
    new_lines = []
    first = True
    for line in lines:
        if first:
            first = False
            continue

        for instruction in INSTRUCTIONS:
            line = line.replace('-' + instruction, '')
    
        before, after = line.split('<', 1)
        before = before.replace(' ', '  ')
        new_lines.append(before + '<' + after)

        directory = getOutputDirectory(component)
        path = os.path.join(directory, file_name)

        with open(path, 'w') as file:
            for line in new_lines:
                file.write(line + '\n')
            file.close()

def getComponentInfo(lines):
    _, name, _, component_type, _  = lines[0].split('"')
    return name, component_type

def main():
    file_name = 'example.html'
    lines = getHtmlAsLines(file_name)
    matches = getMatches(lines)
    name, component_type = getComponentInfo(lines)
    component = Component(name, component_type, matches)
    component.rubify()
    strip_keywords(file_name, component)

main()