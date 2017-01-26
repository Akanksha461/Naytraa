from selenium.webdriver.common.by import By

class NavigatonUIClassLocators(object):
    NAVBAR              =        (By.XPATH,"//div[@class='navbar']")
    NAYTR_LOGO          =        (By.XPATH,"//div[@class='navbar']/div[1]/div/div/div[1]/a/img")

class NavigationFunctionLocators(object):
    USERNAME_IMG        =        (By.XPATH,"//div[@id='logout']/img")
    USERNAME            =        (By.XPATH,"//div[@id='logout']/div[1]/span/span")
    USERNAME_CLICK      =        (By.XPATH,"//div[@id='logout']/div[1]/span/span")
    LOGOUT              =        (By.XPATH,"//div[contains(@id='logout') and contains(@class='user-drop')]")
    LOGOUT_2            =        (By.CSS_SELECTOR,"div#logout.a")

class DashboardSidebar(object):
    DASHBOARD_SIDEBAR=(By.XPATH,"//div[@class='sidenav']")


class ContentSection(object):
    CONTENT_SECTION=(By.CLASS_NAME,"content-section.ui-g-12")
    



