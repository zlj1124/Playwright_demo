'''
Descripttion: 
Author: zlj
Date: 2023-08-07 14:32:38
'''


from models.product_page import ProductPage


from playwright.sync_api import expect
import pytest
import re

class Testother:

    @pytest.fixture(autouse=True)
    def start_for_each(self,login_auth):
        print("for each--start: 打开新页面")
        print(login_auth)

        self.page = login_auth.new_page()
        self.product = ProductPage(self.page)
        self.product.navigate()

        yield
        print("for each--close: 关闭页面")
        self.page.close()

  
    def test_ProductMsg_1(self):
        """销售信息表筛选"""
      
        self.page.wait_for_timeout(1000)
        self.product.select_sales_unit()
        self.product.select_product_line()
        self.product.select_vehicle_type()
        self.product.fill_hierarchy_num("LBF01")
        self.product.fill_vin("TZN01533")
        self.product.click_select_button()
       
        expect(self.product.cell).to_contain_text("TZN01533")

        # self.page.pause() 


 
