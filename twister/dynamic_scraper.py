"""dynamic_scarper.

This handles all jobs required to twister cli to work.
"""
from shutil import which

from selenium import webdriver
from selenium.common.exceptions import (
    InvalidArgumentException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class DynamicScraper:
    """This module creates a scraper what can handle some dynamic websites."""

    driver = None
    link = None
    options = Options()
    options.headless = True
    delay = 10

    def __init__(self):
        """Initialize DynamicScraper class and creates sametime new driver."""
        self.driver = self.get_driver()

    def get_driver(self):
        """Check what dirivers user has installed on computer and tries use them."""
        if which("geckodriver") is not None:
            print("Initialized Geckodriver")
            self.driver = webdriver.Firefox(
                options=self.options, service_log_path="/dev/null", log_path="/dev/null"
            )

        elif which("chromedriver") is not None:
            print("Initialized Chromedriver")
            self.driver = webdriver.Chrome(
                options=self.options, service_log_path="/dev/null"
            )

        if self.driver is None:
            raise ValueError(
                "You need to have geckodriver or "
                "chromedriver installed and in PATH to use this."
                "And if you use chromedriver, you need chrome installed,"
                "and same if you use geckodriver, you need firefox"
            )
        return self.driver

    def find_video_src(self, link):
        """Try to find video src attribute from link what is provided.

        Args
        link: Is link to website that contain dynamic video element

        Returns
        Link what's in video element. Or 'None' if fails to find one.

        """
        if link is None or self.driver is None:
            self.driver.close()
            raise ValueError("Driver wasn't initialized or you didn't provide path.")
        try:
            self.driver.get(link)
            print("Trying to find video")
            if link.find("twist") > 0:
                element = WebDriverWait(self.driver, self.delay).until(
                    ec.presence_of_element_located(
                        (By.CSS_SELECTOR, "video[src*='anime']")
                    )
                )

            else:
                """Try find video element and click it.
                Some hide src before video is actually clicked"""
                try:
                    WebDriverWait(self.driver, self.delay).until(
                        ec.presence_of_element_located((By.CSS_SELECTOR, "video"))
                    ).click()
                except NoSuchElementException:
                    print("No Suck element found")

                element = WebDriverWait(self.driver, self.delay).until(
                    ec.presence_of_element_located((By.CSS_SELECTOR, "video"))
                )

            temp = element.get_attribute("src")
            self.driver.close()
            return temp

        except (TimeoutException, AttributeError, InvalidArgumentException):
            self.driver.close()
            print("Page loading failed")
            return None
