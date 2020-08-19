from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Product(models.Model):
    product_id = models.AutoField(primary_key=True, auto_created=True, validators=[
        RegexValidator(
            regex='^\d{8,}*$',
            message='Product ID Should be atleast 8 characters',
            code='invalid_product_id'
        ),
    ])
    product_name = models.CharField(max_length=50)
    product_desc = models.CharField(max_length=300)
    publish_date = models.DateField()
    product_price = models.FloatField()
    product_available = models.BooleanField(default=True)
    product_quantity = models.IntegerField(default=1)
    product_mrp = models.IntegerField(default=1)

    def __str__(self):
        return self.product_name
