
import time

def test_google_title(setup):
    driver = setup
    driver.get("https://www.google.com")
    time.sleep(5)
    assert "Google" in driver.title
