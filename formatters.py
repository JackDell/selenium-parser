from match import Match

def getFunctionFormatter(match):
    return {
            'sclick' : ['def click%s()\n' % match.getFormattedId(),
                        '    puts \'CLICKING %s\'\n' % match.getFormattedId(),
                        '    @driver.findById(\'%s\').click\n' % match.id,
                        'end'],
            'sinput' : ['def inputTo%s(content)\n' % match.getFormattedId(),
                        '    puts \'INPUTTING %%s TO %s\' %% content\n' % match.getFormattedId(),
                        '    @driver.findById(\'%s\').send_keys content\n' % match.id,
                        'end']
    }

def getTestCaseFormatter(match, parent):  
    return {
        'sclick' : ['require_relative \'../../../test.rb\'\n',
                    'class Click%sTest < Test\n' % match.getFormattedId(),
                    '    def test(driver, meta)\n',
                    '        page = %s.new(driver)\n' % parent,
                    '        page.click%s()\n' % match.getFormattedId(),
                    '    end\n',
                    'end'],
        'sinput' : ['require_relative \'../../../test.rb\'\n',
                    'class InputTo%sTest < Test\n' % match.getFormattedId(),
                    '    def initialize(content)\n',
                    '        @content = content\n',
                    '    end\n\n',
                    '    def test(driver, meta)\n',
                    '        page = %s.new(driver)\n' % parent,
                    '        page.inputTo%s(@content)\n' % match.getFormattedId(),
                    '    end\n',
                    'end']
    }

def getFileNameFormatter(match):
    return {
        'sclick' : 'click%sTest.rb' % match.getFormattedId(),
        'sinput' : 'input%sTest.rb' % match.getFormattedId()
    }

def getPageFormatter(parent):
    return {
        'header' : ['require_relative \'../../../component.rb\'\n',
                    'class %s < Component\n\n' % parent],
        'footer' : 'end'
    }