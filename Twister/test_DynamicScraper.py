from Twister.DynamicScraper import DynamicScraper

test_src = "https://twist.moe/anime/18if/[HorribleSubs]%2018if%20-%2001%20[1080p].mp4"


def test_create_and_close_driver():
    """Creates new driver and closes it."""
    testDriver = DynamicScraper()
    testDriver.driver.close()


def test_find_video_src_at_twist_moe():
    """Creates new driver and tries to find video source."""
    testDriver = DynamicScraper()

    assert testDriver.FindVideoSrc("https://twist.moe/a/18if/1") == test_src


def test_find_video_src_fail():
    """Creates new driver and tries to find src with bad link."""
    testDriver = DynamicScraper()
    assert testDriver.FindVideoSrc("asd") is None
