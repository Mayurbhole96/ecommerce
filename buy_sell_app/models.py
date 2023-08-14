from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name = "Title")
    details = models.TextField(verbose_name = "Details")
    attached_files = models.FileField(upload_to='product_attatch/', blank=True, null=True)
    price = models.CharField(max_length=20, verbose_name = "Price")
    seller = models.ForeignKey(User,verbose_name="Seller",related_name="seller_id", on_delete=models.PROTECT)
    created_date_time = models.DateTimeField(verbose_name="Created Date Time",auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")

    class Meta:
        db_table = "tbl_product"
        verbose_name_plural = "Products"

    def delete(self):
        self.is_deleted = True
        self.is_active = False
        self.save()

    def __str__(self):
        return "%s (ID:%s)" % (self.title, self.id)
    
class Cart(models.Model):
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User,related_name="buyer_cart_id", on_delete=models.CASCADE)
    seller = models.ForeignKey(User,related_name="seller_cart_id", on_delete=models.CASCADE)
    
    is_active = models.BooleanField(default=True, verbose_name='Is Active')
    is_deleted = models.BooleanField(default=False, verbose_name="Is Deleted")

    class Meta:
        db_table = "tbl_cart"
        verbose_name_plural = "Cart"

    def delete(self):
        self.is_deleted = True
        self.is_active = False
        self.save()

    def __str__(self):
        return "%s (ID:%s)" % (self.product_id.title, self.id)    
