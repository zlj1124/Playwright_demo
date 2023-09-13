'''
Descripttion: 
Author: zlj
Date: 2023-08-18 16:26:33
'''

from playwright.sync_api import Page


class ProductPage:

    def __init__(self, page: Page):
        self.page = page
        #搜索框
        self.sales_unit=page.locator(".ant-select-selection-overflow").first #销售单位框
        self.sales_value=page.get_by_title("新能源营销").get_by_text("新能源营销")
        
        self.product_line=page.locator('#product_lines')
            
        self.line_value=page.get_by_title("帅铃", exact=True).get_by_text("帅铃")

        self.vehicle_type=page.locator("#vehicle_type")
        self.type_value=page.get_by_title("混动-PS").get_by_text("混动-PS")

        self.hierarchy_num=page.get_by_placeholder("结构号")
        self.vin=page.get_by_placeholder("底盘号") 
        self.select_btn = page.get_by_role("button", name="查 询")
        #验证
        self.cell =page.get_by_role("cell", name="TZN01533")


    def navigate(self):
        self.page.goto('http://192.168.3.75:30392/basic-info/sale')

    def select_sales_unit(self):
        self.sales_unit.click()
        self.sales_value.click()

    def select_product_line(self):
        self.product_line.click()
        self.line_value.click()

    def select_vehicle_type(self):
        self.vehicle_type.click()  
        self.type_value.click()

    def fill_hierarchy_num(self,num):
        self.hierarchy_num.fill(num)  

    def fill_vin(self,vin):
        self.vin.fill(vin)      

    def click_select_button(self):
        self.select_btn.click()

