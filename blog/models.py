from django.db import models

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Post(models.Model):
    serial_no = models.AutoField(primary_key = True)
    title = models.CharField(max_length=100)
    catagory = models.CharField(max_length=15)
    content = RichTextUploadingField()
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=250)
    publish_date = models.DateTimeField(blank= True)

    def __str__(self):
        return 'Post by' + ' ' + self.author

