from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(unique = True,allow_unicode = True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(default='default.jpg',blank=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    def __str__ (self):
        return self.title

    def pangah_ta_gelo_boro (self):
        return self.body[0:50] + ' ...'
