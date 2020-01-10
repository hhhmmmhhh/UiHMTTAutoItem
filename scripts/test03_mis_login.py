import pytest

from tools.read_yaml import read_yaml
# 获取日志对象
from tools.get_log import GetLog

log = GetLog.get_logger()
import page

from page.page_in import PageIn

from tools.get_driver import GetDriver


class TestMisLogin:
    def setup_class(self):
        self.driver = GetDriver.get_driver(page.url_mis)
        # 获取PageMpLogin对象
        self.mis_login = PageIn(self.driver).page_get_PageMisLogin()
        print("参数化读取数据为：", read_yaml("mis_login.yaml"))

    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    @pytest.mark.parametrize("username,password,expect", read_yaml("mis_login.yaml"))
    def test_mis_login(self, username, password, expect):
        # 调用登录业务方法
        self.mis_login.page_mis_login(username, password)
        try:
            # 断言
            assert expect == self.mis_login.page_get_nickname()
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.mis_login.base_get_img()
            # 抛异常
            raise
