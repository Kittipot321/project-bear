from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    tel = models.CharField(max_length=10,null=True)
    picture = models.ImageField(default='user/default_pic.png',upload_to='user',null=True,blank=True)

class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

class Type(models.Model):
    type_name = models.CharField(max_length=255)
    def __str__(self):
        return self.type_name
    
class Product(models.Model):
    type = models.ForeignKey(Type, on_delete=models.PROTECT,null=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255,null=True)
    price = models.FloatField()
    stock = models.IntegerField()
    picture = models.ImageField(default='product_pic/default.png',upload_to='product_pic',null=True,blank=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    date = models.DateTimeField()
    customer = models.ForeignKey(User, on_delete=models.PROTECT,null=True)
    total_price = models.FloatField()
    status = models.BooleanField(default=False)

class Order_items(models.Model):
    item_no = models.ForeignKey(Product, on_delete=models.PROTECT,null=True)
    unit = models.IntegerField()
    price = models.FloatField()
    item_price = models.FloatField()

class Order_Products(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    amount = models.IntegerField(null=True)

class Payment(models.Model):
    pay_id = models.ForeignKey(Order, on_delete=models.CASCADE,null=True)
    pay_time = models.DateTimeField(auto_now=True)
    pay_name = models.CharField(max_length=255,null=True)
    pay_file = models.ImageField(upload_to='customer_data_via_bank',null=True,blank=True)
    pay_status = models.CharField(max_length=255,null=True)
    