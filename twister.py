#!/usr/bin/env python3
import sys
import subprocess
from shutil import which
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options

_options = Options()
_options.headless = True

_delay = 3


class TwistScraper:
    def __init__(self, link):
        if (which("geckodriver") is not None):
            self.driver = webdriver.Firefox(options=_options)
        elif (which("chromedriver") is not None):
            self.driver = webdriver.Chrome(options=_options)
        else:
            print("You need to have geckodriver or "
                  "chromedriver installed and in PATH to use this."
                  "And if you use chromedriver, you need chrome installed,"
                  "and same if you use geckodriver, you need firefox")
            quit()

        self.driver.get(link)

        try:
            print("Trying to find video")
            if (link.find("twist") > 0):
                print("Found twist")
                element = WebDriverWait(self.driver, _delay).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    "video[src*='anime']")))
            else:
                print("Found other")
                element = WebDriverWait(self.driver, _delay).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "video")))

            link = element.get_attribute("src")
            self.driver.close()
            subprocess.call(["mpv", link])

        except TimeoutException:
            print("Page loading was too slow")


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("This tool takes only one argument right now")
        quit()
    link = sys.argv[1]
    twister = TwistScraper(link)
