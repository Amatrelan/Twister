# flake8: noqa
from twister.dynamic_scraper import DynamicScraper

test_src = "https://twist.moe/anime/18if/[HorribleSubs]%2018if%20-%2001%20[1080p].mp4"


def test_create_and_close_driver():
    """Creates new driver and closes it."""
    test_driver = DynamicScraper()
    test_driver.driver.close()


def test_find_video_src_at_twist_moe():
    """Creates new driver and tries to find video source."""
    test_driver = DynamicScraper()

    assert test_driver.find_video_src("https://twist.moe/a/18if/1") == test_src


def test_find_video_src_fail():
    """Creates new driver and tries to find src with bad link."""
    test_driver = DynamicScraper()
    assert test_driver.find_video_src("asd") is None
