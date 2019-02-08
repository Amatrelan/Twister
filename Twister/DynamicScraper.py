#!/usr/bin/env python3
from shutil import which
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, InvalidArgumentException
from selenium.webdriver.firefox.options import Options


class DynamicScraper:
    driver = None
    link = None

    options = Options()
    options.headless = True

    delay = 3

    def __init__(self):
        self.driver = self.GetDriver()

    def GetDriver(self):
        if (which("geckodriver") is not None):
            print("Initialized Geckodriver")
            driver = webdriver.Firefox(options=self.options)

        elif (which("chromedriver") is not None):
            print("Initialized Chromedriver")
            driver = webdriver.Chrome(options=self.options)

        else:
            print("You need to have geckodriver or "
                  "chromedriver installed and in PATH to use this."
                  "And if you use chromedriver, you need chrome installed,"
                  "and same if you use geckodriver, you need firefox")
            quit()

        return driver

    def FindVideoSrc(self, link):
        try:
            self.driver.get(link)
            print("Trying to find video")
            if (link.find("twist") > 0):
                element = WebDriverWait(self.driver, self.delay).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    "video[src*='anime']")))

            else:
                element = WebDriverWait(self.driver, self.delay).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "video")))

            temp = element.get_attribute("src")
            self.driver.close()
            return temp

        except (TimeoutException, AttributeError, InvalidArgumentException):
            self.driver.close()
            print("Page loading was too slow")
