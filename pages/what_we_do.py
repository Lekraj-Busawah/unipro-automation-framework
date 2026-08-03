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

        # Our Promise Section
        "our promise eyebrow text": (By.XPATH, "//p[normalize-space()='Our promise']"),
        "our promise heading": (By.XPATH, "(//*[@id='services']//h2)[1]"),
        "our promise intro text block": (By.XPATH, "//div[contains(p, 'three essential outcomes')]"),
        "our promise list": (By.XPATH, "//*[@id='services']//ul//p"),
        "our promise list item": (By.XPATH, "(//*[@id='services']//ul//p)[{position}]"),#
        "our promise contact CTA": (By.XPATH, "(//a[@class='button button--primary'][normalize-space()='Contact Us'])[1]"),
        "our promise desktop image": (By.XPATH, "(//*[@id='services']//img[contains(@class,'hide-mobile')])[1]"),
        "our promise mobile image": (By.XPATH, "(//*[@id='services']//img[contains(@class,'hide-desktop')])[1]"),

        # Unipro Difference Section
        "unipro difference eyebrow text": (By.XPATH, "//p[normalize-space()='Our Approach: Human-Led, AI Accelerated Delivery']"),
        "unipro difference heading": (By.XPATH, "//h2[normalize-space()='The Unipro Difference']"),
        "unipro difference intro text block": (By.XPATH, "(//div[contains(@class,'intro-feature-text')])[4]"),
        "unipro difference contact CTA": (By.XPATH, "(//a[@class='button button--primary'][normalize-space()='Contact Us'])[3]"),
        "unipro difference desktop image": (By.XPATH, "(//*[@id='services']//img[contains(@class,'hide-mobile')])[2]"),
        "unipro difference mobile image": (By.XPATH, "(//*[@id='services']//img[contains(@class,'hide-desktop')])[2]"),

        # Final CTA Section
        "final cta eyebrow text": (By.XPATH, "//p[contains(text(),'Ready to Liberate your business')]"),
        "final cta heading": (By.XPATH, "//h2[contains(text(),'Talk to our team to build a bespoke solution')]"),
        "final cta intro text block": (By.XPATH, "//p[contains(text(),'No pressure, no commitment')]"),
        "final cta contact CTA": (By.XPATH, "(//a[@class='button'])[1]"),
    }