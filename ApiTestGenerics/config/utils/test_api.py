from Testcase import ApiTest
import pytest
'''

class TestAssert(TestCase):
	def test_request(self):
		a=ApiTest("",403,"get")
		response=a.callapi()

		assert (response.status_code)==a.success_status_code
'''

import pytest


#@pytest.mark.incremental
class Test_UserHandling:
    def test_login(self):
        a=ApiTest("login/",200,"post",{"email":"golubajpai302@gmail.com","password":"Priyam@13"})
        self.k=a.api()
        assert a.success_status_code==self.k.status_code

    def test_modification(self):
        pass

    def test_deletion(self):
        pass

class Test_UserHandling2:
    def test_login(self):
        a=ApiTest("login/",200,"post",{"email":"golubajpai302@gmail.com","password":"Priyam@13"})
        self.k=a.api()
        assert a.success_status_code==self.k.status_code

    def test_modification(self):
        pass

    def test_deletion(self):
        pass
