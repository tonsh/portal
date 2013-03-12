#coding=utf-8
''' image model '''

import datetime
from libs.utils import _
from models import Image as ImageMod
from business.base import Base
from business.category import Category


class Image(object):
    ''' image model '''
    def get_one_by_id(self, img_id):
        img_id = int(img_id)
        return self.session.query(ImageMapper).filter_by(id=img_id).first()

    def get_all_by_category(self, cid):
        cid = int(cid)
        return self.session.query(ImageMapper).filter_by(cid=cid)

    def insert(self, image):
        category = self.validate(image)
        if self.error_dict:
            raise FormError(self.error_dict)

        image['created_at'] = datetime.datetime.now()
        obj = ImageMapper(**image)
        self._insert(obj)

    def validate(self, image):
        ''' 数据验证 '''
        save_data = {
            'title': self.validate_title(image.get('title', '')),
            'content': self.validate_content(image.get('content', '')),
            'cid': self.validate_cid(image.get('cid', 0)),
        }
        return save_data

    def validate_title(self, title):
        ''' 图像标题验证 '''
        title = title.strip()
        if not title:
            title = _("未命名")
        return title

    def validate_content(self, content):
        ''' 内容验证 '''
        content = content.strip()
        return content

    def validate_cid(self, cid):
        cid = int(cid)
        if cid == 0:
            return 0

        cat_info = Category().get_one_by_id(cid)
        if not cat_info:
            raise ForbiddenError(_('非法访问'))
        return cid
