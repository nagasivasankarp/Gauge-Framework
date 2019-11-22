from getgauge.python import step
from getgauge.python import Messages
from step_impl.pages.page_factory import PageFactory
import os


@step("Login as a user")
def login_as_a_user():
    try:
        PageFactory.login_page.visit()
        home_page_title = PageFactory.login_page.get_page_title()
        Messages.write_message("Application is Launched in Browser")
        if home_page_title is 'eCommerce Logistics & Shipping Solutions: Multiple Courier Aggregator India':
            Messages.write_message("Application Home Page Title is : " + home_page_title)
        else:
            Messages.write_message("Application Home Page Title is : " + home_page_title)
        PageFactory.login_page.fill_email_address_field(os.getenv('UI_SR_EMAIL_ADDRESS'))
        PageFactory.login_page.fill_password_field(os.getenv('UI_SR_PASSWORD'))
        PageFactory.login_page.click_login_button()
        company_name = PageFactory.login_page.get_company_name()
        if company_name is 'CSSquareTech':
            Messages.write_message("User is Successfully Logged into Application")
        else:
            Messages.write_message("User is not Logged into Application")
    except Exception as e:
        raise AssertionError("Exception is ", e)


@step("Create a quick shipment with invalid data <table>")
def create_a_quick_shipment_with_invalid_data(table):
    try:
        for rows in table:
            if not rows:
                break
            PageFactory.create_quick_shipment_page.visit()
            PageFactory.create_quick_shipment_page.fill_deliver_to_field(rows[0])
            PageFactory.create_quick_shipment_page.fill_product_name_field(rows[1])
            PageFactory.create_quick_shipment_page.fill_quantity_field(rows[2])
            PageFactory.create_quick_shipment_page.fill_unit_price_field(rows[3])
            PageFactory.create_quick_shipment_page.fill_weight_field(rows[4])
            PageFactory.create_quick_shipment_page.fill_length_field(rows[5])
            PageFactory.create_quick_shipment_page.fill_breadth_field(rows[6])
            PageFactory.create_quick_shipment_page.fill_height_field(rows[7])
            PageFactory.create_quick_shipment_page.click_search_courier_button()
            alert_message_no_couriers = PageFactory.create_quick_shipment_page.get_alert_message_no_couriers()
            assert alert_message_no_couriers == 'Weight limit exceeded for the entered pin codes.'
            Messages.write_message("Alert Message When No Couriers Available : " + alert_message_no_couriers)
            PageFactory.create_quick_shipment_page.click_alert_cancel_no_couriers()
    except Exception as e:
        raise AssertionError("Exception is ", e)


@step("Create a quick shipment with valid data <table>")
def create_a_quick_shipment_with_valid_data(table):
    try:
        for rows in table:
            if not rows:
                break
            PageFactory.create_quick_shipment_page.click_back_create_shipment_button()
            PageFactory.create_quick_shipment_page.fill_deliver_to_field(rows[0])
            PageFactory.create_quick_shipment_page.fill_product_name_field(rows[1])
            PageFactory.create_quick_shipment_page.fill_quantity_field(rows[2])
            PageFactory.create_quick_shipment_page.fill_unit_price_field(rows[3])
            PageFactory.create_quick_shipment_page.fill_weight_field(rows[4])
            PageFactory.create_quick_shipment_page.fill_length_field(rows[5])
            PageFactory.create_quick_shipment_page.fill_breadth_field(rows[6])
            PageFactory.create_quick_shipment_page.fill_height_field(rows[7])
            PageFactory.create_quick_shipment_page.click_search_courier_button()
            PageFactory.create_quick_shipment_page.select_option('CHEAPEST')
            pickup_description = PageFactory.create_quick_shipment_page.get_pickup_details()
            Messages.write_message("Courier Pickup Description for the above selected : " + pickup_description)
            deliver_to_description = PageFactory.create_quick_shipment_page.get_deliver_to_details()
            Messages.write_message("Courier Deliver Description for the above selected : " + deliver_to_description)
            payment_mode_type = PageFactory.create_quick_shipment_page.get_payment_type()
            Messages.write_message("Payment Type for Courier is : " + payment_mode_type)
            PageFactory.create_quick_shipment_page.select_option('FASTEST')
            Messages.write_message("Selected the Courier Type as : FASTEST")
            pickup_description = PageFactory.create_quick_shipment_page.get_pickup_details()
            Messages.write_message("Courier Pickup Description for the above selected : " + pickup_description)
            deliver_to_description = PageFactory.create_quick_shipment_page.get_deliver_to_details()
            Messages.write_message("Courier Deliver Description for the above selected : " + deliver_to_description)
            payment_mode_type = PageFactory.create_quick_shipment_page.get_payment_type()
            Messages.write_message("Payment Type for Courier is : " + payment_mode_type)
            PageFactory.create_quick_shipment_page.select_option('BEST RATED')
            Messages.write_message("Selected the Courier Type as : BEST RATED")
            pickup_description = PageFactory.create_quick_shipment_page.get_pickup_details()
            Messages.write_message("Courier Pickup Description for the above selected : " + pickup_description)
            deliver_to_description = PageFactory.create_quick_shipment_page.get_deliver_to_details()
            Messages.write_message("Courier Deliver Description for the above selected : " + deliver_to_description)
            payment_mode_type = PageFactory.create_quick_shipment_page.get_payment_type()
            Messages.write_message("Payment Type for Courier is : " + payment_mode_type)
            PageFactory.create_quick_shipment_page.select_option('CUSTOM')
            Messages.write_message("Selected the Courier Type as : CUSTOM")
            pickup_description = PageFactory.create_quick_shipment_page.get_pickup_details()
            Messages.write_message("Courier Pickup Description for the above selected : " + pickup_description)
            deliver_to_description = PageFactory.create_quick_shipment_page.get_deliver_to_details()
            Messages.write_message("Courier Deliver Description for the above selected : " + deliver_to_description)
            payment_mode_type = PageFactory.create_quick_shipment_page.get_payment_type()
            Messages.write_message("Payment Type for Courier is : " + payment_mode_type)
    except Exception as e:
        raise AssertionError("Exception is ", e)


