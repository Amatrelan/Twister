import subprocess
import sys

from dvscraper import dynamic_scraper


def main(link=None):
    """Create DynamicScraper for cmd use."""
    if link is not None:
        tempLink = link
    else:
        try:
            tempLink = sys.argv[1]
        except IndexError:
            print("This cmd tool need one argument what is link to video website")
            return -1

    scraper = dynamic_scraper.DynamicScraper()
    if scraper is not None:
        source = scraper.find_video_src(tempLink)
        subprocess.call(["mpv", source])


if __name__ == "__main__":
    main()
