from django.db import models
import uuid

from django.contrib.auth.models import User

class Product(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('tops_and_tshirts', "Tops and T-Shirts"),
        ('polo_and_shirts', "Polo and Shirts"),
        ('jerseys', "Jerseys"),
        ('shorts', "Shorts"),
        ('pants_and_leggings', "Pants and Leggings"),
        ('hoodies_and_sweatshirts', "Hoodies and Sweatshirts"),
        ('jacket_and_tracktops', "Jacket and Tracktops"),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def increment_views(self):
        self.product_views += 1
        self.save()