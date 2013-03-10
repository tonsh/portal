#coding=utf=8
''' category business '''

from libs import _
from base import Base
from models import Category as CategoryMod
from models.from_error import FormError
from models.from_error import ForbiddenError

class Category(Base):
    ''' category business '''

    def __init__(self):
        super(Base, self).__init__()

    def get_one_by_id(self, cid):
        cid = int(cid)
        return self.session.query(CategoryMod).filter_by(id=cid).first()

    def insert(self, category):
        category = self.validate(category)
        if self.error_dict:
            raise FormException(self.error_dict)

        category['created_at'] = datetime.datetime.now()
        obj = CategoryMod(**category)
        self._insert(obj)

    def update(self, cid, category):
        cid = int(cid)
        category = self.validate(category)
        if self.error_dict:
            raise FormException(self.error_dict)

        obj = self.session.query(CategoryMod).filter_by(id=cid)
        self._update(obj, category)

    def delete(self, cid):
        cid = int(cid)
        obj = self.session.query(CategoryMod).filter_by(id=cid)
        self._delete(obj)

    def validate(self, category):
        ''' 数据验证 '''
        save_data = {
            'title': self.validate_title(category.get('title', '')),
            'parent': self.validate_parent(category.get('parent', 0)),
        }
        return save_data

    def validate_title(self, title):
        ''' 标题验证 '''
        title = title.strip()
        if not title:
            self.error_dict['title'] = _('标题不能为空')
        return title

    def validate_parent(self, cid):
        cid = int(cid)
        if cid == 0:
            return 0

        cat_info = self.get_one_by_id(cid)
        if not cat_info:
            raise ForbiddenError(_('非法访问'))
        return cid

    def get_children(self, cid):
        ''' 获取一个节点下的子节点 '''
        cid = int(cid)
        return self.session.query(CategoryMod).find(parent=cid)

    def reget_children(self, cid):
        ''' 递归获取一个节点下的子节点 '''
        tree = dict({})

        children = self.get_children(cid)
        if not children:
            return None
        for child in children:
            tree[child.id] = self.get_children(child.id)

        return tree
