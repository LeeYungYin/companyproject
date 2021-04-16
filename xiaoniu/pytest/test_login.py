import pytest


@pytest.mark.skip(reason="为什么跳过？")
@pytest.mark.success
class Test_demo:

    def test_login_success(self):
        pass

    def test_login_error(self):
        pass

    def test_login_invaild(self):
        pass

    def test_invent_success(self):
        pass
