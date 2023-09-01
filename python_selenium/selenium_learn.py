import time


def login_page(username, password, driver, By):  # 登录页面
    # driver.find_element(By.XPATH, '//input[@autocomplete="username"]').send_keys(username)
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//input[@autocomplete="current-password"]').send_keys(password)
    # time.sleep(2)
    # driver.find_element(By.XPATH, '//i[@class="icon icon-nocheck"]').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH, '//button[@class="base-button"]').click()
    # time.sleep(1)

    driver.find_element(By.ID, 'username').send_keys(username)
    time.sleep(1)
    driver.find_element(By.ID, 'password').send_keys(password)
    time.sleep(1)
    driver.find_element(By.ID, 'login_submit').click()



def open_url(url, driver):  # 打开页面
    driver.get(url)
    driver.maximize_window()


def search_key(url, driver, username, password, By):
    open_url(url, driver)
    # driver.find_element(By.ID,id='switcher_plogin')
    time.sleep(1)


    # iframe1=driver.find_element(By.XPATH ,'//iframe[@class ="QQMailSdkTool_login_loginBox_qq_iframe"]')   # 连续切换两个窗口
    # driver.switch_to.frame(iframe1)
    # print("切换成功1")
    # iframe2 = driver.find_element(By.XPATH, '//iframe[@id="ptlogin_iframe"]')
    # driver.switch_to.frame(iframe2)
    # print("切换成功2")
    # driver.find_element(By.XPATH,'//a[@id="switcher_plogin"]').click()

    driver.find_element(By.XPATH, '//div[@id="ampHasNoLogin"]').click()

    # iframe1=driver.find_element(By.XPATH ,'//iframe[@name="passport_iframe"]')        # 切换窗口
    # driver.switch_to.frame(iframe1)
    # print("切换成功1")
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//span[text()="密码登录"]').click()

    login_page(username, password, driver, By)
    print("登陆成功")

    # driver.switch_to.parent_frame()

    result = []                 # 打印网页标题
    page_tite = driver.title
    result.append(page_tite)



    return result
