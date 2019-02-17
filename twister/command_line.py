#!/usr/bin/env python3
"""Implements twister cli.

This is used to create that simple cli tool for linux.
"""
import subprocess
import sys

from .dynamic_scraper import DynamicScraper


def main(link=None):
    """Create DynamicScraper for cmd use."""
    if link is None:
        link = sys.argv[1]

    scraper = DynamicScraper()
    if scraper is not None:
        source = scraper.find_video_src(link)
        subprocess.call(["mpv", source])


if __name__ == "__main__":
    main(sys.argv[1])
