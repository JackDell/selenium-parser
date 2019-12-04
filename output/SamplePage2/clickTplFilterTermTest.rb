require_relative '../../../test.rb'
class ClickTplFilterTermTest < Test
    def test(driver, meta)
        page = SamplePage2.new(driver)
        page.clickTplFilterTerm()
    end
end