require_relative '../../../test.rb'
class ClickSavebtnTest < Test
    def test(driver, meta)
        page = SamplePage.new(driver)
        page.clickSavebtn()
    end
end