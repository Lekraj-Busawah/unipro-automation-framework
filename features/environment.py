from datetime import datetime
from selenium import webdriver
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from behave import *
import os
import allure

# Initialize the logger once
logger = LogGen.loggen()

def before_scenario(context, scenario):
    try:
        # 1. Read the URL from Config
        context.base_url = ReadConfig.get_application_url()

        # 2. Setup browser    
        browser_name = ReadConfig.get_browser().lower()
        headless_mode = ReadConfig.get_headless_mode() 

        options = None
        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            if headless_mode:
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--window-size=1920,1080")
            context.driver = webdriver.Chrome(options=options)
        
        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            if headless_mode:
                options.add_argument("--headless")
                options.add_argument("--width=1920")
                options.add_argument("--height=1080")
            context.driver = webdriver.Firefox(options=options)

        # Fallback to Chrome if undefined
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            context.driver = webdriver.Chrome(options=options)

        if headless_mode:
            context.driver.set_window_size(1920, 1080)
        else:
            context.driver.maximize_window()

        context.driver.implicitly_wait(0) # Ensure no implicit wait
        logger.info(f"**** Started Scenario: {scenario.name} ****")
    
    except Exception as e:
        logger.error(f"Failed to start scenario: {e}")
        assert False, f"Browser setup failed: {e}"


def after_step(context, step):
    if step.status != 'passed':
        if hasattr(context, 'driver'):
            try:
                # Take the screenshot in memory
                screenshot = context.driver.get_screenshot_as_png()
                
                # Attempt to attach to Allure
                try:
                    allure.attach(
                        screenshot,
                        name="Screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
                except Exception:
                    logger.warning("Could not attach screenshot to Allure report (Context lost)")

            except Exception as e:
                logger.error(f"Failed to capture screenshot: {e}")

def after_scenario(context, scenario):
    # Close Browser
    if hasattr(context, 'driver'):
        try:
            context.driver.quit()
            logger.info(f"**** Finished Scenario: {scenario.name} - Browser Closed ****")
        except Exception:
            pass