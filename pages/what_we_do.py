from .base_page import BasePage
from selenium.webdriver.common.by import By

class WhatWeDo(BasePage):
    # ---------------------------------------------------------------------------
    # LOCATORS
    # ---------------------------------------------------------------------------
    locators = {
        # Sections
        "hero": (By.CSS_SELECTOR, ".hero-block.block"),
        "build vs buy": (By.CSS_SELECTOR, "#transformation"),
        "our promise": (By.XPATH, "(//div[@id='services'])[1]"),
        "unipro difference": (By.XPATH, "(//div[@id='services'])[2]"),
        "final cta": (By.CSS_SELECTOR, ".cta-block.block"),

        # Hero Section
        "hero eyebrow text": (By.XPATH, "//p[normalize-space()='What we do']"),
        "hero heading": (By.CSS_SELECTOR, "div[class='typography'] h1"),
        "hero intro text block": (By.XPATH, "//p[contains(text(),'agentic AI orchestrated')]"),
    }