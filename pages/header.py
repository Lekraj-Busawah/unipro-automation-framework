from selenium.webdriver.common.by import By
from .base_page import BasePage
from utilities.read_properties import ReadConfig
from selenium.webdriver.support import expected_conditions as EC

class Header(BasePage):

    BASE_URL = ReadConfig.get_application_url()

    @staticmethod
    def link_locator(path):
        return (By.XPATH, f"//a[contains(@href, '{path}')]")
    
    # locators
    header_block = (By.XPATH, "//header[contains(@class, 'header')]")
    header_logo = (By.XPATH, "//div[@class='header__logo']//img[contains(@src, 'unipro-logo')]")
    main_menu = (By.XPATH, "//div[@class='main-menu']")
    who_we_are = link_locator("who-we-are")
    what_we_do = link_locator("what-we-do")
    who_we_do_it_for = link_locator("who-we-do-it-for")
    insights = (By.XPATH, "//a[contains(text(), 'Insights')]")
    contact_us = link_locator("contact-us")
    careers = link_locator("careers")
    hamburger_menu = (By.XPATH, "//*[contains(@class, 'hamburger')]")

    # actions
    def check_header_visible(self):
        header_block = self.wait_for_visibility(self.header_block)
        assert header_block.is_displayed(), "Header block is not visible"

    def check_logo_visible(self):
        header_logo = self.wait_for_visibility(self.header_logo)
        assert header_logo.is_displayed(), "Header logo is not visible"

    def check_main_menu_visible(self):
        main_menu = self.wait_for_visibility(self.main_menu)
        assert main_menu.is_displayed(), "Main menu is not visible"

    def click_menu_item(self, menu_item):
        menu_item = menu_item.lower().strip().replace(" ", "_")

        # Create a mapping between menu item names and locators
        menu_mapping = {
            "who_we_are": self.who_we_are,
            "what_we_do": self.what_we_do,
            "who_we_do_it_for": self.who_we_do_it_for,
            "insights": self.insights,
            "contact_us": self.contact_us,
            "careers": self.careers
        }

        # Validate the menu item
        if menu_item not in menu_mapping:
            raise ValueError(f"Invalid menu item: {menu_item}. "
                            f"Valid options are: {', '.join(menu_mapping.keys())}")

        # Click the element
        self.click_element(menu_mapping[menu_item])

    def verify_page_navigation_by_url(self, expected_path):
        """
        Waits until the URL contains the expected path string.
        """
        try:
            self.wait.until(EC.url_contains(expected_path))
        except:
            # If timeout occurs, fail with a clear message
            actual_url = self.driver.current_url
            raise AssertionError(f"Expected URL to contain '{expected_path}', but found '{actual_url}'")
    
    def is_hamburger_visible(self):
        """
        Check if hamburger menu is visible (mobile layout).
        """
        try:
            element = self.wait_for_visibility(self.hamburger_menu)
            return element.is_displayed()
        except:
            return False








            

