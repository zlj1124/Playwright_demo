'''
Descripttion: 
Author: zlj
Date: 2023-03-29 11:28:24
'''

from playwright.sync_api import Page


class RegisterPage:

    def __init__(self, page: Page):
        self.page = page
        
        self.locator_login_link = page.get_by_role("link", name="登录")#登录按钮
        self.locator_username = page.get_by_placeholder("手机号/用户名/邮箱")
        self.locator_password = page.get_by_placeholder("密码")
        self.locator_login_btn = page.get_by_role("button", name="登录")
        # self.locator_login_link = page.locator('text=已有账号？点这登录')
        # 用户名输入框提示语
        self.locator_username_tip1 = page.get_by_text("请您输入手机号/用户名/邮箱")
    
        # 密码输入框提示语
        self.locator_password_tip1 = page.get_by_text('请您输入密码')
      
        # 账号或密码不正确！
        self.locator_register_error = page.get_by_text("用户名或密码有误，请重新输入或找回密码")

    def navigate(self):
        self.page.goto("https://www.baidu.com")

    def fill_username(self, username):
        self.locator_username.fill(username)

    def fill_password(self, password):
        self.locator_password.fill(password)

    def click_login_button(self):
        self.locator_login_btn.click()

    def click_login_link(self):
         self.locator_login_link.click()
