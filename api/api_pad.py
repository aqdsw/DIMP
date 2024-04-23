import requests
import config
from data import data
from common import read_data
import json


class Pad:
    def api_getpreferenceinfo(self):
        res = requests.get(url=config.BASE_URL + "/api/portal/user/getpreferenceinfo",
                           headers=config.headers)
        return res

    def api_theme(self):
        res = requests.get(url=config.BASE_URL + "/api/portal/user/default/theme",
                           headers=config.headers)
        return res

    def api_refresh_setting(self):
        res = requests.get(url=config.BASE_URL + "/api/portal/user/refresh_setting",
                           headers=config.headers)
        return res
    def api_userchange_connusers(self):
        res = requests.get(url=config.BASE_URL + "/api/portal/user/userchange_connusers",
                           headers=config.headers)
        return res

    def api_datacvg_ask(self):
        res = requests.get(url=config.BASE_URL + "/api/portal/user/datacvg_ask",
                           headers=config.headers)
        return res

    def api_index(self):
        res = requests.get(url=config.BASE_URL + "/api/portal/user/index",
                           headers=config.headers)
        return res

    def api_message_info(self,jsonData):
        res = requests.post(url=config.BASE_URL + "/api/portal/user/message_info",
                           headers=config.headers,
                           json=jsonData)
        return res

    def api_info(self):
        res = requests.get(url=config.BASE_URL + "/api/portal/user/info",
                           headers=config.headers)
        return res

    def api_find_personalsetting(self):
        res = requests.get(url=config.BASE_URL + "/api/portal/find_personalsetting",
                           headers=config.headers)
        return res

    def api_kpi_permission(self):
        res = requests.get(url=config.BASE_URL + "/api/ddb/indexpad/kpi/permission",
                           headers=config.headers)
        return res

    def api_sandtable_permission(self):
        res = requests.get(url=config.BASE_URL + "/api/ddb/indexpad/sandtable/permission",
                           headers=config.headers)
        return res

    def api_watermark(self):
        res = requests.get(url=config.BASE_URL + "/api/portal/user/watermark.do",
                           headers=config.headers)
        return res

    def api_issuePermission(self):
        res = requests.get(url=config.BASE_URL + "/api/ddb/indexpad/sandtable/issuePermission",
                           headers=config.headers)
        return res

    def api_two_dimensional_export_config(self):
        res = requests.get(url=config.BASE_URL + "/api/ddb/two_d/v2/show/two_dimensional_export_config",
                           headers=config.headers)
        return res

    def api_magnitude(self):
        res = requests.get(url=config.BASE_URL + "/api/ddb/indexpad/index/magnitude",
                           headers=config.headers)
        return res

    def api_v2_loadtreenodes(self):
        res = requests.get(url=config.BASE_URL + "/api/ddb/indexpad/v2_loadtreenodes",
                           headers=config.headers)
        return res

    def api_v2_loadClassicition(self):
        res = requests.get(url=config.BASE_URL + "/api/ddb/indexpad/v2_loadClassicition",
                           headers=config.headers)
        return res

    def api_layout(self):
        res = requests.get(url=config.BASE_URL + "/api/report/show/layout",
                           headers=config.headers)
        return res

    def api_note(self):
        res = requests.get(url=config.BASE_URL + "/api/ddb/indexpad/index/note",
                           headers=config.headers)
        return res

    def api_click(self):
        res = requests.get(url=config.BASE_URL + "/api/ddb/indexpad/index/default/click",
                           headers=config.headers)
        return res

    def api_select_search_records(self,Data):
        res = requests.get(url=config.BASE_URL + "/api/ddb/indexpad/select_search_records",
                           params=Data,
                           headers=config.headers)
        return res

    def api_rule(self):
        res = requests.get(url=config.BASE_URL + "/api/ddb/indexpad/time/default/rule",
                           headers=config.headers)
        return res

    def api_page(self):
        res = requests.get(url=config.BASE_URL + '/api/ddb/indexpad/v2/resource/library/position/page',
                           headers=config.headers)
        return res

    def api_dimesion(self,jsonData):
        # json_data = read_data.read_dimension_data("../data/dimension_data.json")
        # for dimension in json_data:
        res = requests.post(url=config.BASE_URL + "/api/ddb/indexpad/indexChart/dimension",
                                json=jsonData,
                                headers=config.headers)
            # print(config.headers)
        return res

    def api_position(self,filename):
        # json_data = read_data.read_position_data("../data/position_data.json")
        res = requests.post(url=config.BASE_URL + "/api/ddb/indexpad/index/position",
                            json=filename,
                            headers=config.headers)
        return res

    def api_show(self,jsonData):
        # json_data = read_data.read_dimension_data("../data/show_data.json")
        # for show in json_data:
        res = requests.post(url=config.BASE_URL + "/api/ddb/indexpad/position/show",
                            json=jsonData,
                            headers=config.headers)
            # print(config.headers)
        return res
