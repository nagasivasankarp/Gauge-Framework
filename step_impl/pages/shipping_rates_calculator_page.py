from selenium.webdriver.common.by import By
from utilities.base_ui import BaseUI


class ShippingRatesCalculatorPageLocators:

    PICKUP_PINCODE_FIELD = (By.CSS_SELECTOR, '#pickup_postcode')
    DELIVERY_PINCODE_FIELD = (By.CSS_SELECTOR, '#delivery_postcode')
    WEIGHT_FIELD = (By.NAME, 'weight')
    DIMENSIONS_LENGTH_FIELD = (By.NAME, 'length')
    DIMENSIONS_BREADTH_FIELD = (By.NAME, 'breadth')
    DIMENSIONS_HEIGHT_FIELD = (By.NAME, 'height')
    DECLARED_VALUE_FIELD = (By.NAME, 'declared_value')
    CALCULATE_BUTTON = (By.CSS_SELECTOR, "div.row.mb.mt.clearfix > div > button")
    COURIER_TYPE_AIR = (By.CSS_SELECTOR,
                        "div.bg-gray-lighter.p > div:nth-child(2) > h5 > strong")
    COURIER_TYPE_SURFACE = (By.CSS_SELECTOR,
                            "div.bg-gray-lighter.p > div:nth-child(3) > h5 > strong")
    AIR_COURIER_LIST = (By.XPATH,
                        "//div[@id='panel_rate']/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div[1]/div/table/tbody/tr")
    SURFACE_COURIER_LIST = (By.XPATH,
                            "//div[@id='panel_rate']/div/div/div/div[1]/div/div[1]/div[1]/div/div[2]/div[2]/div/table/tbody/tr")


class ShippingRatesCalculatorPage(BaseUI):
    URL = '{}rate-calculatorabc?id=page_rate_calc#page_rate_calc'.format(BaseUI.BASE_UI_URL)

    # Method for Fill the PickUp Pincode Field
    def fill_pickup_pincode_field(self, input_value):
        return self.set(
            ShippingRatesCalculatorPageLocators.PICKUP_PINCODE_FIELD,
            input_value
        )

    # Method for Fill the Deliver Pincode Field
    def fill_delivery_pincode_field(self, input_value):
        return self.set(
            ShippingRatesCalculatorPageLocators.DELIVERY_PINCODE_FIELD,
            input_value
        )

    # Method for Fill the Weight Field
    def fill_weight_field(self, input_value):
        return self.set(
            ShippingRatesCalculatorPageLocators.WEIGHT_FIELD, input_value
        )

    # Method for Fill the Length Field
    def fill_dimensions_length_field(self, input_value):
        return self.set(
            ShippingRatesCalculatorPageLocators.DIMENSIONS_LENGTH_FIELD,
            input_value
        )

    # Method for Fill the Breadth Field
    def fill_dimensions_breadth_field(self, input_value):
        return self.set(
            ShippingRatesCalculatorPageLocators.DIMENSIONS_BREADTH_FIELD,
            input_value
        )

    # Method for Fill the Height Field
    def fill_dimensions_height_field(self, input_value):
        return self.set(
            ShippingRatesCalculatorPageLocators.DIMENSIONS_HEIGHT_FIELD,
            input_value
        )

    # Method for Fill the Declared Value Field
    def fill_declared_value_field(self, input_value):
        return self.set(
            ShippingRatesCalculatorPageLocators.DECLARED_VALUE_FIELD,
            input_value
        )

    # Method for click on Calculate button
    def click_calculate_button(self):
        self.click(ShippingRatesCalculatorPageLocators.CALCULATE_BUTTON)

    # Method for Get the Courier Type(Air) Text
    def get_courier_type_air(self):
        return self.get(ShippingRatesCalculatorPageLocators.COURIER_TYPE_AIR)

    # Method for Get the Courier Type(Surface ) Text
    def get_courier_type_surface(self):
        return self.get(
            ShippingRatesCalculatorPageLocators.COURIER_TYPE_SURFACE
        )

    # Method for Get the Courier Details(Air ) Text
    def get_air_courier_provider_list(self):
        return self.get_table_data(
            ShippingRatesCalculatorPageLocators.AIR_COURIER_LIST
        )

    # Method for Get the Courier Details(Surface ) Text
    def get_air_courier_rate_list(self):
        return self.get_table_data(
            ShippingRatesCalculatorPageLocators.SURFACE_COURIER_LIST
        )

    # Method for Navigate to URL
    def visit(self):
        self.custom_wait()
        self.driver.get(self.URL)
