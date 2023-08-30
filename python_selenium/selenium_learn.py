def login_page(username, password, driver, By):  # 登录页面
    driver.find_element(By.ID, 'username').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login_submit').click()


def open_url(url, driver):  # 打开页面
    driver.get(url)
    driver.maximize_window()


def search_key(url, driver, username, password, By):
    open_url(url, driver)
    login_page(username, password, driver, By)
    result = []
    page_tite = driver.title
    result.append(page_tite)
    # print("标题是：{}".format(page_tite))
    page_text = driver.find_element(By.XPATH, '//a[@id="userNameLogin_a"]').text
    result.append(page_text)
    return result
