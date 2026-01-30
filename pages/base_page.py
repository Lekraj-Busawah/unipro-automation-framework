from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from utilities.read_properties import ReadConfig


class BasePage:
    """
    Parent class for all pages. 
    Contains generic methods and initialisation.
    """

    def __init__(self, driver):
        self.driver = driver
        # Standard explicit wait time
        self.wait_timeout = 10
        self.wait = WebDriverWait(self.driver, self.wait_timeout)

    base_url = ReadConfig.get_application_url()
        
    def navigate_to_base_url(self):
        """
        Navigates to the base URL defined in config.
        Waits for the document ready state and handles cookie consent.
        """
        self.driver.get(self.base_url)
        
        # Wait for the page to fully load
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        self.handle_cookie_consent()

    def wait_for_visibility(self, locator):
        """
        Waits for an element to be visible in the DOM.
        
        Args:
            locator (tuple): (By.STRATEGY, "selector")
        
        Returns:
            WebElement: The visible element.
        """
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} was not visible after {self.wait_timeout} seconds")

    def scroll_to_element(self, locator):
        """Scrolls the view until the element is visible."""
        element = self.wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        

    def wait_for_clickable(self, locator):
        """Waits for element to be visible and enabled."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_element(self, locator):
        """Checks for presence of element in the HTML"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_element(self, locator):
        """Wait for element to be visible and click it."""
        return self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def enter_text(self, locator, text):
        """Wait for element, clears it, and types text."""
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)
    
    def get_title(self, expected_text=None):
        """
        Gets the page title. 
        If expected_text is provided, waits for that text to appear in the title.
        """
        if expected_text:
            self.wait.until(EC.title_contains(expected_text))
        else:
            self.wait.until(lambda driver: len(driver.title) > 0)
            
        return self.driver.title
    
    def set_viewport_size(self, width, height=1080):
        """Resizes the window"""
        self.driver.set_window_size(width, height)

    def handle_cookie_consent(self):
        """
        Checks for a cookie consent banner and accepts it if found.
        Uses a shorter wait time to avoid slowing down tests if banner is absent.
        """
        try:
            accept_btn_locator = (By.XPATH, "//button[contains(@class, 'iubenda-cs-accept-btn')]") 
            
            self.wait_short = WebDriverWait(self.driver, 3)
            btn = self.wait_short.until(EC.element_to_be_clickable(accept_btn_locator))
            btn.click()
            print("Cookie banner accepted.")
        except TimeoutException:
            print("No cookie banner found.")
    
    def wait_for_url_to_be(self, url):
        """Waits until the URL is exactly this string"""
        return self.wait.until(EC.url_to_be(url))

    def wait_for_url_to_contain(self, text):
        """Waits until the URL contains this specific text"""
        return self.wait.until(EC.url_contains(text))
    
    def get_windows_id(self, window):
        """Returns window handle(s) based on the request type."""
        if window == 'original_window':
            return self.driver.current_window_handle
        if window == 'existing_windows':
            return self.driver.window_handles
        
    # ---------------------------------------------------------------------------
    # GENERIC LOCATOR METHODS
    # ---------------------------------------------------------------------------

    def is_visible(self, element_name):
        """
        Look up a locator by name and check if it is displayed.
        """
        locator = self.locators.get(element_name)
        if not locator:
            raise ValueError(f"No locator named '{element_name}' found on {self.__class__.__name__}")
        
        # Returns True/False
        return self.find_element(locator).is_displayed()
    
    def get_element_text(self, element_name):
        """
        Generic method to get stripped text from any element in self.locators
        """
        locator = self.locators.get(element_name)
        if not locator:
            raise ValueError(f"No locator named '{element_name}' found on {self.__class__.__name__}")
        
        element = self.wait_for_visibility(locator)
        return element.text.strip()
    
    def get_element(self, element_name):
        """Returns the raw WebElement"""
        locator = self.locators.get(element_name)
        if not locator:
            raise ValueError(f"No locator named '{element_name}' found on {self.__class__.__name__}")
        
        return self.find_element(locator)