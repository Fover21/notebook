#需求：

# 一个类
# 对象的属性 : 姓名 性别 年龄 部门
# 员工管理系统
# 内部转岗 python开发 - go开发
# 姓名 性别 年龄 新的部门
# A men 83 python
# A men 85 go

# 1000个员工
# 如果几个员工对象的姓名和性别相同,这是一个人
# 请对这1000个员工做去重


#用到了set的内层如何实现，先hash，如果hash值一样的话，没比较两个数的值，会用到__eq__方法



class Employee:
    def __init__(self, name, age, sex, partment):
        self.name = name
        self.age = age
        self.sex = sex
        self.partment = partment

    def __hash__(self):
        return hash('%s%s'%(self.name, self.age))

    def __eq__(self, other):
        return True if self.name == other.name and self.age == other.age else False

employee_list = []

for i in range(10):
    employee_list.append(Employee('Jake', 'men', i, '1'))

for i in range(10):
    employee_list.append(Employee('Tom', 'men', i, '2'))

for i in range(10):
    employee_list.append(Employee('Peter', 'men', i, '3'))

# print(employee_list)

employee_list = set(employee_list)

for i in employee_list:
    print(i)
