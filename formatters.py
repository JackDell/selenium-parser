def getFunctionFormatter(match):
    return {
            'sclick' : ['def click%s()\n' % match.getFormattedId(),
                        '    puts \'CLICKING %s\'\n' % match.getFormattedId(),
                        '    @driver.findById(\'%s\').click\n' % match._id,
                        'end'],
            'sinput' : ['def inputTo%s(content)\n' % match.getFormattedId(),
                        '    puts \'INPUTTING %%s TO %s\' %% content\n' % match.getFormattedId(),
                        '    @driver.findById(\'%s\').send_keys content\n' % match._id,
                        'end']
    }

def getFileNameFormatter(match):
    return {
        'sclick' : 'click%sTest.rb' % match.getFormattedId(),
        'sinput' : 'input%sTest.rb' % match.getFormattedId()
    }

def getComponentFormatter(component):
    return {
        'header' : ['require_relative \'../../../component.rb\'\n',
                    'class %s < Component\n' % component.getFullName()],
        'footer' : 'end'
    }

def getTestCaseFormatter(match, component):
    return {
        'sclick' : ['require_relative \'../../../test.rb\'\n',
                    'class Click%sTest < Test\n' % match.getFormattedId(),
                    '    def test(driver, meta)\n',
                    '        %s = %s.new(driver)\n' % (component._type.lower(), component.getFullName()),
                    '        %s.click%s()\n' % (component._type.lower(), match.getFormattedId()),
                    '    end\n',
                    'end'],
        'sinput' : ['require_relative \'../../../test.rb\'\n',
                    'class InputTo%sTest < Test\n' % match.getFormattedId(),
                    '    def initialize(content)\n',
                    '        @content = content\n',
                    '    end\n\n',
                    '    def test(driver, meta)\n',
                    '        %s = %s.new(driver)\n' % (component._type.lower(), component.getFullName()),
                    '        %s.inputTo%s(@content)\n' % (component._type.lower(), match.getFormattedId()),
                    '    end\n',
                    'end']
    }