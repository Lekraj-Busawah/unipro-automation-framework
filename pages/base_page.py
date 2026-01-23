from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:
    """
    Parent class for all pages. 
    Contains generic methods and initialisation.
    """

    def __init__(self, driver):
        self.driver = driver
        # Standard explicit wait time
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_visibility(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Element with locator {locator} was not visible after {timeout} seconds")

    def scroll_to_element(self, locator):
        element = self.wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_element(self, locator):
        """Wait for element to be visible and return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click_element(self, locator):
        """Wait for element to be visible and click it."""
        return self.wait.until(EC.element_to_be_clickable(locator)).click()
    
    def enter_text(self, locator, text):
        """Wait for element, clear it, and type text."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_title(self, expected_text=None):
        """
        If expected_text is provided, it waits for that text to appear in the title.
        Otherwise, it just waits for any title to exist.
        """
        if expected_text:
            self.wait.until(EC.title_contains(expected_text))
        else:
            self.wait.until(lambda driver: len(driver.title) > 0)
            
        return self.driver.title
    
    def set_viewport_size(self, width, height):
        """Resizes the window"""
        self.driver.set_window_size(width, height)

    def handle_cookie_consent(self):
        """Checks for cookie banner and accepts if present."""
        try:
            accept_btn_locator = (By.XPATH, "//button[contains(@class, 'iubenda-cs-accept-btn')]") 
            
            wait_short = WebDriverWait(self.driver, 3)
            btn = wait_short.until(EC.element_to_be_clickable(accept_btn_locator))
            btn.click()
            print("Cookie banner accepted.")
        except:
            print("No cookie banner found.")
    
    def wait_for_url_to_be(self, url):
        """Waits until the URL is exactly this string"""
        return self.wait.until(EC.url_to_be(url))

    def wait_for_url_to_contain(self, text):
        """Waits until the URL contains this specific text"""
        return self.wait.until(EC.url_contains(text))
    
    
    def get_windows_id(self, window):
        if window == 'original_window':
            return self.driver.current_window_handle
        if window == 'existing_windows':
            return self.driver.window_handles