require_relative '../../../test.rb'
class ClickAutoAssignBtnTest < Test
    def test(driver, meta)
        page = SamplePage2.new(driver)
        page.clickAutoAssignBtn()
    end
end