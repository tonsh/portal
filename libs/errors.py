#coding=utf-8
''' 异常类 '''

class BaseError(Exception):
    def __init__(self, msg):
        self.msg = msg


class FormError(BaseError):
    ''' 表单验证错误 '''
    pass


class ForbiddenError(BaseError):
    ''' 非法访问 '''
    pass
