from django.db import models


def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user, filename)

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100)



class Feed(models.Model):
    #upload = models.ImageField(upload_to =user_directory_path)
    user = models.CharField(max_length=100)
    upload = models.ImageField(upload_to = user_directory_path)