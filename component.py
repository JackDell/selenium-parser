import os
from formatters import getComponentFormatter
from helper import getOutputDirectory, capitalize
from match import Match

class Component:
    def __init__(self, name, _type, matches):
        self.name = capitalize(name)
        self._type = capitalize(_type)
        self.matches = matches
        self.formatter = getComponentFormatter(self)

    def getFullName(self):
        return self.name + self._type

    def rubify(self):
        directory = getOutputDirectory(self)
        path = os.path.join(directory, '%s.rb' % self.getFullName())

        with open(path, 'w') as file:
            for line in self.formatter['header']:
                file.write(line)
            file.close()

        for match in self.matches:
            match.rubifyFunctions(self)
            match.rubifyTestCases(self)

        with open(path, 'a') as file:
            file.write(self.formatter['footer'])
            file.close()