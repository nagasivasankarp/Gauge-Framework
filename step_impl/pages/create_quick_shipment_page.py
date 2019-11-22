from selenium.webdriver.common.by import By
from utilities.base_ui import BaseUI


class CreateQuickShipmentPageLocators:
    DELIVER_TO_PINCODE_FIELD = (By.CSS_SELECTOR, '#shipping_pincode')
    PRODUCT_NAME_FIELD = (By.CSS_SELECTOR, '#name')
    QUANTITY_UNITS_FIELD = (By.CSS_SELECTOR, '#units')
    UNIT_PRICE_FIELD = (By.NAME, 'selling_price_0')
    WEIGHT_FIELD = (By.NAME, 'weight')
    DIMENSIONS_LENGTH_FIELD = (By.NAME, 'length')
    DIMENSIONS_BREADTH_FIELD = (By.NAME, 'breadth')
    DIMENSIONS_HEIGHT_FIELD = (By.NAME, 'height')
    SEARCH_COURIER_BUTTON = (By.CSS_SELECTOR, "input[type='submit']")
    ALERT_MESSAGE_NO_COURIERS = (By.XPATH,
                                 "//div[@class='uk-notify uk-notify-top-center']/div/div")
    ALERT_CANCEL_NO_COURIERS = (By.XPATH,
                                "//div[@class='uk-notify uk-notify-top-center']/div/a")
    BACK_TO_CREATE_SHIPMENT_BUTTON = (By.CSS_SELECTOR, "span.text-primary > span")
    COURIER_RATED_LIST = (By.CSS_SELECTOR, '#recommended_val')
    PICKUP_FROM_DETAILS = (By.CSS_SELECTOR, "div.row > div > div:nth-child(1")
    PAYMENT_TYPE = (By.CSS_SELECTOR, "div.row > div > div:nth-child(2)")
    DELIVER_TO_DETAILS = (By.CSS_SELECTOR, "div.row > div > div:nth-child(3)")


class CreateQuickShipmentPage(BaseUI):
    URL = '{}quick-ship'.format(BaseUI.BASE_UI_URL)

    # Method for Fill Deliver TO Field
    def fill_deliver_to_field(self, deliver_pincode):
        self.set(CreateQuickShipmentPageLocators.DELIVER_TO_PINCODE_FIELD, deliver_pincode)

    # Method for Fill Product Name Field
    def fill_product_name_field(self, product_name):
        self.set(
            CreateQuickShipmentPageLocators.PRODUCT_NAME_FIELD, product_name
        )

    # Method for Fill Quantity Field
    def fill_quantity_field(self, quantity_units):
        self.set(
            CreateQuickShipmentPageLocators.QUANTITY_UNITS_FIELD, quantity_units
        )

    # Method for Fill Weight Field
    def fill_weight_field(self, weight):
        self.set(CreateQuickShipmentPageLocators.WEIGHT_FIELD, weight)

    # Method for Fill Unit Price Field
    def fill_unit_price_field(self, unit_price):
        self.set(CreateQuickShipmentPageLocators.UNIT_PRICE_FIELD, unit_price)

    # Method for Fill Length Field
    def fill_length_field(self, length):
        self.set(
            CreateQuickShipmentPageLocators.DIMENSIONS_LENGTH_FIELD, length
        )

    # Method for Fill Breadth Field
    def fill_breadth_field(self, breadth):
        self.set(
            CreateQuickShipmentPageLocators.DIMENSIONS_BREADTH_FIELD, breadth
        )

    # Method for Fill Height Field
    def fill_height_field(self, height):
        self.set(
            CreateQuickShipmentPageLocators.DIMENSIONS_HEIGHT_FIELD, height
        )

    # Method for Click on Search Courier Button
    def click_search_courier_button(self):
        self.do_scroll_to_element(
            CreateQuickShipmentPageLocators.SEARCH_COURIER_BUTTON
        )
        self.custom_wait()
        self.click(CreateQuickShipmentPageLocators.SEARCH_COURIER_BUTTON)

    # Method for get the alert message when there is no couriers are available
    def get_alert_message_no_couriers(self):
        return self.get(CreateQuickShipmentPageLocators.ALERT_MESSAGE_NO_COURIERS)

    # Method for Click on Back To Create Shipment Button
    def click_back_create_shipment_button(self):
        self.custom_wait()
        self.click(CreateQuickShipmentPageLocators.BACK_TO_CREATE_SHIPMENT_BUTTON)

    # Method for Click on Alert Cancel Button
    def click_alert_cancel_no_couriers(self):
        self.click(CreateQuickShipmentPageLocators.ALERT_CANCEL_NO_COURIERS)

    # Method for Select the value from Rated Drop Down
    def select_option(self, visible_text):
        self.custom_wait()
        self.select_option_by_value(
            CreateQuickShipmentPageLocators.COURIER_RATED_LIST, visible_text
        )

    # Method for get the Pick Up Details
    def get_pickup_details(self):
        return self.get(CreateQuickShipmentPageLocators.PICKUP_FROM_DETAILS)

    # Method for get the Deliver To Details
    def get_deliver_to_details(self):
        return self.get(CreateQuickShipmentPageLocators.DELIVER_TO_DETAILS)

    # Method for get the PayMent Mode Type
    def get_payment_type(self):
        return self.get(CreateQuickShipmentPageLocators.PAYMENT_TYPE)

    # Method for Navigate to URL
    def visit(self):
        self.custom_wait()
        self.driver.get(self.URL)
