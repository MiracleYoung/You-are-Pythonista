from  selenium import webdriver

# 这里指定chromedriver程序的路径
browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

# 设置浏览器窗口的位置和大小
browser.set_window_position(20,40)
browser.set_window_size(1100,700)

# 打开一个页面（QQ空间登录页）
browser.get("http://qzone.qq.com")

# 登录表单在页面的框架中中，所以要切换到该框架
# 对于一个现代的web应用，经常会出现框架（frame）或窗口（window）的应用，这也就给我们的定位带来了一个难题。
# 有时候我们定位一个元素，定位器没有问题，但一直定位不了，这时候就要检查这个元素是否在一个frame中，selenium  webdriver 提供了一个switch_to_frame方法，可以很轻松的来解决
browser.switch_to_frame('login_frame')

# 模拟点击登录按钮
# 根据id定位“用户名密码登录”按钮并点击
browser.find_element_by_id('switcher_plogin').click()
# 根据id定位表单并发送qq号
browser.find_element_by_id('u').clear()
browser.find_element_by_id('u').send_keys('qq号')
# 根据id定位表单并发送qq密码
browser.find_element_by_id('p').clear()
browser.find_element_by_id('p').send_keys('qq密码')
# 查找登录按钮，并点击按钮
browser.find_element_by_id('login_button').click()

# do something

# 这里还可以继续写登录以后需要点击的东西

# 退出窗口
browser.quit()