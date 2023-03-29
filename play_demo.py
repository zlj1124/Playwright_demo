from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)          # 启动 chromium 浏览器
    context = browser.new_context()
    page = browser.new_page()              # 打开一个标签页
    page.goto("https://www.baidu.com")     # 打开百度地址
    page.wait_for_timeout(5000)  
    print(page.title())                    # 打印当前页面title



   