import os
from helper import getOutputDirectory, capitalize, INDENT, INSTRUCTIONS
from formatters import getFunctionFormatter, getTestCaseFormatter, getFileNameFormatter

# Class used to represent a match to a parser-keyword
# id = the full id name: 'Save-btn-sclick'
# tag = the html tag the id is applied to: input, button, a, ...
# instructions = a list of parser keyword pulled from the id: ['sclick']
class Match:
    def __init__(self, _id, tag):
        self._id = _id
        self.tag = tag
        self.instructions = self.getInstructions()
        self.function_formatter = getFunctionFormatter(self)
        self.file_name_formatter = getFileNameFormatter(self)
    
    # Returns formatted version of the id in which
    # all hypens and parser-keywords are removed.
    # The remaining terms are capitalized and returned
    # 'add-account-btn-sclick' -> 'AddAccountBtn'
    def getFormattedId(self):
        formatted_id = self._id
        for instruction in self.instructions:
            formatted_id = formatted_id.replace('-' + instruction, '')
            if '-' in formatted_id:
                temp = ''
                names = formatted_id.split('-')
                for name in names:
                    temp += capitalize(name)
                formatted_id = temp
            else:
                formatted_id = capitalize(formatted_id)
        return formatted_id
    
    def rubifyFunctions(self, component):
        directory = getOutputDirectory(component)
        path = os.path.join(directory, '%s.rb' % component.getFullName())
        with open(path, 'a') as file:
            for i in range(len(self.instructions)):
                func = self.function_formatter[self.instructions[i]]
                for line in func:
                    file.write(INDENT + line)
                file.write('\n\n')
            file.close()

    def rubifyTestCases(self, component):
        test_case_formatter = getTestCaseFormatter(self, component)

        directory = getOutputDirectory(component)
        for instruction in self.instructions:
            test_case = test_case_formatter[instruction]
            file_name = self.file_name_formatter[instruction]
            new_file_path = os.path.join(directory, file_name)

            with open(new_file_path, 'w') as file:
                for line in test_case:
                    file.write(line)
                file.close()

    def getInstructions(self):
        instructions = []
        for instruction in INSTRUCTIONS:
            if instruction in self._id:
                instructions.append(instruction)
        return instructions

