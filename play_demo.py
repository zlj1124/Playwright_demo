
from playwright.sync_api import sync_playwright

import ddddocr

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()  # 创建上下文，浏览器实例

    page = context.new_page()    # 打开标签页
    page.goto("http://192.168.3.75:30392/login")
    # # page.pause()
    print(page.title())
    page.get_by_placeholder("请输入账号").fill('19956596012')
    page.locator('#password').fill("19956596012")
     # 保存验证码 
    page.locator("img").screenshot(path='yzm.png')  
     
    # 识别验证码  
    ocr = ddddocr.DdddOcr(show_ad=False)  # 实例化  
    with open('yzm.png', 'rb') as f:  # 打开图片  
        img_bytes = f.read()  # 读取图片  
    yzm = ocr.classification(img_bytes)  # 识别  
    print(f'识别到的验证码: {yzm }')  
   
    # 输入验证码  
    page.get_by_placeholder("验证码").fill(yzm) 
    page.get_by_role("button", name="登 录").click()
    storage = context.storage_state(path="cookie.json")

    page.pause()
    
  
  
    
    # # Get page after a specific action (e.g. clicking a link)
    # with context.expect_page() as new_page_info:
    #     page.click('text=贴吧')  # Opens a new tab
    # new_page = new_page_info.value

    # new_page.wait_for_load_state()  # 等待页面加载到指定状态
    # print(new_page.title())