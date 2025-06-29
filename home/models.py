from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
def min_length(value):
    if len(value) < 5:
        raise ValidationError("عدد حداقلی کم است")


class Category (models.Model):
    name = models.CharField(max_length=15)
    icon = models.ImageField(upload_to= 'category/')

    def __str__(self):
        return self.name


class Item (models.Model):
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to= 'items/')
    price = models.CharField(max_length=8,validators=[min_length])
    description = models.TextField(max_length=60)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CategoryForGallery(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    cat = models.ForeignKey(CategoryForGallery, on_delete=models.CASCADE)

