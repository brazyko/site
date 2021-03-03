from django.db import models
from users.models import Profile
from parts.models import Product2
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import RegexValidator

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    part = models.ForeignKey(Product2, on_delete= models.SET_NULL,null=True)
    in_order = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.part.index

class Order(models.Model):
    INCART     = 'INC'
    ORDERED    = 'ORD'
    PREPARING  = 'PRP'
    SHIPPING   = 'SHP'
    DELIVERED  = 'DLV'
    ORDER_STATUS_CHOISES = [
        (INCART,'In cart'),
        (ORDERED,'Ordered'),
        (PREPARING,'Preparing order'),
        (SHIPPING,'Shipping'),
        (DELIVERED,'Delivered'),
    ]
    
    ref_code = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,null= True)
    items = models.ManyToManyField(CartItem)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(
        max_length=3,
        choices=ORDER_STATUS_CHOISES,
        default=INCART,
    )

    def get_cart_items(self):
        return sum([item.quantity for item in self.items.all()])

    def get_cart_items_total(self):
        return sum([(item.part.price * item.quantity) for item in self.items.all()])

    def __str__(self):
        return '{0} - {1}'.format(self.owner, self.ref_code)

class ShippingData(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30,verbose_name="Ім'я")
    surname = models.CharField(max_length=30,verbose_name="Прізвище")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+380999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=False,verbose_name="Номер телефону") # validators should be a list
    city = models.CharField(max_length=40,verbose_name="Місто/Село")
    viddil = models.IntegerField(verbose_name="Відділ НП")

    def __str__(self):
        return self.surname