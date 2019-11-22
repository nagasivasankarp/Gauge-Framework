from selenium.webdriver.common.by import By
from utilities.base_ui import BaseUI


class NewOrderPageLocators:
    ORDER_ID_FIELD = (By.CSS_SELECTOR, '#form_order_id')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#form_first_name')
    EMAIL_ID_FIELD = (By.CSS_SELECTOR, '#form_email')
    PHONE_NUMBER_FIELD = (By.CSS_SELECTOR, '#form_mobile')
    ADDRESS_FIELD = (By.NAME, 'billing_address')
    PINCODE_FIELD = (By.CSS_SELECTOR, '#form_post_code')
    PRODUCT_NAME_FIELD = (By.NAME, 'order_items.0.name')
    SKU_FIELD = (By.CSS_SELECTOR, '#form_enter_sku')
    QUANTITY_FIELD = (By.CSS_SELECTOR, '#form_enter_qty')
    PRICE_FIELD = (By.CSS_SELECTOR, '#form_enter_price')
    WEIGHT_FIELD = (By.NAME, 'weight')
    DIMENSIONS_LENGTH_FIELD = (By.NAME, 'length')
    DIMENSIONS_BREADTH_FIELD = (By.NAME, 'breadth')
    DIMENSIONS_HEIGHT_FIELD = (By.NAME, 'height')
    PAYMENT_METHOD_SELECT = (By.CSS_SELECTOR, '#form_payment_method')
    ADD_ORDER_BUTTON = (By.CSS_SELECTOR, '#form_add_order')
    ORDER_ID_LINK = (By.XPATH, "//table[@id='ordertable']/tbody/tr[1]/td[4]/div/a")
    CANCEL_ORDER_BUTTON = (By.XPATH,
                           "//body[@id='mainbody']/div[3]/section/div/div/div[1]/button[2]")
    CANCEL_CONFIRMATION_BUTTON = (By.XPATH,
                                  "//body[@id='mainbody']/div[1]/div/div/div[1]/button")
    SUCCESS_ALERT_MESSAGE = (By.XPATH,
                             "//div[@class='modal-dialog modal-sm']/div[1]/div[1]/div[1]/h3")
    ALERT_OK_BUTTON = (By.XPATH,
                       "//div[@class='modal-dialog modal-sm']/div[1]/div[1]/div[1]/button")


class NewOrderPage(BaseUI):
    URL = '{}addorder/?redirect_url='.format(BaseUI.BASE_UI_URL)

    # Method for Fill the Order Field
    def fill_order_field(self):
        self.custom_wait()
        order_od = self.timestamp()
        self.set(NewOrderPageLocators.ORDER_ID_FIELD, order_od)

    # Method for Fill the First Name Field
    def fill_first_name_field(self, input_value):
        self.set(NewOrderPageLocators.FIRST_NAME_FIELD, input_value)

    # Method for Fill the Email ID Field
    def fill_email_id_field(self, input_value):
        self.set(NewOrderPageLocators.EMAIL_ID_FIELD, input_value)

    # Method for Fill the Phone Number Field
    def fill_phone_number_field(self, input_value):
        self.set(NewOrderPageLocators.PHONE_NUMBER_FIELD, input_value)

    # Method for Fill the Address Field
    def fill_address_field(self, input_value):
        self.set(NewOrderPageLocators.ADDRESS_FIELD, input_value)

    # Method for Fill the Pincode Field
    def fill_pincode_field(self, input_value):
        self.set(NewOrderPageLocators.PINCODE_FIELD, input_value)

    # Method for Fill the Product name Field
    def fill_product_name_field(self, input_value):
        self.set(NewOrderPageLocators.PRODUCT_NAME_FIELD, input_value)

    # Method for Fill the SKU Field
    def fill_sku_field(self, input_value):
        self.set(NewOrderPageLocators.SKU_FIELD, input_value)

    # Method for Fill the Quantity Field
    def fill_quantity_field(self, input_value):
        self.set(NewOrderPageLocators.QUANTITY_FIELD, input_value)

    # Method for Fill the Price Field
    def fill_price_field(self, input_value):
            self.set(NewOrderPageLocators.PRICE_FIELD, input_value)

    # Method for Fill the Weight Field
    def fill_weight_field(self, input_value):
        return self.set(NewOrderPageLocators.WEIGHT_FIELD, input_value)

    # Method for Fill the Length Field
    def fill_dimensions_length_field(self, input_value):
        return self.set(
            NewOrderPageLocators.DIMENSIONS_LENGTH_FIELD, input_value
        )

    # Method for Fill the Breadth Field
    def fill_dimensions_breadth_field(self, input_value):
        return self.set(
            NewOrderPageLocators.DIMENSIONS_BREADTH_FIELD, input_value
        )

    # Method for Fill the Height Field
    def fill_dimensions_height_field(self, input_value):
        return self.set(
            NewOrderPageLocators.DIMENSIONS_HEIGHT_FIELD, input_value
        )

    # Method for Select the Payment Type
    def select_payment_method_type(self, option_value):
        self.select_option_by_value(
            NewOrderPageLocators.PAYMENT_METHOD_SELECT, option_value
        )

    # Method for click on the order button
    def click_add_order_button(self):
        self.do_scroll_to_element(NewOrderPageLocators.ADD_ORDER_BUTTON)
        self.custom_wait()
        self.click(NewOrderPageLocators.ADD_ORDER_BUTTON)

    # Method for get the order id
    def get_order_id(self):
        self.custom_wait()
        return self.get(NewOrderPageLocators.ORDER_ID_LINK)

    # Method for click on the order id link
    def click_order_id_link(self):
        self.click(NewOrderPageLocators.ORDER_ID_LINK)

    # Method for click on the cancel order button
    def click_cancel_order_button(self):
        self.custom_wait()
        self.click(NewOrderPageLocators.CANCEL_ORDER_BUTTON)

    # Method for click on the cancel order confirmation button
    def click_cancel_order_confirmation_button(self):
        self.custom_wait()
        self.click(NewOrderPageLocators.CANCEL_CONFIRMATION_BUTTON)

    # Method for get the success message
    def get_success_alert_message(self):
        self.custom_wait()
        return self.get(NewOrderPageLocators.SUCCESS_ALERT_MESSAGE)

    # Method for click on the alert ok button
    def click_alert_ok_button(self):
        self.click(NewOrderPageLocators.ALERT_OK_BUTTON)

    # Method for Navigate to URL
    def visit(self):
        self.custom_wait()
        self.driver.get(self.URL)
