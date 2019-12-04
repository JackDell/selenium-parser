import os

INSTRUCTIONS = ['sclick', 'sinput']
OUTPUT_FOLDER = 'output'
INDENT = ' ' * 4

def getOutputDirectory(component):
    directory = '%s\%s' % (OUTPUT_FOLDER, component.getFullName())
    if not os.path.exists(directory):
        os.mkdir(directory)
    return directory

def capitalize(string):
    return string[0].upper() + string[1:]