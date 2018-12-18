import time

def wai(func):
    def inner(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        return end - start
    return inner

@wai # wai(wuxianxunhuan--def) -> inner -> inner() -> 执行函数
def wuxianxunhuan(): # inner
    for i in range(9999):
        for j in range(9999):
            continue
 
    
# print(wuxianxunhuan())