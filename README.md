# Page Object Model

Starting an UI Automation in Selenium WebDriver is NOT a tough task. You just need to find elements, perform operations on it.

Consider this simple script 

```python
import time
from selenium import webdriver

chrome_path ="path_to_your_chromedriver"

driver = webdriver.Chrome(chrome_path)

driver.maximize_window()


driver.get('target_url')


driver.find_element_by_css_selector('css_selector').click()


time.sleep(4)

driver.quit()
```

Script maintenance looks easy. But with time test suite will grow. As you add more and more lines to your code, things become tough.

A better approach to script maintenance is to create a separate class file which would find web elements, fill them or verify them. This class can be reused in all the scripts using that element. In future, if there is a change in the web element, we need to make the change in just 1 class file and not 10 different scripts.

This approach is called Page Object Model(POM). It helps make the code more readable, maintainable, and reusable.


# Page Object Model Example

The example script takes a simple web application and tries to have a POM for a simple login case. The Login has various scenarios declared
which will be taken into account which will be embedded inside the test script.

One of the most maintenance is required for object locators. You can also solve this problem by inserting objects for each pages to a single object module by separating them with a container like in a class for each pages. 

```python
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    LOGO_IMAGE =          (By.CLASS_NAME,'log-img')
    LOGIN_DE_TXT =        (By.CLASS_NAME,'.login-text.wow.bounceInDown')
    USERNAME =            (By.XPATH,"//input[contains(@class,'ui-inputfield') and contains(@type,'text')]")
    PASSWORD =            (By.XPATH,"//input[contains(@class,'ui-inputfield') and contains(@type,'password')]")
    LOGIN_BTN=            (By.CLASS_NAME,"login-button")
    ERROR_USERNAME =      (By.XPATH,"//form[contains(@class,'ng-untouched')]/div[1]/div/label")
    ERROR_PASSWORD =      (By.XPATH,"//form[contains(@class,'ng-untouched')]/div[2]/div/label")
    ERROR_USER_PASS =     (By.CSS_SELECTOR,".ui-g-12 p")




class ForgetPasswordLocator(object):
    FORGET_PASSWORD =     (By.XPATH,"//p[@class='login-text']")
    FGT_PASSWORD_FIELD =  (By.XPATH,"//input[contains(@class,'ui-inputfield') and contains(@type,'text')]")
    FGT_PASSWORD_BTN =    (By.CLASS_NAME,"login-button")
    FGT_PASSWORD_EMAIL_ERROR = (By.XPATH,"//div[@class='login-inner']/div/label")



```

# File Flow

The POM contains the following files 

    . base.py
    
Base Class that defines all the base methods that are going to be used in the scripts later.

    . Locators.py
    
 This file will be the placeholder that will hold all the locators at one place.
 
    . LoginPage.py
   
 This file contains the methods that will implement the base class method and use the locators to get the elements.
 
    . testCases.py
  
  This file contains the test cases defined for the login scenario.
  
    . Users.py
    
  For login test cases, we need the account credentials of the users. Users.py contains this information.
  
    . testPages.py
   
  This is the file that contains all the combination of the testcases + Locators methods, which will be the file that will implement 
  the POM model. 
  
  
  
# Running Tests

To run the tests, clone this repository on your system. Then go to the directory and run this using the Python command (if running via
command line)

```python testPages.py```

If you're running via an IDE, then copy this to the system, open this in IDE and run from the ```testPages.py``` file



