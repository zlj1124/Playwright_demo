
from models.login_page import RegisterPage
from playwright.sync_api import expect
import pytest

class TestRegister:

    @pytest.fixture(autouse=True)
    def start_for_each(self, context_chrome):
        print("for each--start: 打开新页面访问登录页")
        self.page = context_chrome.new_page()
        self.register = RegisterPage(self.page)
        self.register.navigate()
        yield
        print("for each--close: 关闭登录页")
        self.page.close()

    def test_register_1(self):
        """用户名为空，点登录"""
        self.register.click_login_link()
        self.register.fill_username('')
        self.register.fill_password('123456')
        self.register.click_login_button()
        # 断言
        expect(self.register.locator_username_tip1).to_be_visible()
        expect(self.register.locator_username_tip1).to_contain_text("请您输入手机号/用户名/邮箱")

    def test_register_4(self):
        """密码框不能为空"""
        self.register.click_login_link()
        self.register.fill_username('hello')
        self.register.fill_password('')
        self.register.click_login_button()
        # 断言
        expect(self.register.locator_password_tip1).to_be_visible()
        expect(self.register.locator_password_tip1).to_contain_text("请您输入密码")    

   

    # @pytest.mark.parametrize('test_input', ['abc12', 'abc1234567890abc1'])
    # def test_register_5(self, test_input):
    #     """密码框6-16位"""
    #     self.register.fill_password(test_input)
    #     # 断言
    #     expect(self.register.locator_password_tip2).to_be_visible()
    #     expect(self.register.locator_password_tip2).to_contain_text("密码6-16位字符")

 

  


 
