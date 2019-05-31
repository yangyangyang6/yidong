# allure generate report/ -o report/html --clean
# --alluredir report
class TestLogin:
    def test_login1(self):
        print(1)
        assert 1

    def test_login2(self):
        print(2)
        assert 0

    def test_login3(self):
        print(3)
        assert 1