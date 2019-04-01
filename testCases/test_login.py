import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customerLogger import LogGen


@pytest.mark.usefixtures("oneTimeSetup")
class Test_001_Login():
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()


    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetup):
        self.driver=self.value


    @pytest.mark.sanity
    def test_homePageTitle(self):

        self.logger.info("************** Test_001_Login ************ ")
        self.logger.info("************** Started home page title test ************ ")

        self.driver=self.value
        self.driver.get(self.baseURL)

        if self.driver.title =="Your store. Login":
            assert True==True
            self.logger.info("************** Home PageTitle test is passed ************ ")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_homePageTitle.png")#Capture screenshot
            assert True==False
            self.logger.error("************** Home PageTitle test is failed ************ ")
        self.driver.close()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self):
        self.logger.info("************** Login Test is started ************ ")
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        if self.driver.title=="Dashboard / nopCommerce administration":
            assert True==True
            self.logger.info("************** Login test test is passed ************ ")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")  # Capture screenshot
            assert True == False
            self.logger.error("************** Login test is failed ************ ")
        self.driver.close()


