import pytest
from selenium import webdriver

class TestFlaskWebsite:
    # 用正确的用户名和密码，测试登陆是否通过
    @pytest.mark.parametrize('homeUrl,username,password',
        [("http://localhost:5001", "username1", "password1")])
    def test_site_login_success(self, homeUrl, username, password):
        driver = webdriver.Chrome(executable_path=r"D:\PythonProject\AllBrowserDrivers\chromedriver.exe")

        driver.get(homeUrl)
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("//button[text()='登录']").click()

        # 验证界面上是否显示了用户名
        assert driver.find_element_by_id("user").text==username
        # 验证界面上是否显示了“登出”链接
        assert len(driver.find_elements_by_link_text("登出")) == 1

        driver.quit()

    # 用错误的用户名和密码，测试登陆是否不通过
    @pytest.mark.parametrize('homeUrl,errorUsername,errorPassword',
        [("http://localhost:5001", "errorUser1", "errorPwd1")])
    def test_site_login_fail(self, homeUrl, errorUsername, errorPassword):
        driver = webdriver.Chrome()

        driver.get(homeUrl)
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_name("username").send_keys(errorUsername)
        driver.find_element_by_name("password").send_keys(errorPassword)
        driver.find_element_by_xpath("//button[text()='登录']").click()

        # 验证界面上是否显示“用户名或密码错误！”
        assert driver.find_element_by_tag_name("h3").text=="用户名或密码错误！"

        driver.quit()

if __name__ =="__main__":
    pytest.main(["Test_FlaskWebsite.py"])