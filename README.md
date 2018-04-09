# myFramework
这个branch修改了部分内容，使用了py3版本，将驱动和HTMLTestRUnner也内置进来了，感谢灰蓝大神

## 1、依赖
selenium、configparser、xlrd

## 2、封装方法介绍
- 控制浏览器后退：back()
- 控制浏览器前进：forward()
- 打开网址：open_url(url)，入参为字符串url
- 屏幕截图：take_screenshot()
- 睡眠等待：sleep(seconds)，入参为秒数
- get_page_title()：获取页面title
- 查找元素方法：find_element(selector)，入参selector为字符串"by=>value"，其中by有如下方式：
1. id
2. name
3. class_name
4. link_text
5. tag_name
6. x-path
7. css_selector
- 清空输入框后输入：clear_type(selector, text, log_text),
selector同上，text为要输入的字符串，log_text为bool值，是否在log记录text，默认为true
- 直接在输入框输入：type(selector, text, log_text),参数与clear_type一致
- 清空输入框：clear(selector)
- 点击元素：click(selector)
- 右击元素：right_click(selector)
- 执行js语句：exec_js(javascript)，入参为js语句字符串
- 获取元素文本：get_text(selector)
- 下拉选择：select(selector, select_type, value)，
select_type有index, value, visible_text三种方式，value为对应type的值
- 移动鼠标到元素上悬停：move_to(selector)
 
## 3、基本用法
1. 修改config文件夹下的ini配置文件，选择要用的浏览器
2. 在page文件夹下写页面类，继承BasePage类，将页面操作写在页面类中
3. 在test_case文件夹写用例类，命名为“test_*.py”，继承MyTest类，将用例写在用例类中
4. 执行run_all.py，生成测试报告

## 4、待扩展功能
邮箱发送测试报告（感觉用处不是特别大）、selenium grid、更多的数据驱动
