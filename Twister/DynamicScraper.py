#!/usr/bin/env python3
import subprocess
from shutil import which
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options


class DynamicScraper:
    driver = None
    link = None

    options = Options()
    options.headless = True

    delay = 3

    def __init__(self, link, extra_args=None):
        self.link = link
        self.driver = self.GetDriver()
        self.driver.get(link)
        video_src = self.FindVideoSrc()
        self.driver.close()
        subprocess.call(["mpv", video_src, '&'])

    def GetDriver(self):
        if (which("geckodriver") is not None):
            driver = webdriver.Firefox(options=self.options)

        elif (which("chromedriver") is not None):
            driver = webdriver.Chrome(options=self.options)

        else:
            print("You need to have geckodriver or "
                  "chromedriver installed and in PATH to use this."
                  "And if you use chromedriver, you need chrome installed,"
                  "and same if you use geckodriver, you need firefox")
            quit()

        return driver

    def FindVideoSrc(self):
        try:
            print("Trying to find video")
            if (self.link.find("twist") > 0):
                print("Found twist")
                element = WebDriverWait(self.driver, self.delay).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    "video[src*='anime']")))

            else:
                print("Found other")
                element = WebDriverWait(self.driver, self.delay).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "video")))

            return element.get_attribute("src")

        except TimeoutException:
            print("Page loading was too slow")
