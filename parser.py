import os
from match import Match
from formatters import *
from bs4 import BeautifulSoup

INSTRUCTIONS = ['sclick', 'sinput']

# Takes a document of type .html and breaks it into individual lines
# each line is added to a list as a string and then the list is returned
def getHtmlAsLines(html_doc):
    soup = BeautifulSoup(open(html_doc, 'r'), 'html.parser')
    pretty = soup.prettify()
    return pretty.split('\n')

# Creates returns a list of match objects
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

def getFunctions(match):
    formatter = getFunctionFormatter(match)
    templates = []

    for instruction in match.instructions:
        templates.append(formatter[instruction])
    return templates

def getOutputDirectory(parent):
    directory = 'output/%s' % parent
    if not os.path.exists(directory):
        os.mkdir(directory)
    return directory

def createPage(matches, parent):
    page_formatter = getPageFormatter(parent)
    directory = getOutputDirectory(parent)
    new_page_path = os.path.join(directory, '%s.rb' % parent)
    page = open(new_page_path, 'w')
    indent = ' ' * 4

    for line in page_formatter['header']:
        page.write(line)

    for match in matches:
        for func in getFunctions(match):
            for line in func:
                page.write(indent + line)
            page.write('\n\n')

    page.write(page_formatter['footer'])
    page.close()

def createTestCases(matches, parent):
    for match in matches:
        createTestCase(match, parent)

def createTestCase(match, parent):
    test_case_formatter = getTestCaseFormatter(match, parent)
    file_name_formatter = getFileNameFormatter(match)
    directory = getOutputDirectory(parent)

    for instruction in match.instructions:
        test_case = test_case_formatter[instruction]
        file_name = file_name_formatter[instruction]
        new_file_path = os.path.join(directory, file_name)

        with open(new_file_path, 'w') as file:
            for line in test_case:
                file.write(line)
            file.close()

def processMatches(matches):
    parent = "SamplePage2"
    createPage(matches, parent)
    createTestCases(matches, parent)


processMatches(getMatches('example2.html'))