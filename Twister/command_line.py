import subprocess
import sys

from Twister.DynamicScraper import DynamicScraper


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

    scraper = DynamicScraper()
    if scraper is not None:
        source = scraper.FindVideoSrc(tempLink)
        subprocess.call(["mpv", source])


if __name__ == "__main__":
    main()
