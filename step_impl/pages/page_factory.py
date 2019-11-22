from getgauge.python import before_suite, after_suite
from utilities.base_ui import BaseUI
from step_impl.pages.login_page import LoginPage
from step_impl.pages.create_quick_shipment_page import CreateQuickShipmentPage
from step_impl.pages.shipping_rates_calculator_page import ShippingRatesCalculatorPage
from step_impl.pages.new_order_page import NewOrderPage


class PageFactory:
    global browser_type, base_ui
    driver = None
    login_page = None
    create_quick_shipment_page = None
    shipping_rates_calculator_page = None
    new_order_page = None
    base_ui = BaseUI(driver)


# Method for load all the pages
@before_suite
def setup():
    # PageFactory.driver = base_ui.launch_browser_instance(browser_type='chrome')

    PageFactory.login_page = LoginPage(PageFactory.driver)
    PageFactory.create_quick_shipment_page = CreateQuickShipmentPage(PageFactory.driver)
    PageFactory.shipping_rates_calculator_page = ShippingRatesCalculatorPage(PageFactory.driver)
    PageFactory.new_order_page = NewOrderPage(PageFactory.driver)


# Method for quit from browser instance
@after_suite
def tear_down():
    print("page factory")
    # PageFactory.driver.quit()
