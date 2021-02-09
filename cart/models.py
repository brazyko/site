from django.db import models
from users.models import Profile
from parts.models import Product
from django.contrib.auth.models import User
# Create your models here.


class OrderItem(models.Model):
    part = models.OneToOneField(Product, on_delete= models.SET_NULL,null=True)
    in_order = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.part.title

class Order(models.Model):
    ORDERED = 'ORD'
    PREPARING  = 'PRP'
    SHIPPING = 'SHP'
    DELIVERED = 'DLV'
    ORDER_STATUS_CHOISES = [
        (ORDERED,'Ordered'),
        (PREPARING,'Preparing order'),
        (SHIPPING,'Shipping'),
        (DELIVERED,'Delivered'),
    ]
    
    ref_code = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,null= True)
    items = models.ManyToManyField(OrderItem)
    date_ordered = models.DateField(auto_now=True)
    order_status = models.CharField(
        max_length=3,
        choices=ORDER_STATUS_CHOISES,
        default=ORDERED,
    )

    def get_cart_items(self):
        return self.items.all()

    def get_cart_items_total(self):
        return sum([(item.part.price * item.quantity) for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)