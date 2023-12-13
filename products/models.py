# products/models.py
from django.db import models

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    brand = models.CharField(max_length=50, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py runserver

