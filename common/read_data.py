import json

def read_dimension_data(filename):
    with open(filename,mode='r',encoding='utf-8') as f:
        jsonData = json.load(f)
        result_list = []
        for i in jsonData:
            result_list.append(i)

        return result_list


def read_position_data(filename):
    with open(filename,mode='r',encoding='utf-8') as f:
        jsonData = json.load(f)
        return jsonData


# if __name__ == '__main__':
#     read_position_data = read_position_data("../data/position_data.json")

