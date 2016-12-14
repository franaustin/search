from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(u"blog name",max_length=50,null=False,blank=False)
    description = models.TextField(u"description",null=True,blank=True)
    create_time = models.DateTimeField(null=True)
