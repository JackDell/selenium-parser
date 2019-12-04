require_relative '../../../test.rb'
class ClickTplFilterLocationTest < Test
    def test(driver, meta)
        page = SamplePage2.new(driver)
        page.clickTplFilterLocation()
    end
end