@step("Shipping Rates Calculator <table>")
def shipping_rates_calculator(table):
    try:
        for rows in table:
            if not rows:
                break
            PageFactory.shipping_rates_calculator_page.visit()
            PageFactory.shipping_rates_calculator_page.fill_pickup_pincode_field(rows[0])
            PageFactory.shipping_rates_calculator_page.fill_delivery_pincode_field(rows[1])
            PageFactory.shipping_rates_calculator_page.fill_weight_field(rows[2])
            PageFactory.shipping_rates_calculator_page.fill_dimensions_length_field(rows[3])
            PageFactory.shipping_rates_calculator_page.fill_dimensions_breadth_field(rows[4])
            PageFactory.shipping_rates_calculator_page.fill_dimensions_height_field(rows[5])
            PageFactory.shipping_rates_calculator_page.fill_declared_value_field(rows[6])
            PageFactory.shipping_rates_calculator_page.click_calculate_button()
            courier_type_air = PageFactory.shipping_rates_calculator_page.get_courier_type_air()
            Messages.write_message("Courier Type : " + courier_type_air)
            courier_air_list = PageFactory.shipping_rates_calculator_page.get_air_courier_provider_list()
            for courier_list in courier_air_list:
                Messages.write_message("Couriers List  : " + courier_list)
            courier_surface = PageFactory.shipping_rates_calculator_page.get_air_courier_rate_list()
            courier_type_surface = PageFactory.shipping_rates_calculator_page.get_courier_type_surface()
            Messages.write_message("Courier Type : " + courier_type_surface)
            for courier_list in courier_surface:
                Messages.write_message("Couriers List  : " + courier_list)

    except Exception as e:
        raise AssertionError("Exception is ", e)


@step("Create a add New Order <table>")
def create_a_add_new_order(table):
    try:
        for rows in table:
            if not rows:
                break
            PageFactory.new_order_page.visit()
            PageFactory.new_order_page.fill_order_field()
            PageFactory.new_order_page.fill_first_name_field(rows[1])
            PageFactory.new_order_page.fill_email_id_field(rows[2])
            PageFactory.new_order_page.fill_phone_number_field(rows[3])
            PageFactory.new_order_page.fill_address_field(rows[4])
            PageFactory.new_order_page.fill_pincode_field(rows[5])
            PageFactory.new_order_page.fill_product_name_field(rows[6])
            PageFactory.new_order_page.fill_sku_field(rows[7])
            PageFactory.new_order_page.fill_quantity_field(rows[12])
            PageFactory.new_order_page.fill_price_field(rows[13])
            PageFactory.new_order_page.fill_weight_field(rows[8])
            PageFactory.new_order_page.fill_dimensions_length_field(rows[9])
            PageFactory.new_order_page.fill_dimensions_breadth_field(rows[10])
            PageFactory.new_order_page.fill_dimensions_height_field(rows[11])
            PageFactory.new_order_page.select_payment_method_type('Cash On Delivery')
            PageFactory.new_order_page.click_add_order_button()
            order_id = PageFactory.new_order_page.get_order_id()
            Messages.write_message("Order Id is : " + order_id)
            PageFactory.new_order_page.click_order_id_link()
            PageFactory.new_order_page.click_cancel_order_button()
            PageFactory.new_order_page.click_cancel_order_confirmation_button()
            order_success_message = PageFactory.new_order_page.get_success_alert_message()
            Messages.write_message("Message as : " + order_success_message)
            PageFactory.new_order_page.click_alert_ok_button()

    except Exception as e:
        raise AssertionError("Exception is ", e)
