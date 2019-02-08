import sys
import subprocess
from Twister.DynamicScraper import DynamicScraper


def main():
    temp = DynamicScraper()
    try:
        source = temp.FindVideoSrc(sys.argv[1])
        subprocess.call(["mpv", source])
    except IndexError:
        temp.driver.close()
        print("This cmd tool need one argument what is link to video website")


if (__name__ == '__main__'):
    main()
