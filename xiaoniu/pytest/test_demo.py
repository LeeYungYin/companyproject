"""
pytest运行用例规则：
模块名称：test_*.py *_test.py 开头或结尾，不要同时满足
函数名称：test_开头的函数
类名称：Test开头的类，除了__init__函数，除非继承unittest.Testcase
可以自己设置规则，目录下创建一个pytest.ini文件

如果只想运行需要的用例行，则在类或者函数前加上@pytest.mark.xx ;然后在命令行输入pytest -m "xx" :xx 为自己定义的名称
为了XX 不在页面报错，可以在pytest.ini文件里面添加 markers = xx ；可以添加多个，换行。

嵌套组合过滤 pytest -m "xx" and "yy" or "zz" and not "aa";

某个功能被废弃了，不需要测试
@pytest.mark.skip(reason = "跳过原因")
遇到某个条件后不执行用例
@pytest.mark.skipif(sys.platform =="win32",reason = "does not run on windows")

pytest 断言
直接用内置函数assert

测试报告
安装pytest-html
pytest -m "xx" --html = reports.html

#log 普通文本
--resultlog = report/demo.txt
#xml xml文件
--junitxml = report/demo.xml

#allure
下载allure 配置环境变量
安装allure-pytest

pytest 和 unittest 的区别
1.pytest有丰富的插件
2.pytest是第三方库，unittest是内置库更稳定
3.pytest执行用例更灵活
4.pytest有更灵活的环境管理
5.pytest自动收集用例

pytest -s 打印输出信息

#重运行机制
如果断言失败，测试用例没有通过，则重新运行一次，如果通过则不会运行重运行机制。
pip install pytest-rerunfailures
pytest --reruns 2 执行2次
pyttest --returns 2 --reruns-delay 2 执行2次 停留2秒钟

#数据驱动
pytest.mark.parametrize("data",data) 用法和DDT相似

##fixture
测试夹具，相当于unittest当中的setup和teardown

yield:生成器 惰性求值

#scope 作用域
当设置class级别，那么一个测试类只会执行一次。

pytest 和 unittest 的兼容问题
如果pytest 用了parametrize 和 fixture 装饰器，那么不能和unittest兼容。
方案一：完全用ptest，不用unittest
方案二：用unittest实现用例，ddt和setup teardown，用pytest 执行和管理用例 mark 和allure生成报告

#减少浏览器的初始化次数，提高测试效率
-需要吧fixture作用域改为class
-提高测试效率，首先必须保证测试用例的稳定性
-在web自动化测试，稳定性最重要
-第一个测试的执行结果不会影响第二个用例

#链式调用
return self 返回自己，然后可以继续调用下一个函数，Loginpage.get().login() 调用get函数，由于返回自身，可以继续调用login函数

#返回方式 (PO模式返回值原则)
第一种：返回self，停留在现在的页面。
第二种：返回其他的页面对象，操作完成后，跳转到其他页面。
第三种：返回元素信息或元素的属性，定位元素

四个封装：
1.PO 2.DDT 3.locator 4.basepage

#basepage 当中定义的方法怎么用到其他的page中？里面还可以封装哪些方法？哪些操作是所有的项目都可以使用的。 直接继承-封装常规操作代码
#WEB 自动化框架
-第一步：框架，和common模块直接拷贝（代码库）
-第二步：basepage 是先拷贝到新项目当中的
-第三步：实现测试数据，data 准备好locator 写到类方法当中
-第四步：编写测试用例方法(根据测试步骤编写方法)，用到各种各样的页面。
-第五步：根据测试步骤在对应的页面封装方法。(不需要把一个页面所有的操作都封装成一个方法)

# 辅助工具可以优化成装饰器，因为是可选的。 (截屏操作-可以优化成装饰器）

修饰器主要作用是为了修饰和扩展某个函数或者类的功能

"""

import unittest

import ddt
import pytest
from selenium import webdriver

cases = [
    {"expected": 1},
    {"expected": 2},
    {"expected": 3}
]


## 如何定义pytest的前置条件
## 声明这是一个fixture测试夹具，这是一个前置和后置条件

# @pytest.fixture()
# def before_test_and_after():
#     """启动浏览器"""
#     print("正在启动浏览器")
#     driver = webdriver.Chrome()
#     yield driver  # 返回参数，但是程序不终止
#
#     driver.quit()


def after_test(driver):
    """关闭浏览器"""
    driver.quit()


# unittest版本
@ddt.ddt
class test_demo(unittest.TestCase):

    @ddt.data(*cases)
    def test_demo(self, case_info):
        self.assertTrue(case_info["expected"] == 3)


# pytest版本

class test_demo2():

    @pytest.mark.parametrize("data", cases)
    def test_demo2(self, case_info, before_test_and_after):  # 传入测试用例和前置后置条件函数
        assert case_info["expected"] == 3


def test_minus(before_test_and_after):
    assert True


if __name__ == '__main__':
    pytest.main()
