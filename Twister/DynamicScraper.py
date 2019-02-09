#!/usr/bin/env python3
from shutil import which

from selenium import webdriver
from selenium.common.exceptions import (
    InvalidArgumentException,
    TimeoutException,
    NoSuchElementException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicScraper:
    """This module creates a scraper what can handle some dynamic websites."""

    driver = None
    link = None
    options = Options()
    options.headless = True
    delay = 10

    def __init__(self):
        """Initialize DynamicScraper class and creates sametime new driver."""
        self.driver = self.GetDriver()

    def GetDriver(self):
        """Check what dirivers user has installed on computer and tries use them."""
        if which("geckodriver") is not None:
            print("Initialized Geckodriver")
            self.driver = webdriver.Firefox(
                options=self.options, service_log_path="/dev/null"
            )

        elif which("chromedriver") is not None:
            print("Initialized Chromedriver")
            self.driver = webdriver.Chrome(options=self.options)

        if self.driver is None:
            raise ValueError(
                "You need to have geckodriver or "
                "chromedriver installed and in PATH to use this."
                "And if you use chromedriver, you need chrome installed,"
                "and same if you use geckodriver, you need firefox"
            )
        return self.driver

    def FindVideoSrc(self, link):
        """Try to find video src attribute from link what is provided.

        Args
        link: Is link to website that contain dynamic video element

        Returns
        Link what's in video element. Or 'None' if fails to find one.

        """
        try:
            self.driver.get(link)
            print("Trying to find video")
            if link.find("twist") > 0:
                """Works with twist.moe site"""
                element = WebDriverWait(self.driver, self.delay).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "video[src*='anime']")
                    )
                )

            else:
                """Try find video element and click it.
                Some hide src before video is actually clicked"""
                try:
                    WebDriverWait(self.driver, self.delay).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "video"))
                    ).click()
                except NoSuchElementException:
                    print("No Suck element found")
                    pass
                element = WebDriverWait(self.driver, self.delay).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "video"))
                )

            temp = element.get_attribute("src")
            self.driver.close()
            return temp

        except (TimeoutException, AttributeError, InvalidArgumentException):
            self.driver.close()
            print("Page loading failed")
            return None


if __name__ == "__main__":
    import sys

    test = DynamicScraper()
    source = sys.argv[1]
    test.FindVideoSrc(source)
