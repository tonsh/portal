#coding=utf-8
''' image model '''

import os
import datetime
import imghdr
import pystacia
from settings import IMAGE_RESOURCES
from settings import IMAGE_MAX_SIZE
from settings import IMAGE_MAX_WIDTH
from settings import IMAGE_MAX_HEIGHT
from libs.utils import _
from libs.utils import make_file_name
from business.base import Base
from models import Image as ImageMod
from business.category import Category
from libs.errors import FormError
from libs.errors import ForbiddenError

class Image(Base):
    ''' image model '''
    def get_one_by_id(self, img_id):
        img_id = int(img_id)
        return self.session.query(ImageMod).filter_by(id=img_id).first()

    def get_all_by_category(self, cid):
        cid = int(cid)
        return self.session.query(ImageMod).filter_by(cid=cid)

    def insert(self, image):
        image = self.validate(image)
        if self.error_dict:
            raise FormError(self.error_dict)

        image['created_at'] = datetime.datetime.now()
        obj = ImageMod(**image)
        self._insert(obj)

    def validate(self, image):
        ''' 数据验证 '''
        src_img, thumb_img = self.validate_image(image.get('image'))
        save_data = {
            'title': self.validate_title(image.get('title', '')),
            'content': self.validate_content(image.get('content', '')),
            'cid': self.validate_cid(image.get('cid', 0)),
            'is_topped': self.validate_topped(image.get('is_topped', None)),
            'src_img': src_img,
            'thumb_img': thumb_img,
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

    def validate_topped(self, is_topped):
        if not is_topped:
            return False
        return True

    def validate_image(self, image):
        ''' 检查图片属性 '''
        # 检查图片真实性
        img_type = imghdr.what(image)
        if not img_type:
            self.error_dict['image'] = _('您上传的不是图片文件')
            return None, None

        # 检查图片类型
        if img_type not in ['jpeg','jpg', 'png' 'gif']:
            self.error_dict['image'] = _('上传图片只能为 JPG PNG GIF类型')
            return None, None

        # 检查图片大小
        fsize = os.stat(image).st_size
        if (fsize / 1024.0) > IMAGE_MAX_SIZE:
            self.error_dict['image'] = _('上传图片最大限制为%sK' % IMAGE_MAX_SIZE)
            return None, None

        # 生成缩略图
        thumb_img =self.rescale_image(image, img_type)
        return image, thumb_img

    def rescale_image(self, image, extension):
        ''' 图片缩放 '''
        img_obj = pystacia.read(image)

        # 计算缩放后的宽高
        width, height = img_obj.size
        target_width, target_height = self.rescale_size(width, height)
        img_obj.rescale(int(target_width), int(target_height))

        # 保存缩略图
        thumb_img = make_file_name(extension)
        img_obj.write(thumb_img)
        return thumb_img

    def rescale_size(self, width, height):
        ''' 计算缩放尺寸 '''
        if width < IMAGE_MAX_WIDTH:
            if height > IMAGE_MAX_HEIGHT:
                height = IMAGE_MAX_HEIGHT
        elif height < IMAGE_MAX_HEIGHT:
            width = IMAGE_MAX_WIDTH
        else:
            width = IMAGE_MAX_WIDTH
            height = (width / IMAGE_MAX_WIDTH) * height
            height = min(height, IMAGE_MAX_HEIGHT)
        return width, height
