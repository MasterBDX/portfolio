import random
import string
import os
from django.utils.text import slugify
from . import models


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# def unique_slug_generator(instance, new_slug=None):
#     """
#     This is for a Django project and it assumes your instance
#     has a model with a slug field and a title character (char) field.
#     """
#     if new_slug is not None:
#         slug = new_slug
#     else:
#         slug = slugify(instance.username)

#     klass = instance.__class__
#     qs_exists = klass.objects.filter(slug=slug).exists()
#     if qs_exists:
#         new_slug = "{slug}-{randstr}".format(
#                     slug=slug,
#                     randstr=random_string_generator(size=5)
#                 )
#         return unique_slug_generator(instance, new_slug=new_slug)
#     return slug


def get_propic_name(title,image_name):
    slug_title = slugify(title)
    imgName,imgExt = os.path.splitext(image_name)
    random_str = random_string_generator(size=6)
    img_name = slug_title + '-' + random_str + imgExt
    img_path = os.path.join('projects_pictures',img_name)
    return img_path
