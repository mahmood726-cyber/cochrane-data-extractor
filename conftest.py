"""Pytest config for CochraneDataExtractor.

test_page1_url.py and test_page_numbers.py are standalone Selenium
exploration scripts — NOT pytest-compatible. They call
`ChromeDriverManager().install()` and `driver.get(URL)` at module-import
time, so when pytest tries to collect them it downloads chromedriver from
the internet and opens a Chrome session. That takes ~2 min and causes the
triage 60s smoke cap to fire.

Skip collection of these two files unless RUN_BROWSER_TESTS=1.

To run manually:
    python test_page1_url.py
    python test_page_numbers.py
"""
import os

if not os.environ.get("RUN_BROWSER_TESTS"):
    collect_ignore_glob = [
        "test_page1_url.py",
        "test_page_numbers.py",
    ]
