#coding=utf-8
''' 封装 Mako 渲染模板的类 '''

from mako.template import Template
from mako.lookup import TemplateLookup
from settings import TMPL_LOOKUP

class MakoTemplater(object):
    ''' 封装 Mako 渲染模板的类 '''
    _lookup = None

    def __init__(self):
        pass

    @classmethod
    def render(cls, tmpl_name, **context):
        ''' 模板渲染 '''
        if not cls._lookup:
            cls._lookup = MakoTemplater()._get_lookup()

        return cls._lookup.get_template(tmpl_name).render(**context)

    def _get_lookup(self):
        ''' 通过 TemplateLookup 获取模板对象 '''
        return TemplateLookup(**TMPL_LOOKUP)
