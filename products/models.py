from django.db import models
from django.utils.text import slugify
from category.models import Category

class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="products/images")
    sku = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate slug from name
        if not self.slug:  # Only slugify if slug is not already set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
