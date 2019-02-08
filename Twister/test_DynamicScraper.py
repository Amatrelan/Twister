from Twister.DynamicScraper import DynamicScraper

test_src = 'https://twist.moe/anime/18if/[HorribleSubs]%2018if%20-%2001%20[1080p].mp4'


def test_create_and_close_driver():
    testDriver = DynamicScraper()
    testDriver.driver.close()


def test_find_video_src_at_twist_moe():
    testDriver = DynamicScraper()

    assert testDriver.FindVideoSrc("https://twist.moe/a/18if/1") == test_src


def test_find_video_src_fail():
    testDriver = DynamicScraper()
    testDriver.FindVideoSrc("asd")
