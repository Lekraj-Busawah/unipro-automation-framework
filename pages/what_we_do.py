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
        "desktop hero image": (By.CSS_SELECTOR, ".hero-block__image.hide-mobile"),
        "mobile hero image": (By.CSS_SELECTOR, ".hero-block__image.hide-desktop"),

        # Build vs Buy Section
        "build vs buy eyebrow text": (By.XPATH, "//p[normalize-space()='Build vs Buy']"),
        "build vs buy heading": (By.CSS_SELECTOR, "div#transformation h2"),
        "build vs buy intro text block": (By.XPATH, "//p[contains(., 'Off-the-Shelf Solutions')]"),
        "build vs buy contact CTA": (By.XPATH, "//div[@id='transformation']//a[contains(@class,'button button--primary')]"),
        "build vs buy desktop image": (By.XPATH, "//div[@id='transformation']//img[contains(@class,'hide-mobile')][1]"),
        "build vs buy mobile image": (By.XPATH, "//div[@id='transformation']//img[contains(@class,'hide-desktop')][1]"),

    }