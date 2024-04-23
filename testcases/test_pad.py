import unittest
from api.api_login import Login
from api.api_pad import Pad
from common import read_data
import config


class TestPad(unittest.TestCase):

    def setUp(self):
        self.login = Login()
        self.pad = Pad()

    def test01_login(self):
        res = self.login.api_login()
        print(res.json())
        self.assertEqual(200,res.status_code)
        self.assertEqual("success",res.json().get("message"))
        self.assertIn("token",res.json().get("resultData"))

    def test02_getpreferenceinfo(self):
        res = self.pad.api_getpreferenceinfo()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertIn("max", res.json().get("data")[0].get("preference_key"))

    def test03_theme(self):
        res = self.pad.api_theme()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))

    def test04_refresh_setting(self):
        res = self.pad.api_refresh_setting()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertIn("true", res.json().get("data").get("isRefresh"))

    def test05_userchange_connusers(self):
        res = self.pad.api_userchange_connusers()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertIn("user_pkid", res.json().get("data")[0])

    def test06_datacvg_ask(self):
        res = self.pad.api_datacvg_ask()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual(False, res.json().get("data"))

    def test07_index(self):
        res = self.pad.api_index()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertIn("userInfo", res.json().get("data"))

    def test08_info(self):
        res = self.pad.api_info()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual("3162594727557226953807", res.json().get("data").get("user_pkid"))

    def test09_find_personalsetting(self):
        res = self.pad.api_find_personalsetting()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual("141776322849763954", res.json().get("data").get("144525042344232951").get("res_leftId"))


    def test10_kpi_permission(self):
        res = self.pad.api_kpi_permission()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual("Y-B", res.json().get("data").get("kpiPermission").get("result"))

    def test11_sandtable_permission(self):
        res = self.pad.api_sandtable_permission()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual(True, res.json().get("data").get("sandTablePermission"))

    def test12_watermark(self):
        res = self.pad.api_watermark()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual("mobile", res.json().get("data").get("additionalContent"))

    def test13_issuePermission(self):
        res = self.pad.api_issuePermission()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual(True, res.json().get("data").get("sandTableIssuePermission"))

    def test14_two_dimensional_export_config(self):
        res = self.pad.api_two_dimensional_export_config()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))

    def test15_magnitude(self):
        res = self.pad.api_magnitude()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual("一", res.json().get("data").get("indexMagnitude")[4].get("mnt_description"))

    def test16_v2_loadtreenodes(self):
        res = self.pad.api_v2_loadtreenodes()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual("LSWD_017", res.json().get("data")[0].get("index_id"))

    def test17_v2_loadClassicition(self):
        res = self.pad.api_v2_loadClassicition()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual("LSWD_017", res.json().get("data")[0].get("listData")[0].get("index_id"))

    def test18_layout(self):
        res = self.pad.api_layout()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual("N", res.json().get("data").get("ReportShowLayoutParams").get("ALLOW_EXPORT"))

    def test19_note(self):
        res = self.pad.api_note()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual("https://www.baidu.com/", res.json().get("data"))

    def test20_click(self):
        res = self.pad.api_click()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual("_true_", res.json().get("data"))

    def test21_select_search_records(self):
        res = self.pad.api_select_search_records({"user_pkid": 3162594727557226953807})
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual([], res.json().get("data"))

    def test22_rule(self):
        res = self.pad.api_rule()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual("day,week,month,season,year", res.json().get("data").get("defaultType").get("sort"))

    def test23_message_info(self):
        res = self.pad.api_message_info({"pageIndex": 1, "pageSize": 30})
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertEqual(["1", "2", "5"], res.json().get("data").get("modules"))



    def test24_page(self):
        res = self.pad.api_page()
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertIn("dimensions", res.json().get("data").get("positionPage")[0])

    def test25_dimension(self):
        filename = config.BASE_DIR + "/data/dimension_data.json"
        json_data = read_data.read_dimension_data(filename)
        for dimension in json_data:
            res = self.pad.api_dimesion(dimension)
            print(res.json())
            self.assertEqual(200, res.status_code)
            self.assertEqual("成功", res.json().get("message"))
            self.assertEqual(True, res.json().get("success"))
            self.assertIn("d_res_name", res.json().get("data").get("indexPadDimension")[0])

    def test26_position(self):
        filename = config.BASE_DIR + "/data/position_data.json"
        print(filename)
        json_data = read_data.read_position_data(filename)
        res = self.pad.api_position(json_data)
        print(res.json())
        self.assertEqual(200, res.status_code)
        self.assertEqual("成功", res.json().get("message"))
        self.assertEqual(True, res.json().get("success"))
        self.assertIn("index_id", res.json().get("data").get("indexPosition")[0])

    def test27_show(self):
        filename = config.BASE_DIR + "/data/show_data.json"
        json_data = read_data.read_dimension_data(filename)
        for show in json_data:
            res = self.pad.api_show(show)
            print(res.json())
            self.assertEqual(200, res.status_code)
            self.assertEqual("成功", res.json().get("message"))
            self.assertEqual(True, res.json().get("success"))
            self.assertIn("index_id", res.json().get("data").get("indexChart")[0])
