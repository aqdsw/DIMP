import requests
import config
from data import data
from common import read_data
import json


class Login:
    def api_login(self):
        res = requests.post(url=config.BASE_URL + "/uac/loginauth", params=data.login_data)
        # print(res.json()
        token = "ticket " + res.json().get("resultData").get("token")
        config.headers["Authorization"] = token
        # print(token)
        return res


    # json_data = read_data.read_dimension_data("../data/dimension_data.json")
    # print(json_data)

    # def api_page():
    #     res = requests.get(url=config.BASE_URL + '/api/ddb/indexpad/v2/resource/library/position/page',
    #                        headers=config.headers)
    #     # print(res.json())
    #     res_dimension = res.json()
    #     # print(res_dimension)
    #     dimensions_values = []
    #     position_pages = res_dimension["data"]["positionPage"]
    #     for page in position_pages:
    #         dimensions_str = page["dimensions"]
    #         # print(dimensions_str)
    #         dimensions_str = dimensions_str.replace('[', '').replace(']', '')  # 去除多余的方括号
    #         # print(dimensions_str)
    #         dimensions = dimensions_str.split('","')  # 按逗号分隔维度值
    #         # print(dimensions)
    #         dimensions = [dim.strip('"') for dim in dimensions]  # 去除额外的引号
    #         # print(dimensions)
    #         dimensions_values.extend(dimensions)
    #         # print(dimensions)
    #     return dimensions_values
    #
    # def api_dimesion():
    #
    #     # for i in json_data:
    #     #     res = requests.post(url=config.BASE_URL + "/api/ddb/indexpad/indexChart/dimension",
    #     #                         json=i,
    #     #                         headers=config.headers)
    #     #     # print(config.headers)
    #     #     print(res.json())
    #     #     print("---------------------------------")
    #     json = {"timeVal": "202312"}
    #     dimension_name = api_page()
    #     for dimension_value in dimension_name:
    #         # print(dimension_value)
    #         json["dimensionArr"] = [dimension_value]
    #         res = requests.post(url=config.BASE_URL + "/api/ddb/indexpad/indexChart/dimension",
    #                             json=json,
    #                             headers=config.headers)
    #         # print(res.json())
    #
    #
    # def api_position():
    #     json = {
    #             "page": "1",
    #             "add_type": "F",
    #             "shareUserPkId": "3162594727557226953807"
    #             }
    #     res = requests.post(url=config.BASE_URL + "/api/ddb/indexpad/index/position",
    #                         json=json,
    #                         headers=config.headers)
    #     print(res.json())
    #
# if __name__ == '__main__':
#     API_LOGIN = api_login()
#     API_PAGE = api_page()
#     API_DIMENSION = api_dimesion()
#     API_POSITION = api_position()











