require_relative '../../../test.rb'
class ClickTplFilterLanguageTest < Test
    def test(driver, meta)
        page = SamplePage2.new(driver)
        page.clickTplFilterLanguage()
    end
end