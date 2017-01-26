from selenium import webdriver
chromepath='usr/local/lib/python3.5/site-packages/selenium/chromedriver'
driver = webdriver.Chrome(chromepath)
driver.get('http://naytraangularadmin.sia.co.in/#/login')

#getting the value for the input box

emailinput = driver.find_element_by_css_selector('input.ui-inputfield.ng-pristine.ng-invalid.ui-inputtext.ui-corner-all.ui-state-default.ui-widget.ng-touched')
emailinput.send_keys('ydv.rahul09@gmail.com')
emailinput.is_displayed()

driver.quit()
