# lst1 = ["金毛狮王", "紫衫龙王", "白眉鹰王", "青衣服往"]
# lst2 = lst1 # 列表, 进行赋值操作. 实际上是引用内存地址的赋值. 内存中此时只有一个列表. 两个变量指向一个列表
#
# lst2.append("杨做事")  # 对期中的一个进行操作. 两个都跟着变
# print(lst2)
# print(lst1)


# 浅拷贝 copy 创建新对象
# lst1 = ["赵本山", "刘能", "赵四"]
# # lst2 = lst1.copy()  # lst2 和lst1 不是一个对象了
# lst2 = lst1[:]  # 切片会产生新的对象
# lst1.append("谢大脚")
# print(lst1, lst2)
# # print(id(lst1), id(lst2))


# lst1 = ["超人", "七龙珠", "葫芦娃", "山中小猎人", ["金城武", "王力宏", "渣渣辉"]]
# lst2 = lst1.copy()  # 拷贝. 浅拷贝 拷贝第一层
#
# lst1[4].append("大阳哥")
#
# print(lst1, lst2)
# 深拷贝

import copy
lst1 = ["超人", "七龙珠", "葫芦娃", "山中小猎人", ["金城武", "王力宏", "渣渣辉"]]
lst2 = copy.deepcopy(lst1)  # 把lst1扔进去进行深度拷贝 , 包括内部的所有内容进行拷贝
lst1[4].append("大阳哥")
print(lst1, lst2)

# 为什么要有深浅拷贝
# 拷贝比创建对象的过程要快
