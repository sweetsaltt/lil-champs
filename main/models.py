from django.db import models

class Product(models.Model):    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    
    # def __str__(self):
    #     return self.title
    
    # @property
    # def is_news_hot(self):
    #     return self.news_views > 20
        
    # def increment_views(self):
    #     self.news_views += 1
    #     self.save()