# class Person():
#     def show_info(self):
#         print("调用方法")
#         pass
#
# p2 = Person()
# print("p2",id(p2))
#
# p2.name = "zhangsan"
# p2.show_info()


class Person():
    def __init__(self,new_name,new_age):
        self.new_name = new_name
        self.new_age = new_age
    def show_info(self):
        print(self.new_name,self.new_age)


p1 = Person("王五",20)
p1.show_info()

#关键字参数传递
p2 = Person(new_name="zhangsan",new_age=20)
p2.show_info()

person_dict = {"new_name":"赵四","new_age":20}
p3 = Person(**person_dict)
p3.show_info()

my_list = [{"new_name": "朱八", "new_age": 30}, {"new_name": "刘三", "new_age": 30}]
new_list = [Person(**person_dict) for person_dict in my_list]
# new_list_1 = dict(new_list)
print(new_list,type(new_list))

#遍历每一个对象，调用show_info方法
for i in new_list:
    i.show_info()

