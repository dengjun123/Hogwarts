import pytest
# class TestDemo:
#     def test_fun(self,x):
#         return x + 1
#
#     def test_answer(self):
#         assert self.fun(2) == 3


# @pytest.fixture(scope="module")
# def open():
#     print("通用")
#     yield
#     print("执行后的操作")
#
# def test_1(open):
#     print("test1")
#     # a = "h"
#     # # assert a not in "hello"
#     # pytest.assume(a not in 'hello')
#     # pytest.assume(1==2)
#     # pytest.assume(a  in 'hello')
#
# def test_2(open):
#     print("test2")
#     # a = 'h'
#     # assert a in "hello"
#
# def test_3(open):
#     print("test3")
    # a = 1
    # b = 2
    # c = a + b
    # assert c == 4


#参数化
# @pytest.mark.parametrize("use,pwd",[("Tom",123),("Amy",456),("Cherry",789)])
# #命名规则一定要以test开头
# def test_login(use,pwd):
#     # print(f"用户名是：{use},密码是：{pwd}")
#     print(use,pwd)
#

#
# @pytest.mark.parametrize("test_input,expected",[("3+5",8),("3+5",8),("3+7",81)])
# def test_eval(test_input,expected):
#     #eval 将字符串转化为数字对比
#     assert eval(test_input) == expected



#组合传参
# @pytest.mark.parametrize("a",[1,2])
# @pytest.mark.parametrize("b",[3,4,5])
# def test_demo1(a,b):
#     print(a + b)
#     return a + b


#方法名传参
test_list = [1,2]
@pytest.fixture(scope="module")
def common_1(request):
    #这里接收并传入的参数
    data1 = request.param
    print("列表数据为：%d"%data1)
    return data1

#indirect=True 可以把传过来的参数都函数来执行
@pytest.mark.parametrize("common_1",test_list,indirect=True)
def test_method(common_1):
    print(common_1)
    return common_1
    assert common_1 != ""

def test_add():
    print("haha")


if __name__ == "__main__":
    # pytest.main("-v -s TestDemo")
    # pytest.mian(["-v","-s","TestDemo"])
    pytest.main()
