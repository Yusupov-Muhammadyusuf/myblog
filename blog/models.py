from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = CKEditor5Field('Content', config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title