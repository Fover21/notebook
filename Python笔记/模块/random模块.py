import random

print(random.randrange(1, 10))  # 返回1-10之间的一个随机数，不包括10

print(random.randint(1, 10))  # 返回1-10之间的随机数，包括10

print(random.random())  # 生成0-1的随机数，随机浮点数

print(random.choice('hello word!'))  # 随机选取字符串中的一个字符
print(random.choices('hello word!'))  # 随机选取字符串中的一个字符，以列表形式返回

print(random.sample('hello word', 3))  # 从多个字符中选出特定数量的字符，以列表形式返回

lis = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(lis)  # 洗牌，将列表内容随机打乱
print(lis)

import string

# 生成随机字符串
s = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
print(s)


结果：
	5
	1
	0.1861546218534702
	r
	['w']
	['h', 'w', 'r']
	[7, 5, 3, 2, 4, 1, 6]
	y9qxeo