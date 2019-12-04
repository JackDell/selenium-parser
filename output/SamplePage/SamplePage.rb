require_relative '../../../component.rb'
class SamplePage < Component

    def inputToUsername(content)
        puts 'INPUTTING %s TO Username' % content
        @driver.findById('username-sinput').send_keys content
    end

    def clickSavebtn()
        puts 'CLICKING Savebtn'
        @driver.findById('saveBtn-sclick').click
    end

    def clickAlink()
        puts 'CLICKING Alink'
        @driver.findById('aLink-sclick').click
    end

end