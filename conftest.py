
from playwright.sync_api import sync_playwright
import pytest
import ddddocr

@pytest.fixture(scope="session")
def login():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    # page=context.new_page()
    # page.goto("http://192.168.3.75:30392/login")

    yield context
    # 实现用例后置
    print('conf中关')
    context.close()
    browser.close()
    p.stop()

@pytest.fixture(scope='session')  
def login_auth():
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()    # 打开标签页
    page.goto("http://192.168.3.75:30392/login")
    page.get_by_placeholder("请输入账号").fill('19956596012')
    page.locator('#password').fill("19956596012")
     # 保存验证码 
    page.locator("img").screenshot(path='yzm.png')  
     
    # 识别验证码  
    ocr = ddddocr.DdddOcr(show_ad=False)  # 实例化  
    with open('yzm.png', 'rb') as f:  # 打开图片  
        img_bytes = f.read()  # 读取图片  
    yzm = ocr.classification(img_bytes)  # 识别  
    print(f'识别到的验证码: {yzm}')  
   
    # 输入验证码  
    page.get_by_placeholder("验证码").fill(yzm) 
    page.get_by_role("button", name="登 录").click()
    page.wait_for_timeout(5000)


    storage = context.storage_state(path="cookie.json")
    context = browser.new_context(storage_state="cookie.json")
    # page=context.new_page()

    print('conf保存cookie')
    print(context)
    yield context
    # 实现用例后置
    print('auth,conf中关')
    context.close()
    browser.close()
    p.stop()
    # page = context.new_page()
    # page.goto('/visualize-runing')
      
