from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)
    @staticmethod
    def get_all_category():
        return Category.objects.all()

    



    def __str__(self):
        return self.name
    

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=250)
    image=models.ImageField( upload_to="static/products")

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_by_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()

    @staticmethod
    def get_by_ids(ids):
        return Product.objects.filter(id__in=ids)


    def __str__(self):
        return self.name


class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    phone_num=models.CharField(max_length=50,default="",blank=True)
    address=models.CharField(max_length=250,default="",blank=True)


