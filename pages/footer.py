from .base_page import BasePage
from selenium.webdriver.common.by import By


class Footer(BasePage):
    # locators
    unipro_logo = (By.XPATH, "(//img[@alt='Unipro'])[2]")
    footer_block = (By.XPATH, "(//footer[@class='footer block--dark-purple'])[1]")
    tagline = (By.XPATH, "//p[@class='footer__tagline']")
    email_link = (By.XPATH, "//a[normalize-space()='info@unipro.io']")
    london_office_footer = (By.XPATH, "(//div[@class='footer__col'])[1]")
    havant_office_footer = (By.XPATH, "(//div[@class='footer__col'])[2]")
    london_footer_address = (By.XPATH, "(.//div[contains(@class,'footer__address')])[1]")
    havant_footer_address = (By.XPATH, "(.//div[contains(@class,'footer__address')])[2]")
    linkedin_link = (By.XPATH, "//i[@class='fa-brands fa-linkedin-in']")
    youtube_link = (By.XPATH, "//i[@class='fa-brands fa-linkedin-in']")
    policy_link = {
        'PRIVACY POLICY': (By.XPATH, "(//li[@id='menu-item-480'])[1]"),
        'COOKIE POLICY': (By.XPATH, "(//li[@id='menu-item-482'])[1]"),
        'SECURITY POLICY': (By.XPATH, "(//li[@id='menu-item-1874'])[1]")
    }

    # actions
    def scroll_to_footer(self):
        self.scroll_to_element(self.footer_block)

    def is_footer_visible(self):
        return self.find_element(self.footer_block).is_displayed()
    
    def is_logo_displayed(self):
        return self.find_element(self.unipro_logo).is_displayed()

    def get_tagline_text(self):
        element = self.find_element(self.tagline)
        return element.text
    
    def click_company_logo(self):
        self.click_element(self.unipro_logo)

    def get_footer_email(self):
        return self.find_element(self.email_link)
    
    def get_london_office_section(self):
        return self.find_element(self.london_office_footer)

    def get_havant_office_section(self):
        return self.find_element(self.havant_office_footer)
    
    def get_office_details(self, office):
        if office.lower().__eq__("london"):
            return self.find_element(self.london_footer_address)
        elif office.lower().__eq__("havant"):
            return self.find_element(self.havant_footer_address)