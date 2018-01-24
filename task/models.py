from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Post_Email(models.Model):

    email_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.email_name


# Create your models here.

@python_2_unicode_compatible
class Used(models.Model):
    used = models.CharField(max_length=30,verbose_name="used")

    def __str__(self):
        return self.used