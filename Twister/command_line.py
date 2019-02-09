import subprocess
import sys

from Twister.DynamicScraper import DynamicScraper


def main(link=None):
    """Create DynamicScraper for cmd use."""
    if link is not None:
        tempLink = link
    else:
        tempLink = sys.argv[1]
        pass

    scraper = DynamicScraper()
    try:
        if scraper is not None:
            source = scraper.FindVideoSrc(tempLink)
            subprocess.call(["mpv", source])
    except IndexError:
        scraper.driver.close()
        print("This cmd tool need one argument what is link to video website")


if __name__ == "__main__":
    main()
