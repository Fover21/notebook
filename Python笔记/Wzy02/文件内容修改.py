'''
    吃的文件内容：
    过油肉菜
    尖椒菜
    娃娃菜
'''

import os
with open("吃的", mode="r", encoding="utf-8") as f1, \
        open("吃的_副本", mode="w", encoding="utf-8") as f2:
    # s = f1.read()
    # ss = s.replace("肉", "菜")
    # f2.write(ss)
    for line in f1:
        s = line.replace("菜", "肉")
        f2.write(s)

os.remove("吃的") #　删除文件
os.rename("吃的_副本", "吃的") # 重命名文件

结果：
‘’‘
过油肉肉
 尖椒肉
娃娃肉
’‘’