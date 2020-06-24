import pytest

# @pytest.fixture(scope="module")
# def common_1(request):
#     #这里接收并传入的参数
#     data1 = request.param
#     print("列表数据为：%d"%data1)
#     return data1


# def pytest_collection_modifyitems(session,config,items:list):
#     # print(items)
#     # print(type(items))
#     for item in items:
#         if "method" in item.nodeid:
#             item.add_marker(pytest.mark.method)
#
#     #反向 执行
#     items.reverse()

def pytest_collection_modifyitems(session,config,items:list):
    for item in items:
        if "add" in item.nodeid:
            item.add_marker(pytest.mark.add)
        elif "div" in item.nodeid:
            item.add_marker(pytest.mark.div)