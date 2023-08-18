'''
Descripttion: 
Author: zlj
Date: 2023-03-29 11:28:24
'''

from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.locator_username=page.get_by_placeholder("请输入账号")
        self.locator_password=page.locator('#password')
        self.locator_code_image=page.locator("img")
        self.locator_code=page.get_by_placeholder("验证码") 
        self.locator_login_btn = page.get_by_role("button", name="登 录")

        # # 用户名输入框提示语
        # self.locator_username_tip1 = page.get_by_text("请您输入手机号/用户名/邮箱")
    
        # # 密码输入框提示语
        self.locator_password_tip1=page.get_by_text("请输入密码")  #密码为空
        self.locator_password_tip2=page.get_by_text("密码长度为8-16位")#密码长度
     
      
        # # 账号或密码不正确！
        # self.locator_register_error = page.get_by_text("用户名或密码有误，请重新输入或找回密码")

    def navigate(self):
        self.page.goto("http://192.168.3.75:30392/login")

    def fill_username(self, username):
        self.locator_username.fill(username)

    def fill_password(self, password):
        self.locator_password.fill(password)

    def fill_code(self,code):
        self.locator_code.fill(code)    

    def click_login_button(self):
        self.locator_login_btn.click()

