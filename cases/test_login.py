'''
Descripttion: 
Author: zlj
Date: 2023-08-07 14:32:38
'''

from models.login_page import LoginPage
from playwright.sync_api import expect
import pytest
import re

class Testother:

    @pytest.fixture(autouse=True)
    def start_for_each(self,login_auth):
        print("for each--start: 打开新页面")
        # browser = playwright.chromium.launch(headless=False)
   
        # context = browser.new_context(storage_state="cookie.json")
        # # context = browser.new_context(storage_state="state.json")
        print(login_auth)
        self.page = login_auth.new_page()
        self.page.goto('http://192.168.3.75:30392/basic-info/sale')
        # self.login = LoginPage(self.page)
        # self.login.navigate()
        yield
        print("for each--close: 关闭登录页")
        self.page.close()

  
    def test_l_1(self):
        """密码框不能为空"""

        # self.page.goto('http://192.168.3.75:30392/basic-info/sale')


        print('11')
        self.page.wait_for_timeout(5000)

 
