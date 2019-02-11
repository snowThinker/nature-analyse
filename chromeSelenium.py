from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('auto-open-devtools-for-tabs')
browser = webdriver.Chrome(chrome_options=options)

browser.get('http://uatm.ag13813.com/login/index.html')
browser.find_element_by_name('loginName').send_keys('18912348989')
browser.find_element_by_name('password').send_keys('qwer1234')
browser.find_element_by_class_name('ag-login-js').click()


