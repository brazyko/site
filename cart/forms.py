from django.forms import ModelForm
from .models import ShippingData


class ShippingForm(ModelForm):
    class Meta:
        model = ShippingData
        fields = ['name','surname','phone_number','city','viddil']
       