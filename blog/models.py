from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    category = models.ForeignKey("Category")
    content = models.TextField()
    
    def __str__(self):
        return "%s" % (self.title, )
    
class Category(models.Model):
    title = models.CharField(max_length=200)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return "%s" % (self.title, )
