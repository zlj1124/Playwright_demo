'''
Descripttion: 
Author: zlj
Date: 2023-03-29 11:29:45
'''
import ddddocr
from models.login_page import LoginPage
from playwright.sync_api import expect
import pytest
import re

class Testlogin:

    @pytest.fixture(autouse=True)
    def start_for_each(self, login):
        print("for each--start: 打开新页面访问登录页")
        self.page = login.new_page()
        self.login = LoginPage(self.page)
        self.login.navigate()
        yield
        print("for each--close: 关闭登录页")
        self.page.close()
        

  
    def test_login_1(self):
        """密码框不能为空"""
     
        self.login.fill_username('13011223344')
        self.login.fill_password('')
        self.login.click_login_button()
        # 断言
        expect(self.login.locator_password_tip1).to_be_visible()
        expect(self.login.locator_password_tip1).to_contain_text("请输入密码")    

   

    @pytest.mark.parametrize('test_input', ['abc12', 'abcd111'])
    def test_login_2(self, test_input):
        """密码框6-16位"""
        self.login.fill_username('13011223344')
        self.login.fill_password(test_input)
        # 断言
        expect(self.login.locator_password_tip2).to_be_visible()
        expect(self.login.locator_password_tip2).to_contain_text("密码长度为8-16位")
        # self.page.pause()

    # @pytest.mark.skip()
    def test_login_3(self):
        """登录成功"""
        self.login.fill_username('13011223344')
        self.login.fill_password('13011223344')
        self.locator_code_image=self.login.locator_code_image.screenshot(path='yzm.png')
        ocr = ddddocr.DdddOcr(show_ad=False)  # 实例化  
        with open('yzm.png', 'rb') as f:  # 打开图片  
            img_bytes = f.read()  # 读取图片  
        yzm = ocr.classification(img_bytes)  # 识别  
        self.login.fill_code(yzm)
        self.login.locator_login_btn
        self.login.click_login_button()
        #断言  
        self.page.wait_for_timeout(1000)
        expect(self.page).to_have_title(re.compile("运行监控"))
        # expect(self.login).to_be_visible()


  


 
