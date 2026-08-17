from selenium.webdriver.common.by import By
from .base_page import BasePage


class SuccessStories(BasePage):
    # ---------------------------------------------------------------------------
    # LOCATORS
    # ---------------------------------------------------------------------------

    locators = {
        # Sections
        "hero": (By.CSS_SELECTOR, ".hero-block"),
        "breadcrumb": (By.CSS_SELECTOR, ".sub-menu-bar-block"),
        "search bar": (By.CSS_SELECTOR, ".archive-page .search-bar"),
        "search input": (By.CSS_SELECTOR, ".archive-page .search-bar input"),
        "success story card grid": (By.CSS_SELECTOR, ".archive-page__cards"),
        "final cta": (By.CSS_SELECTOR, ".cta-block"),

    }