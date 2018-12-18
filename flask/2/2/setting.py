class Debug(object):
    DEBUG=True
    SECRET_KEY="jinwangba"
    SESSION_COOKIE_NAME = "jinwangba's session"

class Testing(object):
    TESTING=True
    SECRET_KEY="yinwangba"
    SESSION_COOKIE_NAME = "yinwangba's session"
    
class XianShang(object):
    SECRET_KEY = "KingEight"
    SESSION_COOKIE_NAME = "CSRF_TOKEN"