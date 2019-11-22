import os
import time
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options


class BaseUI(object):
    BASE_UI_URL = os.getenv('UI_BASE_URL')

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Method for Click on the element
    def click(self, locator):
        element = self.explicit_wait(locator)
        element.click()

    # Method for Explicit wait(45 seconds) to element
    def explicit_wait(self, locator):
        element = WebDriverWait(self.driver, 45).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return element

    # Method for Explicit wait(30 seconds) to list of elements
    def explicit_wait_all_elements(self, locator):
        elements = WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_all_elements_located(locator)
        )
        return elements

    # Method for Explicit wait(*time parameter) to element
    def explicit_wait_custom_time(self, locator, time):
        element = WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located(locator)
        )
        return element

    # Method for set the values in field
    def set(self, locator, value):
        element = self.explicit_wait(locator)
        element.clear()
        element.send_keys(value)

    # Method for get the text from element in a page
    def get(self, locator):
        element = self.explicit_wait(locator)
        return element.text

    # Method for element is displayed or not
    def is_displayed(self, locator):
        element = self.driver.find_element(*locator).is_displayed()
        if element is True:
            return True
        else:
            return False

    # Method for time stamp
    def timestamp(self):
        return datetime.datetime.now().strftime('%M%S%f')

    # Method for Select option by value
    def select_option_by_value(self, locator, option):
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(option)

    # Method for Select option by index
    def select_option_by_index(self, locator, index):
        select = Select(self.driver.find_element(*locator))
        select.select_by_index(index)

    def custom_wait(self):
        time.sleep(3)

    # Method for scroll the page to element
    def do_scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(0, document.documentElement.scrollHeight-10);",
            element)

    # Method for mouse over to element
    def mouse_over(self, loc_tuple):
        self.explicit_wait(loc_tuple)
        element = self.driver.find_element(loc_tuple[0], loc_tuple[1])
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    # Method for multiple window handle
    def window_handle(self, index):
        next_window = self.driver.window_handles[index]
        self.driver.switch_to.window(next_window)

    # Method for accept the alerts
    def accept_alert_popup(self):
        alert_accept = self.driver.switchTo().alert().accept()
        alert_accept.accept()

    # Method to launch the browser in different browsers(chrome, firefox and ie(edge))
    def launch_browser_instance(self, browser_type=None):
        driver = None
        if browser_type is 'chrome':
            options = Options()
            options.add_argument("--disable-notifications")
            driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        elif browser_type is 'firefox':
            options = Options()
            options.add_argument("--disable-notifications")
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_options=options)
        elif browser_type is 'ie':
            driver = webdriver.Edge(EdgeDriverManager().install())
        driver.maximize_window()
        return driver

    # Method for Switch to frame using frame id
    def switch_to_frame_by_id(self, frame_id):
        switch_frame = self.driver.find_element_by_id(*frame_id)
        self.driver.switch_to.frame(switch_frame)

    # Method for switch to default content
    def switch_to_default_frame(self):
        self.driver.switch_to.default_content()

    # Method for get the data from list of elements
    def get_table_data(self, locator):
        table_data = []
        elements = self.explicit_wait_all_elements(locator)
        for element in elements:
            table_data.append(element.text)
        return table_data
