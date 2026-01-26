from .base_page import BasePage
from selenium.webdriver.common.by import By


class Homepage(BasePage):
    # locators
    hero_section = (By.CSS_SELECTOR, ".hero-block.block")
    heading = (By.CSS_SELECTOR, "div[class='typography'] h1")
    intro_text = (By.XPATH, "(//div[@class='intro-feature-text'])[1]")


    # actions