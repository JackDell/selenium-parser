require_relative '../../../test.rb'
class InputToUsernameTest < Test
    def initialize(content)
        @content = content
    end

    def test(driver, meta)
        page = SamplePage.new(driver)
        page.inputToUsername(@content)
    end
end