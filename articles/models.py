from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__ (self):
        return self.title

    def pangah_ta_gelo_boro (self):
        return self.body[0:50] + ' ...'
    #in add thumbnail
    #add in author
