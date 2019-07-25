import pytest
from selenium import webdriver
import allure
import logging, sys


logger = logging.getLogger("Test_case")
logger.setLevel(logging.DEBUG)


@allure.step("First step of Execution")
@pytest.fixture()
def open_browser(request):
    driver = webdriver.Chrome(r"D:\\Programe_Files\\chromedriver_win32\\chromedriver.exe")
    logger.debug("open_browser Fucn: %s" % "Open chrome browser")
    driver.maximize_window()
    logging.debug("open_browser Fucn: %s" % "Maximize the window of the browser")
    @allure.step("End of the Execution")
    def close_browser():
        driver.close()
        logger.debug("close_browser Fucn: %s" % "close the chrome browser")
    request.addfinalizer(close_browser)

    return driver


@allure.feature("Chrome_browser_First_page")
@allure.title("Nakuri Website Page")
class TestWebClass:

    @allure.story("Job requirement or Job search page ")
    @allure.step("Start Execution")
    @allure.description("To verify nakuri website in chrome browser")
    def test_nakuri_first_page_001(self, open_browser):
        page_actual_tittle='Jobs - Recruitment - Job Search - Employment - Job Vacancies - Naukri.com'
        open_browser.get("https://www.naukri.com/")
        try:
            self.page_expected_tittle = open_browser.title
            logger.debug("Started Comparision")
            logger.debug("===================")
        except Exception as e:
            print("Test case exception: %s" % (str(e)), file=sys.stderr)
        assert self.page_expected_tittle == page_actual_tittle
        logger.debug("My custom msg: Expected {} actual status {}".format(self.page_expected_tittle, page_actual_tittle))
        print("First case expected Result: %s" % self.page_expected_tittle)






