import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)


class TestData:
    CHROME_EXECUTABLE_PATH = parentdir + "\Drivers\chromedriver.exe"
    BASE_URL = "https://www.amazon.in"
    SEARCH_TERM = "WD My Passport 4TB"
    HOME_PAGE_TITLE = "Amazon.in"
    NO_RESULTS_TEXT = "No results found."
    SIGN_IN_PAGE_TITLE = "Amazon Sign In"
