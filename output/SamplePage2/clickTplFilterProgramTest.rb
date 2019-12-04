require_relative '../../../test.rb'
class ClickTplFilterProgramTest < Test
    def test(driver, meta)
        page = SamplePage2.new(driver)
        page.clickTplFilterProgram()
    end
end