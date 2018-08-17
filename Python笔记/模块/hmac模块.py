# hmac模块使用步骤：
# hmac模块模块的使用步骤与hashlib模块的使用步骤基本一致，只是在第1步获取hmac对象时，只能使用hmac.new()函数，
# 因为hmac模块没有提供与具体哈希算法对应的函数来获取hmac对象。

# hmac_demo.py HMAC算法
# 与hashlib不同之处在于多了key
 
import hmac
 
 
def hmac_demo():
  # 加密
  h = hmac.new(b"sore")
  h.update(b"me")
  h_str = h.hexdigest()
  print(h_str)
 

  # 比较密码
  boolean = hmac.compare_digest(h_str, hmac.new(b"sore", b"me").hexdigest())
  print(boolean)
 
  
 
def hmac_func():
  # 创建key和内容,再都进行加密
  # hmac.new(key, msg=None, digestmod=None) // 创建新的hmac对象, key:键, msg:update(msg), digestmod:hash名称(同hashlib.new())(默认md5)
  hc = hmac.new(b"key")
  print(hc)
  # hmac对象
  hc.update(b"msg") # 字节缓冲区 hc.update(a) hc.update(b) == hc.update(a+b)
  hash_bytes = hc.digest() # 字节hash
  hash_str = hc.hexdigest() # 16进制hash字符串
  hc = hc.copy() # 拷贝hmac副本
  strs = hc.name # hash名称
  print(hc, strs)
  # hmac.compare_digest(a, b) // 比较两个hash密钥是否相同, 参数可为: str / bytes-like object, (注:建议使用,不建议使用a==b)
  boolean = hmac.compare_digest(hmac.new(b"net", b"luzhuo.me").digest(), hmac.new(b"net", b"luzhuo.me").digest())
  print(boolean)
  
 
 
if __name__ == "__main__":
  hmac_demo()
 
  hmac_func()


