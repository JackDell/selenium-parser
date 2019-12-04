# Class used to represent a match to a parser-keyword
# id = the full id name: 'Save-btn-sclick'
# tag = the html tag the id is applied to: input, button, a, ...
# instructions = a list of parser keyword pulled from the id: ['sclick']
class Match:
    def __init__(self, id, tag, instructions):
        self.id = id
        self.tag = tag
        self.instructions = instructions
    
    # Returns formatted version of the id in which
    # all hypens and parser-keywords are removed.
    # The remaining terms are capitalized and returned
    # 'add-account-btn-sclick' -> 'AddAccountBtn'
    def getFormattedId(self):
        formatted_id = self.id
        for instruction in self.instructions:
            formatted_id = formatted_id.replace('-' + instruction, '')
            if '-' in formatted_id:
                temp = ''
                names = formatted_id.split('-')
                for name in names:
                    temp += name.capitalize()
                formatted_id = temp
            else:
                formatted_id = formatted_id.capitalize()
        return formatted_id