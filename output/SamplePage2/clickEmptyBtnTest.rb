require_relative '../../../test.rb'
class ClickEmptyBtnTest < Test
    def test(driver, meta)
        page = SamplePage2.new(driver)
        page.clickEmptyBtn()
    end
end