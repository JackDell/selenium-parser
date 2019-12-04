require_relative '../../../test.rb'
class ClickAlinkTest < Test
    def test(driver, meta)
        page = SamplePage.new(driver)
        page.clickAlink()
    end
end