
from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import TextChoices

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
    date=models.DateTimeField(auto_now_add=True)
    status_choice=(
        ('1', 'Pending'),
        ('2', 'Packed'),
        ('3', 'on the way'),
        ('4','Delivered'),
        ('5',"Cancelled"),
    )
    status=models.CharField(max_length=1,choices=status_choice)
    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_of_user(user_id):
        return Order.objects.filter(customer=user_id).order_by("-date")

    




